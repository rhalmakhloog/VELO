import time
import board
import adafruit_dotstar as dotstar

# On-board DotStar for boards including Gemma, Trinket, and ItsyBitsy
strip = dotstar.DotStar(board.SCK, board.MOSI, 60, brightness=0.6)
strip2 = dotstar.DotStar(board.D6, board.D5, 60, brightness=0.9)
# Using a DotStar Digital LED Strip with 30 LEDs connected to hardware SPI
# dots = dotstar.DotStar(board.SCK, board.MOSI, 30, brightness=0.2)

# Using a DotStar Digital LED Strip with 30 LEDs connected to digital pins
# dots = dotstar.DotStar(board.D6, board.D5, 30, brightness=0.2)
numpix = 30
pos = 0  # position
direction = 30  # direction of "eye"

while True:
    strip2[pos] = ([255, 0, 0])  # brightest
    strip2[pos + 1] = ([255, 0, 0])  # Medium red
    strip2[pos + 2] = ([255, 0, 0])
    strip2[pos + 3] = ([255, 0, 0])
    strip2[pos + 4] = ([255, 0, 0])
    strip2[pos + 5] = ([255, 0, 0])
    strip2[pos + 6] = ([255, 0, 0])
    strip2[pos + 7] = ([255, 0, 0])
    strip2[pos + 8] = ([255, 0, 0])
    strip2[pos + 9] = ([255, 0, 0])
    strip2[pos + 10] = ([255, 0, 0])
    strip2[pos + 11] = ([255, 0, 0])  # Medium red
    strip2[pos + 12] = ([255, 0, 0])
    strip2[pos + 13] = ([255, 0, 0])
    strip2[pos + 14] = ([255, 0, 0])
    strip2[pos + 15] = ([255, 0, 0])
    strip2[pos + 16] = ([255, 0, 0])
    strip2[pos + 17] = ([255, 0, 0])
    strip2[pos + 18] = ([255, 0, 0])
    strip2[pos + 19] = ([255, 0, 0])
    strip2[pos + 20] = ([255, 0, 0])

    if (pos ) < numpix:
        # Dark red, do not exceed number of pixels
        strip2[pos ] = ([255, 0, 0])

    strip2.show()
    time.sleep(0.00)

    # Rather than being sneaky and erasing just the tail pixel,
    # it's easier to erase it all and draw a new one next time.
    for j in range(-15, 15):
        strip2[pos + j] = (0, 0, 0)
        if (pos + 0) < numpix:
            strip2[pos + 0] = (0, 0, 0)

    # Bounce off ends of strip
    pos += direction
    if pos < 0:
        pos = 1
        direction = -direction
    elif pos >= (numpix - 1):
        pos = numpix - 30
        direction = direction