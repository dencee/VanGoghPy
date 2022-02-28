if False:
    from lib.Processing3 import *

from Brush import Brush

global brush, canvas
canvas = None
brush = None

def setup():
    global brush, canvas
    size(800, 500)

    # starryNight.jpg painterOnRoad.jpg, wheatField.jpg, strawHatPortrait.jpg
    canvas = loadImage("images/canvas.jpg")
    painting = loadImage("images/starryNight.jpg")

    canvas.resize(width, height)
    painting.resize(width, height)

    paintbrush_cursor = loadImage("images/paintbrushCur.png")
    paintbrush_cursor.resize(22 * 2, 28 * 2)
    cursor(paintbrush_cursor)
    background(canvas)

    brush = Brush(painting)

def draw():
    brush.update()
    brush.draw()
    pass

def keyPressed():
    if key == 'r':
        image(canvas, 0, 0)


if __name__ == '__main__':
    try:
        __papplet__
        #li = list(globals())
        #for i in li:
        #    print(i)
        #print(PApplet.__dict__)
        print('got')
    except NameError:
        import os
        os.system('java -jar lib/processing-py.jar ' + __file__)

