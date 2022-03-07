import pygame
import random
pygame.init()  
pygame.display.set_caption("breakout")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

LEFT = 0
RIGHT = 1

keys = [False, False]

random.seed()


class Brick:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        rand = random.randrange(0,255)
        self.color = (rand, 255 - rand, rand / 2)
        self.width = 80
        self.height = 20
        self.alive = True
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.width = 10
        self.height = 10
        
        self.vx = random.randrange(-6,6)
        self.vy = -5
    def draw(self):
        pygame.draw.rect(screen, (255,255,255), (self.x, self.y, self.width, self.height))
    def update(self):
        self.x += self.vx
        self.y += self.vy
        
        if self.x < 0:
            self.x = 0
            self.vx *= -1
        elif self.x > 805:
            self.x = 805
            self.vx *= -1
        
        if self.y < 0:
            self.y = 0
            self.vy *= -1
        elif self.y > 805:
            self.y = 805
            self.vy *= -1
    def collide(self, rect):
        if self.x < rect.x + rect.width and self.x + self.width > rect.x and self.y < rect.y + rect.height and self.y > rect.y:
            self.vy *= random.choice((-1.2, -1.1, -1, -0.9, -0.8))
            return True
        else:
            return False
        


class Paddle:
    def __init__(self):
        self.x = 360
        self.y = 700
        self.width = 80
        self.height = 10
    def draw(self):
        pygame.draw.rect(screen, (255,255,255), (self.x, self.y, self.width, self.height))

        

bricks = list()
for i in range(24):
    newBrick = Brick(((i % 8) * 80) + ((i % 8) *20) + 10, (((i % 3) * 10) + 40 + (i % 3) * 20) )
    bricks.append(newBrick)
    
ball = Ball(392, 650)

paddle = Paddle()
    
while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS
    
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
            
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
                
            if event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False

            if event.key == pygame.K_RIGHT:
                keys[RIGHT]= False
                
                
    #UPDATE--------------------------------------------------------------------
    if keys[LEFT]:
        paddle.x -= 7
    if keys[RIGHT]:
        paddle.x += 7
        
    for brick in bricks:
        if brick.alive:
            check = ball.collide(brick)
        if check:
            brick.alive = False
    
    ball.collide(paddle)    
        
    ball.update()
    
    
    
   #RENDER------------------------------------------------------------------------- 
        
    screen.fill((0,0,0))


    for brick in bricks:
        if brick.alive:
            brick.draw()
        
    ball.draw()
        
    paddle.draw()
        
    pygame.display.flip()
        
pygame.quit()

