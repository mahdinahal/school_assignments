from gturtle import *

def quadrat(s):
    repeat 4:
        fd(s)
        rt(90)
        
def rotquads(s,n):
    repeat n:
        quadrat(s)
        rt(360/n)        
    

makeTurtle()
hideTurtle()

rotquads(100,20)