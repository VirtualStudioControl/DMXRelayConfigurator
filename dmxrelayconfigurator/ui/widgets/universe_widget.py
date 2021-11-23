from typing import Optional

from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget

from dmxrelayconfigurator.dmx import frame_manager, device_manager
from dmxrelayconfigurator.interfaces.IFrameProvider import IFrameProvider
from dmxrelayconfigurator.logging import logengine
from dmxrelayconfigurator.net.tcpclient import TCPClient
from dmxrelayconfigurator.net import clientprotocol as proto
from dmxrelayconfigurator.ui.widgets.channel_widget import ChannelWidget


logger = logengine.getLogger()


class UniverseWidget(QWidget, IFrameProvider):

    def __init__(self, universe: int, frameData = None, parent=None):
        super().__init__(parent)

        self.UPDATE_DELAY_MS = 10

        self.universe = universe
        self._client: Optional[TCPClient] = None

        self.scrollAreaWidgetContents: Optional[QWidget] = None

        uic.loadUi('GUI/widgets/universewidget.ui', self)

        self.channelWidgets = []

        self.frameUpdateTimer = QTimer()
        self.frameUpdateTimer.timeout.connect(self.onFrameUpdateTimer)
        self.frameUpdateTimer.setSingleShot(True)

        for i in range(512):
            value = 0
            if frameData is not None:
                value = frameData[i]
            widget = ChannelWidget(label="Channel {}".format(i+1), value=value, channel=i, valueChanged=self.updateFrame)
            self.channelWidgets.append(widget)
            self.scrollAreaWidgetContents.layout().addWidget(widget)

        if frameData is not None:
            self.setFrame(frameData)
        frame_manager.registerFrameProvider(self.universe, self)

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

    def setChannel(self, channel, value):
        self.channelWidgets[channel].value = value

    def setChannelSilent(self, channel, value):
        self.channelWidgets[channel].setValueSilent(value)

    def getChannel(self, channel):
        return self.channelWidgets[channel].value

    def updateFrame(self):
        self.frameUpdateTimer.start(self.UPDATE_DELAY_MS)

    def onFrameUpdateTimer(self):
        dmxFrame = [0]*512
        for widget in self.channelWidgets:
            dmxFrame[widget.channel] = widget.value

        if self._client is not None and self._client.isConnected:
            self._client.sendMessage(proto.createDMXMessage(False, self.universe, dmxFrame))

        device_manager.updateDMXDevices()