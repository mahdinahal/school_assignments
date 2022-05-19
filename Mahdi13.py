from gturtle import *

def vieleck(s,n):
    repeat n:
        fd(s)
        rt(360/n)
        
makeTurtle()
hideTurtle()

vieleck(100,7)