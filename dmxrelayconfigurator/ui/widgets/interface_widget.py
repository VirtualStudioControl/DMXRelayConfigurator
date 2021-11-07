from typing import Optional

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QSpinBox, QComboBox, QToolButton

CONFIG_KEY_DMX_INTERFACE_PORT = "port"
CONFIG_KEY_DMX_INTERFACE_TYPE = "type"
CONFIG_KEY_DMX_INTERFACE_UNIVERSE = "universe"

class InterfaceWidget(QWidget):

    def __init__(self, universe, port, interface, interfaces_available, ports_available, destructor, parent=None):
        super().__init__(parent)

        self.universe_spin: Optional[QSpinBox] = None
        self.port_combo: Optional[QComboBox] = None
        self.interface_combo: Optional[QComboBox] = None

        self.close_btn: Optional[QToolButton] = None

        uic.loadUi('GUI/widgets/interface.ui', self)

        self.universe_spin.setValue(universe)
        self.port_combo.addItems(ports_available)
        if port not in ports_available:
            self.port_combo.addItem(port)
        self.port_combo.setCurrentText(port)

        self.interface_combo.addItems(interfaces_available)
        self.interface_combo.setCurrentText(interface)

        self.destructor = destructor

        self.setupCallbacks()

    def setupCallbacks(self):
        self.close_btn.clicked.connect(self.removeWidget)

    def removeWidget(self, checked=False):
        self.parent().layout().removeWidget(self)
        self.destructor(self)

    def getConfiguration(self):
        return {
            CONFIG_KEY_DMX_INTERFACE_UNIVERSE: self.universe_spin.value(),
            CONFIG_KEY_DMX_INTERFACE_PORT: self.port_combo.currentText(),
            CONFIG_KEY_DMX_INTERFACE_TYPE: self.interface_combo.currentText(),
        }