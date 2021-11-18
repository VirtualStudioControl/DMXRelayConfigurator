from typing import Iterable


class IFrameProvider:

    def getFrame(self) -> Iterable[int]:
        return [0]*512

    def setFrame(self, frameData):
        pass

    def updateFrame(self):
        pass

    def setChannel(self, channel, value):
        pass

    def setChannelSilent(self, channel, value):
        pass

    def getChannel(self, channel) -> int:
        return 0