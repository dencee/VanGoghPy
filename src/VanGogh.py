if False:
    from lib.Processing3 import *

from Brush import Brush

# Brush settings. Change after the you're able to paint on the canvas
Brush.NUMBER_OF_BRISTLES = 200
Brush.BRUSH_SIZE = 20
Brush.BRUSH_THICKNESS = 20
Brush.BRUSH_STAGGER = 6

#
# Objective: Paint a Van Gogh painting
#
# 1. Create global variables for a paintbrush, canvas, and painting


def setup():
    size(800, 500)
    initializeCursor()

    # 2. Declare the global variables from step 1), example:
    # global brush, canvas, painting


    # 3. Use the loadImage function to initialize the canvas AND
    # painting variables in the images folder, example:
    # canvas = loadImage("images/canvas.jpg")


    # 4. Call resize on the canvas and painting variables to resize
    # the width and height, example
    # canvas.resize(width, height)


    # 5. Use the background function to set the canvas image as the background
    # Do you see the canvas image on the window?


    # 6. Initialize the brush variable to a new Brush, example:
    # brush = Brush(painting)
    # You won't see the paint until you complete the next step!


def draw():
    pass
    # 7. Call the brush's update and draw methods
    # Do you see the paint on the window when you hold down the mouse?


def keyPressed():
    pass
    # 8. Reset the background canvas when the key variable is equal to 'r'


def initializeCursor():
    paintbrush_cursor = loadImage("images/paintbrushCur.png")
    paintbrush_cursor.resize(22 * 2, 28 * 2)
    cursor(paintbrush_cursor)

if __name__ == '__main__':
    try:
        __papplet__
    except NameError:
        import os
        os.system('java -jar lib/processing-py.jar ' + __file__)

