from typing import Dict

from dmxrelayconfigurator.interfaces.IFrameProvider import IFrameProvider

FRAME_PROVIDERS: Dict[int, IFrameProvider] = {}


def registerFrameProvider(universe, frame: IFrameProvider):
    FRAME_PROVIDERS[universe] = frame


def unregisterFrameProvider(universe, frame: IFrameProvider):
    if universe in FRAME_PROVIDERS:
        del FRAME_PROVIDERS[universe]


def getFrameProvider(universe) -> IFrameProvider:
    if universe in FRAME_PROVIDERS:
        return FRAME_PROVIDERS[universe]
    return IFrameProvider()