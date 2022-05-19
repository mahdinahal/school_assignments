from gturtle import *

def quadrat(s):
    repeat 4:
        fd(s)
        rt(90)
        
def rotquads(n):
    repeat n:
        quadrat(50)
        rt(360/n)        
    

makeTurtle()
hideTurtle()

rotquads(20)