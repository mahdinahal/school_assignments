from gturtle import *

def quadrat100():
    repeat 4:
        fd(100)
        rt(90)

makeTurtle()
quadrat100()
repeat 360:
    rt(1)
    quadrat100()
