from Brush import Brush

# Brush settings.
# Change after the you're able to paint on the canvas
Brush.NUMBER_OF_BRISTLES = 200
Brush.BRUSH_SIZE = 20
Brush.BRUSH_THICKNESS = 20
Brush.BRUSH_STAGGER = 6

#
# Objective: Create a program to paint some Van Gogh paintings!
#

# 1. Create global variables for a paintbrush, canvas, and painting
# global paintbrush, canvas, painting
global paintbrush, canvas, painting

def setup():
    size(800, 500)
    initializeCursor()

    # 2. Declare the global variables from step 1) in this function, example:
    # global paintbrush, canvas, painting
    global paintbrush, canvas, painting

    # 3. Use the loadImage function to initialize the canvas AND
    # painting variables in the images folder, example:
    # canvas = loadImage("../images/canvas.jpg")
    canvas = loadImage("../images/canvas.jpg")

    # 4. Use the loadImage function to initialize the painting variable
    painting = loadImage("../images/starryNight.jpg")

    # 5. Call resize on the canvas and painting variables to resize
    # the width and height
    canvas.resize(width, height)
    painting.resize(width, height)

    # 6. Use the background function to set the canvas image as the background
    # Do you see the canvas image on the window?
    background(canvas)

    # 7. Initialize the brush variable to a new Brush, example:
    # paintbrush = Brush(painting)
    # You won't see the paint until you complete the next step!
    paintbrush = Brush(painting)

def draw():
    pass
    # 8. Call the brush's update and draw methods
    # Do you see the paint on the window when you hold down the mouse?
    paintbrush.update()
    paintbrush.draw()

def keyPressed():
    pass
    # 9. Reset the background canvas when the key variable is equal to 'r'
    if key == 'r':
        background(canvas)

# 10. Try painting the other paintings in the /images folder and changing the
# paintbrush settings at the top of the file.

# 11.EXTRA: Find more paintings and add them to your code.
#           Watercolor paintings work the best!


def initializeCursor():
    paintbrush_cursor = loadImage("../images/paintbrushCur.png")
    paintbrush_cursor.resize(22 * 2, 28 * 2)
    cursor(paintbrush_cursor)


if __name__ == '__main__':
    if False:
        from ..lib.Processing3 import *

    try:
        __papplet__
    except NameError:
        import subprocess
        subprocess.call('java -jar ../lib/processing-py.jar ' + __file__)
