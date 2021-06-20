
import math
from graphics import Canvas
import random
import time

CANVAS_WIDTH = 420
CANVAS_HEIGHT = 600

NBRICK_COLUMNS = 10

NBRICK_ROWS = 10
BRICK_SEP = 4
BRICK_WIDTH = math.floor((CANVAS_WIDTH - (NBRICK_COLUMNS + 1.0) * BRICK_SEP) / NBRICK_COLUMNS)
BRICK_HEIGHT = 8
BRICK_Y_OFFSET = 70
BALL_RADIUS = 10
VELOCITY_Y = 6.0
VELOCITY_X_MIN = 2.0
VELOCITY_X_MAX = 6.0
DELAY = 1 / 60
PADDLE_WIDTH = 60
PADDLE_HEIGHT = 10
PADDLE_Y_OFFSET = 30
NTURNS = 3
BOUNCE_SOUND = "bounce.au"



def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("Breakout")
    while True:
        keys = canvas.get_new_key_presses()
        for key in keys:
            print(keys)
    # TODO: your code here!

    canvas.mainloop()


if __name__ == '__main__':
    main()
