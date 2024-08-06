from dmxrelayconfigurator.dmx import device_manager
from dmxrelayconfigurator.dmx.dmxdevice import *
from dmxrelayconfigurator.io.filetools import writeJSON

UNIVERSE_1 = 0
UNIVERSE_2 = 1

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

def addVarytecHeroWash715 (name, baseaddress, universe):
    dev = DMXDevice(universe=universe, baseChannel=baseaddress, channelCount=16,
                    name=name, devtype="Varytec Hero Wash 715 HEX LED",
                    channelTypes=[CHANNEL_TYPE_PAN, CHANNEL_TYPE_PAN_FINE,
                                  CHANNEL_TYPE_TILT, CHANNEL_TYPE_TILT_FINE, CHANNEL_TYPE_XYSPEED,
                                  CHANNEL_TYPE_DIMMER, CHANNEL_TYPE_STROBO,
                                  CHANNEL_TYPE_RED, CHANNEL_TYPE_GREEN,
                                  CHANNEL_TYPE_BLUE, CHANNEL_TYPE_WHITE, CHANNEL_TYPE_AMBER, CHANNEL_TYPE_UV,
                                  CHANNEL_TYPE_COLOR_TEMPERATURE,
                                  CHANNEL_TYPE_COLOR_MODE, CHANNEL_TYPE_CUSTOM],
                    constantChannels={CHANNEL_TYPE_COLOR_MODE: 0x00,
                                      CHANNEL_TYPE_CUSTOM: 0x00,
                                      CHANNEL_TYPE_RESET: 0x00},
                    dimmerRange=[0, 8, 134, 255])
    device_manager.addDMXDevice(dev)
    return dev

def addETECRGBWAUvMovingHead(name, baseaddress, universe):
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

def addRGBLight(name, baseaddress, universe):
    dev = DMXDevice(universe=universe, baseChannel=baseaddress, channelCount=3,
                    name=name, devtype="Spot",
                    channelTypes=[CHANNEL_TYPE_RED,
                                  CHANNEL_TYPE_GREEN,
                                  CHANNEL_TYPE_BLUE],
                    constantChannels={},
                    dimmerRange=[0, 1, 254, 255])
    device_manager.addDMXDevice(dev)
    return dev

def addRGBBar(name, baseaddress, universe):
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

def addGroupRGBWAUvMHs(name, devicelist):
    dev = DMXDevice(universe=-1, baseChannel=0, channelCount=12,
                    name=name, devtype="MH Group",
                    channelTypes=[CHANNEL_TYPE_RED, CHANNEL_TYPE_GREEN,
                                  CHANNEL_TYPE_BLUE, CHANNEL_TYPE_WHITE,
                                  CHANNEL_TYPE_AMBER, CHANNEL_TYPE_UV,
                                  CHANNEL_TYPE_DIMMER,
                                  CHANNEL_TYPE_XYSPEED,
                                  CHANNEL_TYPE_PAN, CHANNEL_TYPE_PAN_FINE,
                                  CHANNEL_TYPE_TILT, CHANNEL_TYPE_TILT_FINE,
                                  ],
                    constantChannels={})

    for d in devicelist:
        d.setParent(dev)

    device_manager.addDMXDevice(dev)
    return dev

#endregion


if __name__ == "__main__":
#    bars = []
#    rgbaw = []

#    rgbaw.append(addVarytecHeroWash715("Hero Wash", 39, UNIVERSE_1))
#    bars.append(addRGBBar("Bar 1", 0, UNIVERSE_1))
#    bars.append(addRGBBar("Bar 2", 0, UNIVERSE_2))

#    barg = addGroupRGB("Bars", bars)
    #mhg = addGroupMHs("Moving Heads", rgbaw)


#    all = addGroupRGB("ALL", [mhg])

#    mhs = []

#    mhs.append(addMovingHead("Traverse 1",  0, UNIVERSE_1))
#    mhs.append(addMovingHead("Traverse 2", 28, UNIVERSE_1))
#    mhs.append(addMovingHead("Traverse 3", 42, UNIVERSE_1))

#    addGroupMHs("Traverse", mhs)

#    addETECRGBWAUvMovingHead("Notification Light", 139, UNIVERSE_1)

    mh = []
    mhe = []
    big = []

    mh.append(addMovingHead("I01 - RGBW MovingHead", 0, UNIVERSE_1))
    mhe.append(addETECRGBWAUvMovingHead("I02 - ETEC RGBWAUv MovingHead", 15, UNIVERSE_1))
    mh.append(addMovingHead("I03 - RGBW MovingHead", 30, UNIVERSE_1))
    mh.append(addMovingHead("I04 - RGBW MovingHead", 45, UNIVERSE_1))
    mh.append(addMovingHead("I05 - RGBW MovingHead", 60, UNIVERSE_1))

    big.append(addBIG("I06 - BIG", 75, UNIVERSE_1))

    mh.append(addMovingHead("I07 - RGBW MovingHead", 90, UNIVERSE_1))
    mh.append(addMovingHead("I08 - RGBW MovingHead", 105, UNIVERSE_1))

    big.append(addBIG("I09 - BIG", 120, UNIVERSE_1))

    mh.append(addMovingHead("I10 - RGBW MovingHead", 135, UNIVERSE_1))
    mh.append(addMovingHead("I11 - RGBW MovingHead", 150, UNIVERSE_1))
    mhe.append(addETECRGBWAUvMovingHead("I12 - ETEC RGBWAUv MovingHead", 165, UNIVERSE_1))

    big.append(addBIG("I13 - BIG", 180, UNIVERSE_1))

    mh.append(addMovingHead("I14 - RGBW MovingHead", 195, UNIVERSE_1))
    mh.append(addMovingHead("I15 - RGBW MovingHead", 210, UNIVERSE_1))
    mh.append(addMovingHead("I16 - RGBW MovingHead", 225, UNIVERSE_1))


    mheg = addGroupRGBWAUvMHs("RGBWAUv MovingHeads", mhe)
    mhgg = addGroupMHs("RGBW MovingHeads", mh)
    mhg = addGroupMHs("RGBW MovingHeads", [mheg, mhgg])

    bigg = addGroupRGB("Bigs", big)

    all = addGroupRGB("ALL", [mhg, bigg])

    values = device_manager.toDict()
    writeJSON("dmxscene.json", values)