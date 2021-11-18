def rgb_to_rgbw(red, green, blue):
    white = min(red, green, blue)
    red = red - white
    green = green - white
    blue = blue - white

    return red, green, blue, white