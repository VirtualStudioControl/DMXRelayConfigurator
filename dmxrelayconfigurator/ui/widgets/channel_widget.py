from typing import Optional, Callable

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QSpinBox

from dmxrelayconfigurator.logging import logengine

logger = logengine.getLogger()

class ChannelWidget(QWidget):

    def __init__(self, parent=None, channel: int = 0, label="", valueChanged: Callable[[], None] = None):
        super().__init__(parent)
        self.valueChanged = None
        self.channel: int = channel
        self._value = 0
        self.label: Optional[QLabel] = None

        self.slider: Optional[QSlider] = None
        self.spin: Optional[QSpinBox] = None

        uic.loadUi('GUI/widgets/channelwidget.ui', self)

        self.label.setText(label)

        self.setupCallbacks()
        self.spin.setValue(0)
        self.valueChanged = valueChanged

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self.spin.setValue(value)

    def setValueSilent(self, value):
        self._value = value
        self.spin.blockSignals(True)
        self.spin.setValue(value)
        self.spin.blockSignals(False)

        self.slider.blockSignals(True)
        self.slider.setValue(value)
        self.slider.blockSignals(False)

    def setupCallbacks(self):
        self.slider.valueChanged.connect(self.onSliderMoved)
        self.spin.valueChanged.connect(self.onSpinValueChanged)

    def onSpinValueChanged(self, newValue):
        self._value = newValue
        self.slider.blockSignals(True)
        self.slider.setValue(newValue)
        self.slider.blockSignals(False)

        try:
            if self.valueChanged is not None:
                self.valueChanged()
        except Exception as ex:
            logger.exception(ex)

    def onSliderMoved(self, newValue):
        self.spin.setValue(newValue)
