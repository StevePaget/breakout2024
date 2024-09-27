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
        self.ySpeed = 10
        self.xSpeed = 8
        
    def move(self):
        self.yPos += self.ySpeed
        self.xPos += self.xSpeed
        if self.xPos<0 or self.xPos>1000:
            self.xSpeed *= -1
        if self.yPos <0 or self.yPos > 900:
            self.ySpeed *= -1
        drawEllipse(self.xPos, self.yPos, 25,25,self.colour)

class Brick:
    def __init__(self,x,y, colour):
        # attributes
        self.xPos = x
        self.yPos = y
        self.colour = colour
        self.width = 75
        self.height = 50
        
    def draw(self):
        drawRect(self.xPos,self.yPos,self.width, self.height, self.colour)
        
    def detectHit(self, ball):
        if self.xPos <=  ball.xPos <= self.xPos +self.width:
            if  self.yPos <= ball.yPos <= self.yPos +self.height:
                return True
        return False
                
    def update(self,ball):
        self.draw()
        print(self.detectHit(ball))


balls= []
balls.append(Ball(500,500,"red"))
bricks = []
for x in range(0,1000, 77):
    bricks.append(Brick(x,100,"orange"))
    bricks.append(Brick(x,200,"purple"))
    bricks.append(Brick(x,300,"green"))
    
    
while True:
    clearShapes()
    for b in balls:
        b.move()
    for brick in bricks:
        brick.draw()
    tick(60)
    updateDisplay()
    
endWait()
