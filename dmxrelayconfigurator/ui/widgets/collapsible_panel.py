from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class CollapsibleBox(QWidget):

    onClose = pyqtSignal()
    isInitialised = False
    contentSet = False

    def __init__(self, parent=None, title="Collapsible Panel", hasCloseButton=False):
        super(CollapsibleBox, self).__init__(parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.toggle_animation = QParallelAnimationGroup(self)
        self.resize_animation = QParallelAnimationGroup(self)

        self.headder_widget = CollapsibleTitleWidget(toggle_animation=self.toggle_animation, title=title, hasCloseButton=hasCloseButton, closeFunction=self.onCloseRequest)

        self.content_area = QScrollArea(
            maximumHeight=0, minimumHeight=0
        )
        self.content_area.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        self.content_area.setFrameShape(QFrame.NoFrame)

       # titleLayout = QHBoxLayout(self)

        #titleLayout.setSpacing(0)
        #titleLayout.setContentsMargins(0, 0, 0, 0)

        #titleLayout.addWidget(self.toggle_button)
        #if self.hasCloseButton:
        #    titleLayout.addWidget(self.close_button)

        lay = QVBoxLayout()
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.headder_widget)

        lay.addWidget(self.content_area)

        super().setLayout(lay)

        self.toggle_animation.addAnimation(
            QPropertyAnimation(self, b"minimumHeight")
        )
        self.toggle_animation.addAnimation(
            QPropertyAnimation(self, b"maximumHeight")
        )
        self.toggle_animation.addAnimation(
            QPropertyAnimation(self.content_area, b"maximumHeight")
        )

        self.resize_animation.addAnimation(
            QPropertyAnimation(self, b"minimumHeight")
        )
        self.resize_animation.addAnimation(
            QPropertyAnimation(self, b"maximumHeight")
        )
        self.resize_animation.addAnimation(
            QPropertyAnimation(self.content_area, b"maximumHeight")
        )

        self.isInitialised = True

    def onCloseRequest(self):
        self.onClose.emit()
        self.deleteLater()

    def setTitle(self, title=""):
        self.headder_widget.toggle_button.setText(title)

    def setLayout(self, a0: 'QLayout') -> None:
        if self.isInitialised:
            self.setContentLayout(a0)
        else:
            super(CollapsibleBox, self).setLayout(a0)

    def layout(self) -> 'QLayout':
        return self.content_area.layout()

    def resizeCollapsibleBoxHeight(self, delta):
        if not self.contentSet:
            return

        newContentHeight = self.content_height + delta

        for i in range(self.resize_animation.animationCount()):
            animation = self.resize_animation.animationAt(i)
            animation.setDuration(1)
            animation.setStartValue(self.collapsed_height + self.content_height)
            animation.setEndValue(self.collapsed_height + newContentHeight)

        content_animation = self.resize_animation.animationAt(
            self.toggle_animation.animationCount() - 1
        )
        content_animation.setDuration(1)
        content_animation.setStartValue(self.content_height)
        content_animation.setEndValue(newContentHeight)

        for i in range(self.toggle_animation.animationCount()):
            animation = self.toggle_animation.animationAt(i)
            animation.setDuration(500)
            animation.setStartValue(self.collapsed_height)
            animation.setEndValue(self.collapsed_height + newContentHeight)

        content_animation = self.toggle_animation.animationAt(
            self.toggle_animation.animationCount() - 1
        )
        content_animation.setDuration(500)
        content_animation.setStartValue(0)
        content_animation.setEndValue(newContentHeight)

        self.content_height = newContentHeight

        self.resize_animation.start()

    def setContentLayout(self, layout):
        lay = self.content_area.layout()
        del lay
        self.content_area.setLayout(layout)
        self.collapsed_height = (
            self.sizeHint().height() - self.content_area.maximumHeight()
            #
        )
        self.content_height = layout.sizeHint().height()

        for i in range(self.toggle_animation.animationCount()):
            animation = self.toggle_animation.animationAt(i)
            animation.setDuration(500)
            animation.setStartValue(self.collapsed_height)
            animation.setEndValue(self.collapsed_height + self.content_height)

        content_animation = self.toggle_animation.animationAt(
            self.toggle_animation.animationCount() - 1
        )
        content_animation.setDuration(500)
        content_animation.setStartValue(0)
        content_animation.setEndValue(self.content_height)

        self.contentSet = True

class CollapsibleTitleWidget(QWidget):
    def __init__(self, toggle_animation, title="", hasCloseButton=False, closeFunction=None):
        super().__init__()
        self.toggle_animation = toggle_animation

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.hasCloseButton = hasCloseButton
        self.toggle_button = QToolButton(
            text=title, checkable=True, checked=False
        )
        self.toggle_button.setStyleSheet("QToolButton { border: none; }")
        self.toggle_button.setToolButtonStyle(
            Qt.ToolButtonTextBesideIcon
        )
        self.toggle_button.setArrowType(Qt.RightArrow)
        self.toggle_button.pressed.connect(self.on_pressed)

        self.toggle_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.toggle_button)
        if hasCloseButton:
            self.close_button = QToolButton(text="X")
            self.close_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.close_button.clicked.connect(closeFunction)
            layout.addWidget(self.close_button)

        self.setLayout(layout)

    @pyqtSlot()
    def on_pressed(self):
        checked = self.toggle_button.isChecked()
        self.toggle_button.setArrowType(
            Qt.DownArrow if not checked else Qt.RightArrow
        )
        self.toggle_animation.setDirection(
            QAbstractAnimation.Forward
            if not checked
            else QAbstractAnimation.Backward
        )
        self.toggle_animation.start()