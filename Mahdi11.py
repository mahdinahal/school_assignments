from gturtle import *

def circle():
    repeat 360:
        fd(2)
        rt(1)
    
makeTurtle()
hideTurtle()

repeat 4:
    circle()
    rt(90)