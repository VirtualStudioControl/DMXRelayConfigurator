from dmxrelayconfigurator.dmx.dmxdevice import *

def addRGBLight(device_manager, name, baseaddress, universe):
    dev = DMXDevice(universe=universe, baseChannel=baseaddress, channelCount=3,
                    name=name, devtype="Spot",
                    channelTypes=[CHANNEL_TYPE_RED,
                                  CHANNEL_TYPE_GREEN,
                                  CHANNEL_TYPE_BLUE],
                    constantChannels={},
                    dimmerRange=[0, 1, 254, 255])
    device_manager.addDMXDevice(dev)
    return dev

def addRGBBar(device_manager, name, baseaddress, universe):
    nodes = []
    for i in range(8):
        nodes.append(addRGBLight("{}, element {}".format(name, i), baseaddress + 3*i, universe))

    dev = DMXDevice(universe=-1, baseChannel=0, channelCount=3,
                    name=name, devtype="RGB Bar",
                    channelTypes=[CHANNEL_TYPE_RED, CHANNEL_TYPE_GREEN,
                                  CHANNEL_TYPE_BLUE],
                    constantChannels={})

    for d in nodes:
        d.setParent(dev)

    device_manager.addDMXDevice(dev)
    return dev

#region Device Creators
def addBIG(device_manager, name, baseaddress, universe):
    dev = DMXDevice(universe=universe, baseChannel=baseaddress, channelCount=8,
                                          name=name, devtype="Big Deeper Sleeka S60 Slim",
                                          channelTypes=[CHANNEL_TYPE_RED, CHANNEL_TYPE_GREEN, CHANNEL_TYPE_BLUE,
                                                        CHANNEL_TYPE_STROBO,
                                                        CHANNEL_TYPE_COLOR_MODE, CHANNEL_TYPE_COLOR_JUMP_SPEED,
                                                        CHANNEL_TYPE_UNKNOWN, CHANNEL_TYPE_UNKNOWN],
                                          constantChannels={CHANNEL_TYPE_COLOR_MODE: 0x00})
    device_manager.addDMXDevice(dev)
    return dev

def addUKing(device_manager, name, baseaddress, universe):
    dev = DMXDevice(universe=universe, baseChannel=baseaddress, channelCount=7,
                                          name=name, devtype="UKing ZQ-B53B",
                                          channelTypes=[CHANNEL_TYPE_DIMMER, CHANNEL_TYPE_RED, CHANNEL_TYPE_GREEN,
                                                        CHANNEL_TYPE_BLUE,
                                                        CHANNEL_TYPE_STROBO, CHANNEL_TYPE_COLOR_MODE,
                                                        CHANNEL_TYPE_COLOR_JUMP_SPEED],
                                          constantChannels={CHANNEL_TYPE_COLOR_MODE: 0x00},
                                          dimmerRange = [0, 1, 254, 255]
    )
    device_manager.addDMXDevice(dev)
    return dev

def addMovingHead(device_manager, name, baseaddress, universe):
    dev = DMXDevice(universe=universe, baseChannel=baseaddress, channelCount=14,
                                          name=name, devtype="Lixada RGBW Moving Head",
                                          channelTypes=[CHANNEL_TYPE_PAN, CHANNEL_TYPE_PAN_FINE, CHANNEL_TYPE_TILT,
                                                        CHANNEL_TYPE_TILT_FINE, CHANNEL_TYPE_XYSPEED,
                                                        CHANNEL_TYPE_DIMMER, CHANNEL_TYPE_RED, CHANNEL_TYPE_GREEN,
                                                        CHANNEL_TYPE_BLUE, CHANNEL_TYPE_WHITE, CHANNEL_TYPE_COLOR_MODE,
                                                        CHANNEL_TYPE_COLOR_JUMP_SPEED, CHANNEL_TYPE_CUSTOM,
                                                        CHANNEL_TYPE_RESET],
                                          constantChannels={CHANNEL_TYPE_COLOR_MODE: 0x00,
                                                            CHANNEL_TYPE_CUSTOM: 0x00,
                                                            CHANNEL_TYPE_RESET: 0x00},
                                          dimmerRange = [0, 8, 134, 255])
    device_manager.addDMXDevice(dev)
    return dev








def addRGBLight(device_manager, name, baseaddress, universe):
    dev = DMXDevice(universe=universe, baseChannel=baseaddress, channelCount=3,
                    name=name, devtype="Spot",
                    channelTypes=[CHANNEL_TYPE_RED,
                                  CHANNEL_TYPE_GREEN,
                                  CHANNEL_TYPE_BLUE],
                    constantChannels={},
                    dimmerRange=[0, 1, 254, 255])
    device_manager.addDMXDevice(dev)
    return dev

def addRGBBar(device_manager, name, baseaddress, universe):
    nodes = []
    for i in range(8):
        nodes.append(addRGBLight("{}, element {}".format(name, i), baseaddress + 3*i, universe))

    dev = DMXDevice(universe=-1, baseChannel=0, channelCount=3,
                    name=name, devtype="RGB Bar",
                    channelTypes=[CHANNEL_TYPE_RED, CHANNEL_TYPE_GREEN,
                                  CHANNEL_TYPE_BLUE],
                    constantChannels={})

    for d in nodes:
        d.setParent(dev)

    device_manager.addDMXDevice(dev)
    return dev

def addSpot(device_manager, name, baseaddress, universe):
    dev = DMXDevice(universe=universe, baseChannel=baseaddress, channelCount=14,
                    name=name, devtype="Spot",
                    channelTypes=[CHANNEL_TYPE_DIMMER,
                                  CHANNEL_TYPE_RED,
                                  CHANNEL_TYPE_GREEN,
                                  CHANNEL_TYPE_BLUE,
                                  CHANNEL_TYPE_WHITE,
                                  CHANNEL_TYPE_COLOR_MODE],
                    constantChannels={CHANNEL_TYPE_COLOR_MODE: 0},
                    dimmerRange=[0, 8, 134, 255])
    device_manager.addDMXDevice(dev)
    return dev

def addMini(device_manager, name, baseaddress, universe):
    dev = DMXDevice(universe=universe, baseChannel=baseaddress, channelCount=14,
                    name=name, devtype="Mini",
                    channelTypes=[CHANNEL_TYPE_DIMMER,
                                  CHANNEL_TYPE_RED,
                                  CHANNEL_TYPE_GREEN,
                                  CHANNEL_TYPE_BLUE,
                                  CHANNEL_TYPE_WHITE,
                                  CHANNEL_TYPE_COLOR_MODE,
                                  CHANNEL_TYPE_COLOR_JUMP_SPEED],
                    constantChannels={CHANNEL_TYPE_COLOR_MODE: 0},
                    dimmerRange=[0, 1, 254, 255])
    device_manager.addDMXDevice(dev)
    return dev

#endregion