
def mapLinear(value, omin, omax, nmin, nmax):
    if omin == nmin and omax == nmax:
        return value
    factor = float(value-omin)/float(omax - omin)
    return (factor * (nmax - nmin)) + nmin


def rgb_to_rgbw(red, green, blue):
    white = min(red, green, blue)
    red = red - white
    green = green - white
    blue = blue - white

    return red, green, blue, white


def rgbw_to_rgb(red, green, blue, white):

    red = min(255, red + white)
    green = min(255, green + white)
    blue = min(255, blue + white)

    return red, green, blue

def rgbwa_to_rgb(red, green, blue, white, amber=0):

    red = min(255, red + white + amber)
    green = min(255, green + white + (amber//2))
    blue = min(255, blue + white)

    return red, green, blue


def byte_to_dimmer_range(value, dimmerRange):
    if value <= 0:
        return dimmerRange[0]
    if value >= 0xff:
        return dimmerRange[3]
    return round(mapLinear(value, 1, 254, dimmerRange[1], dimmerRange[2]))


def dimmer_range_to_byte(value, dimmerRange):
    if value <= dimmerRange[0]:
        return 0
    if value >= dimmerRange[3]:
        return 0xff
    return round(mapLinear(value, dimmerRange[1], dimmerRange[2], 1, 254))
