import pygame
import random
pygame.init()  
pygame.display.set_caption("easy platformer")  # sets the window title
screen = pygame.display.set_mode((1000, 800))  # creates game screen
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
ypos = 700 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform
offset = 0
jumps = 1
airJump = False
lvl = 1

class star:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 2
    def draw(self):
        pygame.draw.circle(screen, (255,255,255), (self.x, self.y), self.size)
    def update(self, offset):
        self.offset = offset
        self.x = self.x + offset



class platform:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (random.randrange(0,200), random.randrange(100,105), random.randrange(100,255))
        self.offset = 0
        
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 200, 20))
         
    def collide(self, px, py):
        if px>self.x and px<self.x + 200 and py+20 >self.y and py+20 <self.y + 20:
            return self.y - 20 
        else:
            return False
        
    def update(self, offset):
        self.offset = offset
        self.x = self.x + offset
        

starbag = list()
for i in range(100):
    starbag.append(star(random.randrange(-1600, 2400), random.randrange(0,800)))


plats = list()
for i in range(40):
    val = random.randrange(1, 40) + (20*i)
    plats.append(platform(random.randrange(-1600, 2400), val))

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
                
            if event.key == pygame.K_UP:
                keys[UP]=True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False

            if event.key == pygame.K_UP:
                keys[UP]=False
                
            if event.key == pygame.K_RIGHT:
                keys[RIGHT]= False
          
    #physics section--------------------------------------------------------------------
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        if xpos > 300:
            vx =-5
            offset = 0
        else:
            xpos = 300
            offset =+ 5
            vx = 0
        direction = LEFT
        
    elif keys[RIGHT]==True:
        if xpos < 700:
            vx =+5
            offset = 0
        else:
            xpos = 700
            vx = 0
            offset =- 5
        direction = RIGHT

    #turn off velocity
    else:
        offset = 0
        vx = 0
    
    
    isOnGround = False
    
    for i in range(len(plats)):
        if plats[i].collide(xpos, ypos) != False:
            jumps = 1
            vy = 0
            ypos = plats[i].collide(xpos, ypos)
            isOnGround = True
            airJump = False
        plats[i].update(offset)
        
    for i in range(len(starbag)):
        starbag[i].update(offset / 2)
        
                   
        
        
        #stop falling if on bottom of game screen
    if ypos > 780:
        jumps = 1
        isOnGround = True
        vy = 0
        ypos = 780
        airJump = False
        
    if ypos < 5:
        ypos =+ 750
        lvl += 1
        plats = list()
        for i in range(40):
            val = random.randrange(1, 10) + (20*i)
            plats.append(platform(random.randrange(-1600, 2400), val))
        starbag = list()
        for i in range(110 + (lvl * 10)):
            starbag.append(star(random.randrange(-1600, 2400), random.randrange(0,800)))

    #JUMPING
    if keys[UP] and jumps > 0 and airJump or keys[UP] and isOnGround: #only jump when on the ground
        vy = -8.8
        direction = UP
        if isOnGround == True and airJump == False:
            isOnGround = False
            print("groundjump")
            airJump = False
        elif isOnGround == False and airJump:
            jumps -= 1
            print("airjump")
            
            
    #gravity
    if isOnGround == False:
        vy+=.4 #notice this grows over time, aka ACCELERATION
        if keys[UP] == False:
            airJump = True
    

    #update player position
    xpos+=vx 
    ypos+=vy
  
    # RENDER Section--------------------------------------------------------------------------------
            
    screen.fill((fill,fill,fill)) #wipe screen so it doesn't smear
  
    
    
    for i in range(len(starbag)):
        starbag[i].draw()
    
    for i in range(len(plats)):
        plats[i].draw()
        
    pygame.draw.rect(screen, (97, 255, 139), (xpos, ypos, 20, 20))
                   
    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()
