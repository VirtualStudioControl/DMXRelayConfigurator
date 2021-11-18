from typing import Callable, Optional, Union

from PyQt5 import uic
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget

from dmxrelayconfigurator.dmx.dmxdevice import DMXDevice
from dmxrelayconfigurator.logging import logengine
from dmxrelayconfigurator.ui.widgets.color_selection_button import ColorSelectionButton

logging = logengine.getLogger()


class DMXColorChooserWidget(QWidget):

    def __init__(self, device: DMXDevice, parent=None):
        super().__init__(parent=parent)
        self.device = device

        self.color_chooser: Optional[ColorSelectionButton] = None

        uic.loadUi('GUI/widgets/dmx_color_chooser.ui', self)

    def connect(self, func: Callable[[QColor], None]):
        self.color_chooser.colorChanged.connect(func)

    def setColor(self, color: QColor):
        logging.info("Set Color")
        try:
            self.color_chooser.setColor(color)
        except Exception as ex:
            logging.exception(ex)

