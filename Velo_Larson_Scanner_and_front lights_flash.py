import time
import board
import adafruit_dotstar as dotstar

# On-board DotStar for boards including Gemma, Trinket, and ItsyBitsy
strip2 = dotstar.DotStar(board.D6, board.D5, 60, brightness=0.5)

# Using a DotStar Digital LED Strip with 30 LEDs connected to hardware SPI
# dots = dotstar.DotStar(board.SCK, board.MOSI, 30, brightness=0.2)

# Using a DotStar Digital LED Strip with 30 LEDs connected to digital pins
# dots = dotstar.DotStar(board.D6, board.D5, 30, brightness=0.2)
numpix = 10
pos = 0  # position
direction = 1  # direction of "eye"

while True:

    strip2[pos - 2] = ([50, 0, 0])    # Dark red
    strip2[pos - 1] = ([50, 0, 0])  # Medium red
    strip2[pos] = ([255, 0, 0])  # brightest
    strip2[pos + 1] = ([255, 0, 0])  # Medium red
    strip2[pos + 2] = ([255, 0, 0])  # Medium red
    strip2[pos + 3] = ([255, 0, 0])  # Medium red
    strip2[pos + 4] = ([255, 0, 0])  # Medium red
    strip2[pos + 5] = ([255, 0, 0])  # Medium red
    strip2[pos + 6] = ([255, 0, 0])  # Medium red
    strip2[pos + 7] = ([255, 0, 0])  # Medium red
    strip2[pos + 8] = ([255, 0, 0])  # Medium red
    strip2[pos + 9] = ([255, 0, 0])  # Medium red
    strip2[pos + 10] = ([255, 0, 0])  # Medium red
    strip2[pos + 11] = ([255, 0, 0])  # Medium red
    strip2[pos + 12] = ([255, 0, 0])  # Medium red
    strip2[pos + 13] = ([255, 0, 0])  # Medium red
    strip2[pos + 14] = ([255, 0, 0])  # Medium red
    strip2[pos + 15] = ([255, 0, 0])  # Medium red

    if (pos + 2) < numpix:
        # Dark red, do not exceed number of pixels
        strip2[pos + 2] = ([255, 0, 0])

    strip2.show()
    time.sleep(0.0)

    # Bounce off ends of strip
    pos += direction
    if pos < 0:
        pos = 1
        direction = -direction
    elif pos >= (numpix - 1):
        pos = numpix - 10
        direction = -direction