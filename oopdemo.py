from pygame_functions import *
import random

screenSize(1000,900)
setBackgroundColour("#BBBBFF")
setAutoUpdate(False)

class Ball:
    def __init__(self,x,y, colour):
        # attributes
        self.xPos = x
        self.yPos = y
        self.colour = colour
        self.ySpeed = 0
        self.xSpeed = random.randint(-10,10)
        
    def move(self):
        self.ySpeed += 1
        self.yPos += self.ySpeed
        self.xPos += self.xSpeed
        if self.xPos<0 or self.xPos>900:
            self.xSpeed *= -1
        if self.yPos > 900:
            self.ySpeed *= -1
            self.yPos = 900
        drawEllipse(self.xPos, self.yPos, 50,50,self.colour)

balls= []
for i in range(500):
    red = random.randint(1,255)
    green = random.randint(1,255)
    blue = random.randint(1,255)
    balls.append(Ball(random.randint(50,850),random.randint(50,600),(red,green,blue)))
    
while True:
    clearShapes()
    for b in balls:
        b.move()
    tick(60)
    updateDisplay()
    
endWait()
