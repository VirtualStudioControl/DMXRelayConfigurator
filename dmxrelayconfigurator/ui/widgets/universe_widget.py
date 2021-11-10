from typing import Optional

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from dmxrelayconfigurator.logging import logengine
from dmxrelayconfigurator.net.tcpclient import TCPClient
from dmxrelayconfigurator.net import clientprotocol as proto
from dmxrelayconfigurator.ui.widgets.channel_widget import ChannelWidget


logger = logengine.getLogger()

class UniverseWidget(QWidget):

    def __init__(self, universe: int, parent=None):
        super().__init__(parent)

        self.universe = universe
        self._client: Optional[TCPClient] = None

        self.scrollAreaWidgetContents: Optional[QWidget] = None

        uic.loadUi('GUI/widgets/universewidget.ui', self)

        self.channelWidgets = []

        for i in range(512):
            widget = ChannelWidget(label="Channel {}".format(i+1), channel=i, valueChanged=self.updateFrame)
            self.channelWidgets.append(widget)
            self.scrollAreaWidgetContents.layout().addWidget(widget)

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, client):
        self._client = client
        self.updateFrame()

    def setFrameData(self, data):
        for widget in self.channelWidgets:
            widget.setValueSilent(data[widget.channel])
        self.updateFrame()

    def getFrame(self):
        dmxFrame = [0] * 512
        for widget in self.channelWidgets:
            dmxFrame[widget.channel] = widget.value
        return dmxFrame

    def setFrame(self, frameData):
        for widget in self.channelWidgets:
            widget.setValueSilent(frameData[widget.channel])
        self.updateFrame()

    def updateFrame(self):
        dmxFrame = [0]*512
        for widget in self.channelWidgets:
            dmxFrame[widget.channel] = widget.value

        if self._client is not None and self._client.isConnected:
            self._client.sendMessage(proto.createDMXMessage(False, self.universe, dmxFrame))