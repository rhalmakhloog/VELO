import time
import random
import board
import adafruit_dotstar as dotstar

# On-board DotStar for boards including Gemma, Trinket, and ItsyBitsy
strip = dotstar.DotStar(board.SCK, board.MOSI, 60, brightness=0.6)

# Using a DotStar Digital LED Strip with 30 LEDs connected to hardware SPI
# dots = dotstar.DotStar(board.SCK, board.MOSI, 30, brightness=0.2)

# Using a DotStar Digital LED Strip with 30 LEDs connected to digital pins
# dots = dotstar.DotStar(board.D6, board.D5, 30, brightness=0.2)
numpix = 60
pos = 0  # position
direction = 1  # direction of "eye"

while True:

    strip[pos - 2] = ([255, 255, 0]) # Dark red
    strip[pos - 1] = ([128, 0, 0])  # Medium red
    strip[pos] = ([255, 48, 0])  # brightest
    strip[pos + 1] = ([128, 0, 0])  # Medium red
    strip[pos + 2] = ([255, 0, 0])  # Medium red


    if (pos + 6) < numpix:
        # Dark red, do not exceed number of pixels
        strip[pos + 6] = ([255, 0, 0])

    strip.show()
    time.sleep(0.00)



    # Bounce off ends of strip
    pos += direction
    if pos < 0:
        pos = 1
        direction = -direction
    elif pos >= (numpix - 1):
        pos = numpix - 2
        direction = -direction