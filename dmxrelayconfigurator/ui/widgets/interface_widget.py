from typing import Optional

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QSpinBox, QComboBox, QToolButton, QStackedWidget

CONFIG_KEY_DMX_INTERFACE_PORT = "port"

CONFIG_KEY_DMX_INTERFACE_USB_VENDOR_ID = "usb_vendor_id"
CONFIG_KEY_DMX_INTERFACE_USB_PRODUCT_ID = "usb_product_id"
CONFIG_KEY_DMX_INTERFACE_USB_BUS = "usb_bus"
CONFIG_KEY_DMX_INTERFACE_USB_ADDRESS = "usb_address"

CONFIG_KEY_DMX_INTERFACE_TYPE = "type"
CONFIG_KEY_DMX_INTERFACE_UNIVERSE = "universe"


USB_INTERFACE_NAMES = ["UDMX"]


class InterfaceWidget(QWidget):

    def __init__(self, universe, port, interface, interfaces_available, ports_available, vendor_id, product_id,
                 bus, address, destructor, parent=None):
        super().__init__(parent)

        self.universe_spin: Optional[QSpinBox] = None

        self.optionStack: Optional[QStackedWidget] = None

        self.port_combo: Optional[QComboBox] = None
        self.interface_combo: Optional[QComboBox] = None

        self.vendor_id_spin: Optional[QSpinBox] = None
        self.product_id_spin: Optional[QSpinBox] = None
        self.bus_spin: Optional[QSpinBox] = None
        self.address_spin: Optional[QSpinBox] = None

        self.close_btn: Optional[QToolButton] = None

        uic.loadUi('GUI/widgets/interface.ui', self)

        self.universe_spin.setValue(universe)
        self.port_combo.addItems(ports_available)
        if port not in ports_available:
            self.port_combo.addItem(port)
        self.port_combo.setCurrentText(port)

        self.interface_combo.addItems(interfaces_available)

        self.interface_combo.setCurrentText(interface)

        self.vendor_id_spin.setValue(vendor_id)
        self.product_id_spin.setValue(product_id)
        self.bus_spin.setValue(bus)
        self.address_spin.setValue(address)

        if interface in USB_INTERFACE_NAMES:
            # Interface needs USB Params
            self.optionStack.setCurrentIndex(1)
        else:
            # Interface needs Serial Params
            self.optionStack.setCurrentIndex(0)

        self.destructor = destructor

        self.setupCallbacks()

    def setupCallbacks(self):
        self.close_btn.clicked.connect(self.removeWidget)
        self.interface_combo.currentIndexChanged.connect(self.updateStack)

    def updateStack(self):
        if self.interface_combo.currentText() in USB_INTERFACE_NAMES:
            # Interface needs USB Params
            self.optionStack.setCurrentIndex(1)
        else:
            # Interface needs Serial Params
            self.optionStack.setCurrentIndex(0)

    def removeWidget(self, checked=False):
        self.parent().layout().removeWidget(self)
        self.destructor(self)

    def getConfiguration(self):
        return {
            CONFIG_KEY_DMX_INTERFACE_UNIVERSE: self.universe_spin.value(),
            CONFIG_KEY_DMX_INTERFACE_PORT: self.port_combo.currentText(),
            CONFIG_KEY_DMX_INTERFACE_TYPE: self.interface_combo.currentText(),

            CONFIG_KEY_DMX_INTERFACE_USB_VENDOR_ID: self.vendor_id_spin.value(),
            CONFIG_KEY_DMX_INTERFACE_USB_PRODUCT_ID: self.product_id_spin.value(),
            CONFIG_KEY_DMX_INTERFACE_USB_BUS: self.bus_spin.value(),
            CONFIG_KEY_DMX_INTERFACE_USB_ADDRESS: self.address_spin.value()
        }