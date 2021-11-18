from typing import List

from dmxrelayconfigurator.dmx.dmxdevice import DMXDevice, fromDict as dictToDMXDevice

DMX_DEVICES: List[DMXDevice] = []


def addDMXDevice(device: DMXDevice):
    DMX_DEVICES.append(device)


def clearDMXDevices():
    DMX_DEVICES.clear()


def getDMXDevices():
    return DMX_DEVICES


def toDict():
    devices = []
    for dev in DMX_DEVICES:
        if not dev.hasParent():
            devices.append(dev.toDict())

    return {
        "dmxdevices": devices
    }


def fromDict(values):
    for device in values["dmxdevices"]:
        addDMXDevice(dictToDMXDevice(device))
