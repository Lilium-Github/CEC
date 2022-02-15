import pygame
import random
pygame.init()  
pygame.display.set_caption("easy platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3

fill = 0

#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform


class platform:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        
    def draw(self):
         pygame.draw.rect(screen, self.color, (self.x, self.y, 100, 20))
         
    def collide(self, px, py):
        if px>self.x and px<self.x + 100 and py+40 >self.y and py+40 <self.y + 20:
            return self.y - 40 
        else:
            return False

plats = list()
for i in range(10):
    val = random.randrange(1, 40) + (80*i)
    plats.append(platform(random.randrange(50, 700), val))

while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS
    
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True

            elif event.key == pygame.K_UP:
                keys[UP]=True
                
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False

            elif event.key == pygame.K_UP:
                keys[UP]=False
                
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]= False
          
    #physics section--------------------------------------------------------------------
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-4
        direction = LEFT
        
    elif keys[RIGHT]==True:
        vx=+4
        direction = RIGHT

    #turn off velocity
    else:
        vx = 0
    
    
    isOnGround = False
    
    for i in range(len(plats)):
        if plats[i].collide(xpos, ypos) != False:
            isOnGround = True
            vy = 0
            ypos = plats[i].collide(xpos, ypos)
        
        
        #stop falling if on bottom of game screen
    if ypos > 760:
        isOnGround = True
        vy = 0
        ypos = 760
        
    if ypos < 5:
        ypos = 760
        fill = fill + 5
        plats = list()
        for i in range(10):
            val = random.randrange(1, 80) + (80*i)
            plats.append(platform(random.randrange(50, 700), val))

    #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        isOnGround = False
        direction = UP
    
    #gravity
    if isOnGround == False:
        vy+=.15 #notice this grows over time, aka ACCELERATION
    

    #update player position
    xpos+=vx 
    ypos+=vy
    
  
    # RENDER Section--------------------------------------------------------------------------------
            
    screen.fill((fill,fill,fill)) #wipe screen so it doesn't smear
  
    pygame.draw.rect(screen, (255, 0, 200), (xpos, ypos, 20, 40))
    
    for i in range(len(plats)):
        plats[i].draw()
    
    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()
