from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QColorDialog, QPushButton


MAGIC_VALUE_HEX = "#hex"

class ColorSelectionButton(QPushButton):

    colorChanged = pyqtSignal(QColor)

    def __init__(self, parent=None, color: QColor=None):
        super(ColorSelectionButton, self).__init__(parent)
        self.color = color
        if color is None:
            self.color = QColor("#ffffff")
        self.displayColorName = False
        self.setColor(self.color)
        self.clicked.connect(self.onColorChanged)

    def setText(self, text: str) -> None:
        if text == MAGIC_VALUE_HEX:
            self.displayColorName = True
            super().setText(self.color.name())
        else:
            self.displayColorName = False
            super().setText(text)

    def setColor(self, color: QColor):

        lum = 0.3 * color.redF() + 0.59 * color.greenF() + 0.11 * color.blueF()

        if lum > 0.5:
            self.setStyleSheet("color: #000000; background-color: {}; border: 1px solid; border-radius: 4px;".format(color.name()))
        else:
            self.setStyleSheet("color: #ffffff; background-color: {}; border: 1px solid; border-radius: 4px;".format(color.name()))

        if self.displayColorName:
            super().setText(color.name())

        self.repaint()


    def onColorChanged(self, checked=False):
        color = QColorDialog.getColor(self.color, self.parent(), "Choose Color",
                              QColorDialog.ColorDialogOption.ShowAlphaChannel)
        if not color.isValid():
            return

        self.color = color
        self.setColor(color)
        self.colorChanged.emit(color)