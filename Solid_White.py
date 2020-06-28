import time
import board
import adafruit_dotstar as dotstar

# On-board DotStar for boards including Gemma, Trinket, and ItsyBitsy
strip = dotstar.DotStar(board.SCK, board.MOSI, 60, brightness=1.0)

strip.fill((255, 255, 255))