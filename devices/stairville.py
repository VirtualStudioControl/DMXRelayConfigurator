from dmxrelayconfigurator.dmx.dmxdevice import *

def __addXBrickHexSegment(device_manager, name, baseaddress, universe):
    dev = DMXDevice(universe=universe, baseChannel=baseaddress, channelCount=6,
                    name=name, devtype="Spot",
                    channelTypes=[CHANNEL_TYPE_RED,
                                  CHANNEL_TYPE_GREEN,
                                  CHANNEL_TYPE_BLUE,
                                  CHANNEL_TYPE_WHITE,
                                  CHANNEL_TYPE_AMBER,
                                  CHANNEL_TYPE_UV],
                    constantChannels={},
                    dimmerRange=[0, 1, 254, 255])
    device_manager.addDMXDevice(dev)
    return dev

def addStairvilleXBrickHex(device_manager, name, baseaddress, universe):
    nodes = []
    for i in range(4):
        nodes.append(__addXBrickHexSegment(device_manager, "{}, Segment {}".format(name, i), baseaddress + 1 + 6 * i, universe))

    dev = DMXDevice(universe=universe, baseChannel=baseaddress, channelCount=28,
                    name=name, devtype="RGBAWUv Bar",
                    channelTypes=[CHANNEL_TYPE_DIMMER,
                                  CHANNEL_TYPE_RED,
                                  CHANNEL_TYPE_GREEN,
                                  CHANNEL_TYPE_BLUE,
                                  CHANNEL_TYPE_WHITE,
                                  CHANNEL_TYPE_AMBER,
                                  CHANNEL_TYPE_UV,
                                  CHANNEL_TYPE_CUSTOM,
                                  CHANNEL_TYPE_CUSTOM,
                                  CHANNEL_TYPE_CUSTOM,
                                  CHANNEL_TYPE_CUSTOM,
                                  CHANNEL_TYPE_CUSTOM,
                                  CHANNEL_TYPE_CUSTOM,
                                  CHANNEL_TYPE_CUSTOM,
                                  CHANNEL_TYPE_CUSTOM,
                                  CHANNEL_TYPE_CUSTOM,
                                  CHANNEL_TYPE_CUSTOM,
                                  CHANNEL_TYPE_CUSTOM,
                                  CHANNEL_TYPE_CUSTOM,
                                  CHANNEL_TYPE_CUSTOM,
                                  CHANNEL_TYPE_CUSTOM,
                                  CHANNEL_TYPE_CUSTOM,
                                  CHANNEL_TYPE_CUSTOM,
                                  CHANNEL_TYPE_CUSTOM,
                                  CHANNEL_TYPE_CUSTOM,
                                  CHANNEL_TYPE_PROGRAM,
                                  CHANNEL_TYPE_CUSTOM,
                                  CHANNEL_TYPE_STROBO],
                    constantChannels={})

    for d in nodes:
        d.setParent(dev)

    device_manager.addDMXDevice(dev)
    return dev

def __addRGBBarSegment(device_manager, name, baseaddress, universe):
    dev = DMXDevice(universe=universe, baseChannel=baseaddress, channelCount=3,
                    name=name, devtype="Spot",
                    channelTypes=[CHANNEL_TYPE_RED,
                                  CHANNEL_TYPE_GREEN,
                                  CHANNEL_TYPE_BLUE],
                    constantChannels={},
                    dimmerRange=[0, 1, 254, 255])
    device_manager.addDMXDevice(dev)
    return dev

def addLedBar240_8(device_manager, name, baseaddress, universe):
    nodes = []
    for i in range(8):
        nodes.append(__addRGBBarSegment(device_manager, "{}, Segment {}".format(name, i), baseaddress + 3*i, universe))

    dev = DMXDevice(universe=-1, baseChannel=0, channelCount=3,
                    name=name, devtype="RGB Bar",
                    channelTypes=[CHANNEL_TYPE_RED, CHANNEL_TYPE_GREEN,
                                  CHANNEL_TYPE_BLUE],
                    constantChannels={})

    for d in nodes:
        d.setParent(dev)

    device_manager.addDMXDevice(dev)
    return dev