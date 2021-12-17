from dmxrelayconfigurator.dmx import device_manager
from dmxrelayconfigurator.dmx.dmxdevice import *
from dmxrelayconfigurator.io.filetools import writeJSON

UNIVERSE_1 = 1
UNIVERSE_2 = 2

#region Device Creators
def addBIG(name, baseaddress, universe):
    dev = DMXDevice(universe=universe, baseChannel=baseaddress, channelCount=8,
                                          name=name, devtype="Big Deeper Sleeka S60 Slim",
                                          channelTypes=[CHANNEL_TYPE_RED, CHANNEL_TYPE_GREEN, CHANNEL_TYPE_BLUE,
                                                        CHANNEL_TYPE_STROBO,
                                                        CHANNEL_TYPE_COLOR_MODE, CHANNEL_TYPE_COLOR_JUMP_SPEED,
                                                        CHANNEL_TYPE_UNKNOWN, CHANNEL_TYPE_UNKNOWN],
                                          constantChannels={CHANNEL_TYPE_COLOR_MODE: 0x00})
    device_manager.addDMXDevice(dev)
    return dev


def addUKing(name, baseaddress, universe):
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


def addMovingHead(name, baseaddress, universe):
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


def addRGBAWMovingHead(name, baseaddress, universe):
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


def addSpot(name, baseaddress, universe):
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


def addMini(name, baseaddress, universe):
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

#region Groups

def addGroupRGB(name, devicelist):
    dev = DMXDevice(universe=-1, baseChannel=0, channelCount=3,
              name=name, devtype="RGB Group",
              channelTypes=[CHANNEL_TYPE_RED, CHANNEL_TYPE_GREEN,
                            CHANNEL_TYPE_BLUE, CHANNEL_TYPE_DIMMER],
              constantChannels={})

    for d in devicelist:
        d.setParent(dev)

    device_manager.addDMXDevice(dev)
    return dev

def addGroupMHs(name, devicelist):
    dev = DMXDevice(universe=-1, baseChannel=0, channelCount=9,
                    name=name, devtype="MH Group",
                    channelTypes=[CHANNEL_TYPE_RED, CHANNEL_TYPE_GREEN,
                                  CHANNEL_TYPE_BLUE, CHANNEL_TYPE_WHITE,
                                  CHANNEL_TYPE_DIMMER,
                                  CHANNEL_TYPE_PAN, CHANNEL_TYPE_PAN_FINE,
                                  CHANNEL_TYPE_TILT, CHANNEL_TYPE_TILT_FINE,
                                  CHANNEL_TYPE_XYSPEED],
                    constantChannels={})

    for d in devicelist:
        d.setParent(dev)

    device_manager.addDMXDevice(dev)
    return dev

#endregion


if __name__ == "__main__":
    mhs = []
    bigs = []
    ukings = []

    mhs.append(addMovingHead("MH 1", 0, UNIVERSE_1))
    mhs.append(addMovingHead("MH 2", 14, UNIVERSE_1))
    mhs.append(addMovingHead("MH 3", 28, UNIVERSE_1))
    mhs.append(addMovingHead("MH 4", 42, UNIVERSE_1))

    bigs.append(addBIG("BIG 1", 56, UNIVERSE_1))
    bigs.append(addBIG("BIG 2", 64, UNIVERSE_1))
    bigs.append(addBIG("BIG 3", 72, UNIVERSE_1))
    bigs.append(addBIG("BIG 4", 80, UNIVERSE_1))

    ukings.append(addUKing("UK 1", 88, UNIVERSE_1))
    ukings.append(addUKing("UK 2", 96, UNIVERSE_1))

    addSpot("SP 1", 104, UNIVERSE_1)
    addSpot("SP 2", 112, UNIVERSE_1)

    addRGBAWMovingHead("rgbaw-MH", 139, UNIVERSE_1)
    addRGBAWMovingHead("rgbaw-MH", 159, UNIVERSE_1)

    mhs.append(addMovingHead("MH 5", 0, UNIVERSE_2))
    mhs.append(addMovingHead("MH 6", 14, UNIVERSE_2))
    mhs.append(addMovingHead("MH 7", 28, UNIVERSE_2))
    mhs.append(addMovingHead("MH 8", 42, UNIVERSE_2))
    mhs.append(addMovingHead("MH 9", 56, UNIVERSE_2))
    mhs.append(addMovingHead("MH 10", 70, UNIVERSE_2))

    ukings.append(addUKing("UK 3", 84, UNIVERSE_2))
    ukings.append(addUKing("UK 4", 92, UNIVERSE_2))
    ukings.append(addUKing("UK 5", 100, UNIVERSE_2))
    ukings.append(addUKing("UK 6", 108, UNIVERSE_2))
    ukings.append(addUKing("UK 7", 116, UNIVERSE_2))

    addMini("MINI 1", 132, UNIVERSE_2)

    addRGBAWMovingHead("rgbaw-MH", 139, UNIVERSE_2)
    addRGBAWMovingHead("rgbaw-MH", 159, UNIVERSE_2)
    addRGBAWMovingHead("rgbaw-MH", 179, UNIVERSE_2)

    mhg = addGroupMHs("Moving Heads", mhs)
    bigg = addGroupRGB("Bigs", bigs)
    ukingg = addGroupRGB("UKings", ukings)

    all = addGroupRGB("ALL", [mhg, bigg, ukingg])

    values = device_manager.toDict()
    print(values)
    writeJSON("dmxscene.json", values)