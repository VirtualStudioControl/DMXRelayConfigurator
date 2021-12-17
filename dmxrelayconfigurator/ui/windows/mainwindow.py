import json
from time import sleep
from typing import  Optional, List, Dict

from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QWidget, QTabWidget, QLineEdit, QSpinBox, QToolButton, QAction, QFileDialog, \
    QVBoxLayout, QScrollArea

from dmxrelayconfigurator.data import datatools
from dmxrelayconfigurator.dmx import device_manager
from dmxrelayconfigurator.dmx.dmxdevice import DMXDevice
from dmxrelayconfigurator.io.dmxframe_io import writeDMXFrame, readDMXFrame
from dmxrelayconfigurator.logging import logengine
from dmxrelayconfigurator.net import clientprotocol
from dmxrelayconfigurator.net.tcpclient import TCPClient
from dmxrelayconfigurator.tools.bytetools import getStringList, getInt
from dmxrelayconfigurator.ui.widgets.channel_widget import ChannelWidget
from dmxrelayconfigurator.ui.widgets.collapsible_panel import CollapsibleBox
from dmxrelayconfigurator.ui.widgets.dmx_device_widget import DMXDeviceWidget
from dmxrelayconfigurator.ui.widgets.interface_widget import InterfaceWidget
from dmxrelayconfigurator.ui.widgets.universe_widget import UniverseWidget


logger = logengine.getLogger()

CONFIG_KEY_DMX_INTERFACE_PORT = "port"
CONFIG_KEY_DMX_INTERFACE_TYPE = "type"
CONFIG_KEY_DMX_INTERFACE_UNIVERSE = "universe"

CONFIG_KEY_DMX_INTERFACE_USB_VENDOR_ID = "usb_vendor_id"
CONFIG_KEY_DMX_INTERFACE_USB_PRODUCT_ID = "usb_product_id"
CONFIG_KEY_DMX_INTERFACE_USB_BUS = "usb_bus"
CONFIG_KEY_DMX_INTERFACE_USB_ADDRESS = "usb_address"

class MainWindow(QMainWindow):

    onConfigGotten = pyqtSignal()
    onDMXSceneGotten = pyqtSignal()

    def __init__(self):
        """
        Constructor
        """
        super().__init__()

        self.connection_address: Optional[QLineEdit] = None
        self.connection_port: Optional[QSpinBox] = None
        self.connection_username: Optional[QLineEdit] = None
        self.connection_password: Optional[QLineEdit] = None

        self.client_connect_button: Optional[QToolButton] = None

        self.interface_container: Optional[QWidget] = None
        self.add_interface_button: Optional[QToolButton] = None
        self.push_interface_configuration_button: Optional[QToolButton] = None

        self.device_list: Optional[QWidget] = None
        self.universetabwidget: Optional[QTabWidget] = None

        self.actionDMXFrameBin: Optional[QAction] = None
        self.action_import_DMXFrameBinary: Optional[QAction] = None

        self.client: Optional[TCPClient] = None

        self.device_widget_list = []

        self.interfaceNames = []
        self.availablePorts = []
        self.interface_config = {}
        self.binaryDMXFrameData = None
        self.interface_widgets: List[InterfaceWidget] = []

        self.universe_widgets: Dict[int, UniverseWidget] = {}

        uic.loadUi('GUI/windows/mainwindow.ui', self)

        self.setupDocks()
        self.setupCallbacks()

    #region Interactive UI
    def setupCallbacks(self):
        self.client_connect_button.clicked.connect(self.onConnectToClient)
        self.onConfigGotten.connect(self.createServerUI)
        self.onDMXSceneGotten.connect(self.setupDMXScene)

        self.add_interface_button.clicked.connect(self.onAddInterface)
        self.push_interface_configuration_button.clicked.connect(self.pushInterfaceConfiguration)

        self.actionDMXFrameBin.triggered.connect(self.exportDMXBin)
        self.action_import_DMXFrameBinary.triggered.connect(self.importDMXBin)

    def importDMXBin(self):
        path = ""
        path = QFileDialog.getOpenFileName(self, "Open DMX Frame", path,  "DMX Frame (*.dmxframe)")[0]

        universes = readDMXFrame(path)

        for universe in universes:
            if universe[0] in self.universe_widgets.keys():
                self.universe_widgets[universe[0]].setFrame(universe[1])

    def exportDMXBin(self):
        interfaceTuples = []
        for universe in self.universe_widgets:
            interfaceTuples.append((self.universe_widgets[universe].universe,
                                   self.universe_widgets[universe].getFrame()))

        path = ""

        path = QFileDialog.getSaveFileName(self, "Save DMX Frame", path,  "DMX Frame (*.dmxframe)")[0]
        if path == "":
            return
        try:
            writeDMXFrame(path, interfaceTuples)
        except Exception as ex:
            logger.exception(ex)

    def pushInterfaceConfiguration(self):
        config = []
        for widget in self.interface_widgets:
            config.append(widget.getConfiguration())

        content = json.dumps(config, indent=2, sort_keys=True).encode("utf-8")
        self.client.sendMessage(clientprotocol.createGetSet(datatools.messageID(),
                                                            clientprotocol.GET_INTERFACE_CONFIGURATION, content))
        self.interface_config = config

        self.onConfigGotten.emit()

    def onAddInterface(self, checked=False):
        if self.client is None:
            return
        try:
            self.addInterfaceWidget(0, "", self.interfaceNames[0])
        except Exception as ex:
            logger.exception(ex)


    def onConnectToClient(self):
        if self.client is None:
            address = self.connection_address.text()
            port = self.connection_port.value()
            username = self.connection_username.text()
            password = self.connection_password.text()

            self.client_connect_button.setText("Disconnect")

            self.client = TCPClient(address=address, port=port, username=username, password=password)
            self.client.setTimeout(2)
            self.client.start()

            sleep(1)

            try:
                self.setupUniverseWidgets()
                self.setupDeviceWidgets()
            except Exception as ex:
                logger.exception(ex)

            logger.info("Client Connected")

        else:
            self.client_connect_button.setText("Connect")
            self.client.requestStop()
            self.client = None
            self.clearDeviceWidgets()
            self.clearUniverseWidgets()

            logger.info("Client Disconnected")

    def clearDeviceWidgets(self):
        for widget in self.device_widget_list:
            self.device_list.layout().removeWidget(widget)
            widget.onCloseRequest()
        self.device_widget_list.clear()
        device_manager.clearDMXDevices()

    def setupDeviceWidgets(self):
        self.client.sendMessage(clientprotocol.createGet(datatools.messageID(),
                                                         clientprotocol.GET_CURRENT_DMX_SCENE, self.parseDMXScene))

    def parseDMXScene(self, client, value):
        dmxscene = json.loads(value)
        device_manager.fromDict(dmxscene)

    def setupDMXScene(self):
        for device in device_manager.getDMXDevices():
            self.addDMXWidget(device)

        #self.device_list.layout().addWidget(Spacer())

    def addDMXWidget(self, device: DMXDevice):
        box = CollapsibleBox(title="{} [Universe {}, Channel {}]".format(device.name, device.universe,
                                                                             device.baseChannel+1), hasCloseButton=False)
        widget = DMXDeviceWidget(device)
        layout = QVBoxLayout()
        layout.addWidget(widget)
        box.setContentLayout(layout)
        self.device_list.layout().addWidget(box, alignment=Qt.AlignTop)

        self.device_widget_list.append(box)


    def clearUniverseWidgets(self):
        self.universetabwidget.clear()
        for widget in self.interface_widgets:
            widget.removeWidget()

        for widget in self.interface_widgets:
            widget.removeWidget()

    def setupUniverseWidgets(self):
        self.client.sendMessage(clientprotocol.createGet(datatools.messageID(),
                                                         clientprotocol.GET_INTERFACE_NAMES, self.parseInterfaceList))

    def parseInterfaceList(self, client, value):
        logger.info("Parsing Interface list....")
        self.interfaceNames = getStringList(value)
        logger.info(self.interfaceNames)
        self.client.sendMessage(clientprotocol.createGet(datatools.messageID(),
                                                         clientprotocol.GET_AVAILABLE_PORTS,
                                                         self.parsePortList))

    def parsePortList(self, client, value):
        self.availablePorts = getStringList(value)
        self.client.sendMessage(clientprotocol.createGet(datatools.messageID(),
                                                         clientprotocol.GET_INTERFACE_CONFIGURATION,
                                                         self.parseInterfaceConfiguration))

    def parseInterfaceConfiguration(self, client, value: bytes):
        self.interface_config = json.loads(value.decode("utf-8"))
        self.client.sendMessage(clientprotocol.createGet(datatools.messageID(),
                                                         clientprotocol.GET_CURRENT_DMX_FRAME,
                                                         self.getDMXData))

    def getDMXData(self, client, value: bytes):
        self.binaryDMXFrameData = value
        self.onConfigGotten.emit()

    def parseDMXBinaryData(self, content):
        universeCount = getInt(content, 0)
        results = {}

        position = 4
        for i in range(universeCount):
            universe = getInt(content, position)
            position += 4
            universeLength = getInt(content, position)
            position += 4
            data = content[position: position + universeLength]
            position += universeLength
            results[universe] = data

        return results

    def createServerUI(self):
        self.clearUniverseWidgets()
        try:
            dmx_buffer = self.parseDMXBinaryData(self.binaryDMXFrameData)
            for interface in self.interface_config:
                universe = interface[CONFIG_KEY_DMX_INTERFACE_UNIVERSE]
                port = interface[CONFIG_KEY_DMX_INTERFACE_PORT]
                device = interface[CONFIG_KEY_DMX_INTERFACE_TYPE]

                vendor_id = interface[CONFIG_KEY_DMX_INTERFACE_USB_VENDOR_ID]
                product_id = interface[CONFIG_KEY_DMX_INTERFACE_USB_PRODUCT_ID]
                bus = interface[CONFIG_KEY_DMX_INTERFACE_USB_BUS]
                address = interface[CONFIG_KEY_DMX_INTERFACE_USB_ADDRESS]

                frame = [0]*512
                if universe in dmx_buffer:
                    frame = dmx_buffer[universe]

                uniWidget = UniverseWidget(universe, frame)
                uniWidget.client = self.client

                self.universe_widgets[universe] = uniWidget

                self.universetabwidget.addTab(uniWidget,
                                              "Universe {}".format(universe))

                self.addInterfaceWidget(universe, port, device, vendor_id, product_id, bus, address)
        except Exception as ex:
            logger.exception(ex)

        self.onDMXSceneGotten.emit()
    #endregion

    def addInterfaceWidget(self, universe, port, device, vendor_id, product_id, bus, address):
        interWidget = InterfaceWidget(universe, port, device, self.interfaceNames, self.availablePorts, vendor_id,
                                      product_id, bus, address, self.removeInterfacewidgetFromList)
        self.interface_widgets.append(interWidget)
        self.interface_container.layout().addWidget(interWidget)

    def removeInterfacewidgetFromList(self, widget):
        self.interface_widgets.remove(widget)

    #region Docks

    def setupDocks(self):
        self.setCorner(Qt.Corner.BottomRightCorner, Qt.DockWidgetArea.RightDockWidgetArea)
        self.setCorner(Qt.Corner.TopRightCorner, Qt.DockWidgetArea.RightDockWidgetArea)

        self.setCorner(Qt.Corner.BottomLeftCorner, Qt.DockWidgetArea.LeftDockWidgetArea)
        self.setCorner(Qt.Corner.TopLeftCorner, Qt.DockWidgetArea.LeftDockWidgetArea)

    #endregion
