from dmxrelayconfigurator.dmx.dmxdevice import *

def addETECRGBWAUvMovingHead(device_manager, name, baseaddress, universe):
    dev = DMXDevice(universe=universe, baseChannel=baseaddress, channelCount=16,
                    name=name, devtype="ETEC RGBWAUv Moving Head",
                    channelTypes=[CHANNEL_TYPE_PAN, CHANNEL_TYPE_PAN_FINE, CHANNEL_TYPE_TILT,
                                  CHANNEL_TYPE_TILT_FINE, CHANNEL_TYPE_XYSPEED,
                                  CHANNEL_TYPE_DIMMER, CHANNEL_TYPE_RED, CHANNEL_TYPE_GREEN,
                                  CHANNEL_TYPE_BLUE, CHANNEL_TYPE_WHITE, CHANNEL_TYPE_AMBER, CHANNEL_TYPE_UV,
                                  CHANNEL_TYPE_COLOR_MODE,
                                  CHANNEL_TYPE_COLOR_JUMP_SPEED, CHANNEL_TYPE_CUSTOM,
                                  CHANNEL_TYPE_RESET],
                    constantChannels={CHANNEL_TYPE_COLOR_MODE: 0x00,
                                      CHANNEL_TYPE_CUSTOM: 0x00,
                                      CHANNEL_TYPE_RESET: 0x00},
                    dimmerRange=[0, 8, 134, 255])
    device_manager.addDMXDevice(dev)
    return dev