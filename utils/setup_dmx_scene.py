from dmxrelayconfigurator.dmx import device_manager
from dmxrelayconfigurator.dmx.dmxdevice import *
from dmxrelayconfigurator.io.filetools import writeJSON

UNIVERSE = 1

if __name__ == "__main__":
    device_manager.addDMXDevice(DMXDevice(universe=UNIVERSE, baseChannel=0, channelCount=3,
                    name="Große Leuchte", devtype="Generic RGB",
                    channelTypes=[CHANNEL_TYPE_RED, CHANNEL_TYPE_GREEN, CHANNEL_TYPE_BLUE],
                    constantChannels={}))


    device_manager.addDMXDevice(DMXDevice(universe=UNIVERSE, baseChannel=30, channelCount=4,
                    name="UKing", devtype="Generic Dimmed RGB",
                    channelTypes=[CHANNEL_TYPE_DIMMER, CHANNEL_TYPE_RED, CHANNEL_TYPE_GREEN, CHANNEL_TYPE_BLUE],
                    constantChannels={CHANNEL_TYPE_DIMMER: 0xff}))

    device_manager.addDMXDevice(DMXDevice(universe=UNIVERSE, baseChannel=90, channelCount=14,
                                          name="MovingHead", devtype="Generic RGBW Moving Head",
                                          channelTypes=[CHANNEL_TYPE_PAN, CHANNEL_TYPE_PAN_FINE, CHANNEL_TYPE_TILT,
                                                        CHANNEL_TYPE_TILT_FINE, CHANNEL_TYPE_XYSPEED,
                                                        CHANNEL_TYPE_DIMMER, CHANNEL_TYPE_RED, CHANNEL_TYPE_GREEN,
                                                        CHANNEL_TYPE_BLUE, CHANNEL_TYPE_WHITE, CHANNEL_TYPE_COLOR_MODE,
                                                        CHANNEL_TYPE_COLOR_JUMP_SPEED, CHANNEL_TYPE_CUSTOM,
                                                        CHANNEL_TYPE_RESET],
                                          constantChannels={CHANNEL_TYPE_DIMMER: 0xff,
                                                            CHANNEL_TYPE_COLOR_MODE: 0x00,
                                                            CHANNEL_TYPE_CUSTOM: 0x00,
                                                            CHANNEL_TYPE_RESET: 0x00}))

    writeJSON("dmxscene.json", device_manager.toDict())