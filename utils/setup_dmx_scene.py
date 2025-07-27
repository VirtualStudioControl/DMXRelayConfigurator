from devices.grouping import addGroupRGBAWUv
from devices.stairville import addStairvilleXBrickHex
from devices.varytec import addVarytecHeroWash715
from dmxrelayconfigurator.dmx import device_manager
from dmxrelayconfigurator.io.filetools import writeJSON

UNIVERSE_1 = 0

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

    #mh = []
    #mhe = []
    #big = []

    #mh.append(addMovingHead("I01 - RGBW MovingHead", 0, UNIVERSE_1))
    #mhe.append(addETECRGBWAUvMovingHead("I02 - ETEC RGBWAUv MovingHead", 15, UNIVERSE_1))
    #mh.append(addMovingHead("I03 - RGBW MovingHead", 30, UNIVERSE_1))
    #mh.append(addMovingHead("I04 - RGBW MovingHead", 45, UNIVERSE_1))
    #mh.append(addMovingHead("I05 - RGBW MovingHead", 60, UNIVERSE_1))

    #big.append(addBIG("I06 - BIG", 75, UNIVERSE_1))

    #mh.append(addMovingHead("I07 - RGBW MovingHead", 90, UNIVERSE_1))
    #mh.append(addMovingHead("I08 - RGBW MovingHead", 105, UNIVERSE_1))

    #big.append(addBIG("I09 - BIG", 120, UNIVERSE_1))

    #mh.append(addMovingHead("I10 - RGBW MovingHead", 135, UNIVERSE_1))
    #mh.append(addMovingHead("I11 - RGBW MovingHead", 150, UNIVERSE_1))
    #mhe.append(addETECRGBWAUvMovingHead("I12 - ETEC RGBWAUv MovingHead", 165, UNIVERSE_1))

    #big.append(addBIG("I13 - BIG", 180, UNIVERSE_1))

    #mh.append(addMovingHead("I14 - RGBW MovingHead", 195, UNIVERSE_1))
    #mh.append(addMovingHead("I15 - RGBW MovingHead", 210, UNIVERSE_1))
    #mh.append(addMovingHead("I16 - RGBW MovingHead", 225, UNIVERSE_1))


    #mheg = addGroupRGBWAUvMHs("RGBWAUv MovingHeads", mhe)
    #mhgg = addGroupMHs("RGBW MovingHeads", mh)
    #mhg = addGroupMHs("RGBW MovingHeads", [mheg, mhgg])

    #bigg = addGroupRGB("Bigs", big)

    xbrick = addStairvilleXBrickHex(device_manager, "XBrick 1", 99, 0)
    mh = addVarytecHeroWash715(device_manager, "MH1", 49, 0)

    all = addGroupRGBAWUv("ALL", [xbrick, mh])

    values = device_manager.toDict()
    writeJSON("dmxscene.json", values)