from dmxrelayconfigurator.dmx import device_manager
from dmxrelayconfigurator.dmx.dmxdevice import *

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

def addGroupRGBAWUv(name, devicelist):
    dev = DMXDevice(universe=-1, baseChannel=0, channelCount=6,
              name=name, devtype="RGBAWUv Group",
              channelTypes=[CHANNEL_TYPE_RED,
                            CHANNEL_TYPE_GREEN,
                            CHANNEL_TYPE_BLUE,
                            CHANNEL_TYPE_WHITE,
                            CHANNEL_TYPE_AMBER,
                            CHANNEL_TYPE_UV],
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