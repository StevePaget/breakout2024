from pygame_functions import *
import random

screenSize(1000,900)
setBackgroundColour("#000000")
setAutoUpdate(False)

class Ball:
    def __init__(self,x,y, colour):
        # attributes
        self.xPos = x
        self.yPos = y
        self.colour = colour
        self.ySpeed = 10
        self.xSpeed = 8
        
    def move(self, lives):
        self.yPos += self.ySpeed
        self.xPos += self.xSpeed
        if self.xPos<0 or self.xPos>1000:
            self.xSpeed *= -1
        if self.yPos <0:
            self.ySpeed *= -1
        if self.yPos > 900:
            lives -= 1
            self.ySpeed *= -1
            self.yPos = 700
            self.xPos = 500
        drawEllipse(self.xPos, self.yPos, 25,25,self.colour)
        return lives
            
class Brick:
    def __init__(self,x,y, colour):
        # attributes
        self.xPos = x
        self.yPos = y
        self.colour = colour
        self.width = 75
        self.height = 50
        self.active= True
        
    def draw(self):
        if self.active:
            drawRect(self.xPos,self.yPos,self.width, self.height, self.colour)
        
    def detectHit(self, balls):
        for ball in balls:
            if self.xPos <=  ball.xPos <= self.xPos +self.width:
                if  self.yPos <= ball.yPos <= self.yPos +self.height:
                    ball.ySpeed *= -1
                    return True
        return False
                
    def update(self,balls):
        self.draw()
        if self.active and self.detectHit(balls):
            self.active = False


class Bat(Brick): # inherits the Brick class
    def __init__(self,x,y,colour):
        super().__init__(x,y,colour)
        self.width=150
        self.height = 25
        
    def update(self, balls): # overriding the previous
        self.draw()
        self.detectHit(balls)
        self.xPos = mouseX()-75

class MultiBrick(Brick):
    
    def update(self,balls):
        self.draw()
        if self.active and self.detectHit(balls):
            self.active = False
            balls.append( Ball(self.xPos, self.yPos, "yellow"))
    
    
balls= []
balls.append(Ball(500,500,"red"))
bricks = []
for x in range(0,1000, 77):
    bricks.append(Brick(x,100,"orange"))
    bricks.append(Brick(x,200,"purple"))
    bricks.append(Brick(x,300,"green"))

randomPos = random.randint(0,len(bricks))
removedbrick = bricks.pop(randomPos)
bricks.insert(randomPos,MultiBrick(removedbrick.xPos,
                                   removedbrick.yPos,"red"))
    
bat = Bat(500,850,"lightblue")  # Instantiation
lives = 3
livesLabel = makeLabel("Lives:", 24, 10,10,"white")
showLabel(livesLabel)
gameOverLabel = makeLabel("GAME OVER", 50, 350,450,"red")
running = True
while running:
    clearShapes()
    changeLabel(livesLabel, "Lives: " + str(lives))
    bat.update(balls)
    for b in balls:
        lives = b.move(lives) # send the number of lives
        if lives <=0:
            showLabel(gameOverLabel)
            running = False
    for brick in bricks:
        brick.update(balls)
    tick(60)
    updateDisplay()
    
endWait()
