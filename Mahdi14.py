from gturtle import *

def figur1(s):
    repeat 3:
        fd(s)
        rt(120)
        
def figur2(s):
    repeat 6:
        figur1(s)
        rt(60)
        
makeTurtle()
hideTurtle()

figur2(100)