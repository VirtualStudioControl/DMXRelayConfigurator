from typing import Optional, Callable

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QWidget, QLabel, QHBoxLayout

from dmxrelayconfigurator.dmx.dmxdevice import DMXDevice
from dmxrelayconfigurator.logging import logengine
from dmxrelayconfigurator.ui.widgets.channel_widget import ChannelWidget
from dmxrelayconfigurator.ui.widgets.collapsible_panel import CollapsibleBox
from dmxrelayconfigurator.ui.widgets.dmx_color_chooser import DMXColorChooserWidget

logger = logengine.getLogger()


class DMXDeviceWidget(QWidget):

    def __init__(self, device: DMXDevice, parent=None):
        super().__init__(parent=parent)
        self.device = device

        uic.loadUi('GUI/widgets/dmx_device_widget.ui', self)

        self.label_name.setText(device.name)
        self.label_type.setText(device.deviceType)
        self.label_universe.setText("{}".format(device.universe))
        self.label_basechannel.setText("{}".format(device.baseChannel+1))

        self.panWidget = None
        self.tiltWidget = None
        self.speedWidget = None

        if device.hasColor():
            self.setupColorWidget()

        if device.hasPan():
            self.panWidget = self.setupRotationWidget("Pan", 0xffff, valueChanged=self.setDevicePan)

        if device.hasTilt():
            self.tiltWidget = self.setupRotationWidget("Tilt", 0xffff, False, valueChanged=self.setDeviceTilt)

        if device.hasSpeed():
            self.speedWidget = self.setupRotationWidget("Speed", 0xff, valueChanged=self.setDeviceSpeed)

    def setupRotationWidget(self, title, maximum, seperator=True, valueChanged: Optional[Callable[[], None]] = None):
        widget = ChannelWidget(label=title, seperator=seperator, valueChanged=valueChanged)
        widget.setMaximumValue(maximum)
        self.param_widget.layout().addWidget(widget, alignment=Qt.AlignTop)
        return widget

    def setupColorWidget(self):
        widget = DMXColorChooserWidget(self.device)
        widget.connect(self.setDeviceColor)
        self.param_widget.layout().addWidget(widget, alignment=Qt.AlignTop)

    def setDevicePan(self):
        if self.panWidget is not None:
            self.device.setPan(self.panWidget.value)

    def setDeviceTilt(self):
        if self.tiltWidget is not None:
            self.device.setTilt(self.tiltWidget.value)

    def setDeviceSpeed(self):
        if self.speedWidget is not None:
            self.device.setPanTiltSpeed(self.speedWidget.value)

    def setDeviceColor(self, color: QColor = Qt.red):
        logger.info("{}".format(self.device))
        self.device.setColorRGB(color.red(), color.green(), color.blue())
