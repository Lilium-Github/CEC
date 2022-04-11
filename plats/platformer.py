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
NONE = 4

fill = 0


player = pygame.image.load('sheep.png') #load your spritesheet
player.set_colorkey((255, 0, 255))


#player variables
xpos = 500 #xpos of player
ypos = 700 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform
offset = 0
jumps = 1
airJump = False
lvl = 1
playerColor = (97, 255, 139)

#variables for animation
frameWidth = 20
frameHeight = 20
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0

class enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 16
        self.image = pygame.image.load('enemy.png')
        self.dir = 0
    def draw(self):
        screen.blit(self.image, (self.x, self.y))
    def update(self, offset):
        if self.dir == RIGHT:
            self.x += 4
        if self.dir == LEFT:
            self.x -= 4
        if self.dir == DOWN:
            self.y += 4
        if self.dir == UP:
            self.y -= 4
        self.x = self.x + offset
        if random.randrange(1, 60) == 1:
            self.dir = random.randrange(0,4)
        

class star:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randrange(1,3)
        self.adder = 1
    def draw(self):
        pygame.draw.circle(screen, (255,255,255), (self.x, self.y), self.size)
    def update(self, offset):
        self.offset = offset
        self.x = self.x + offset
        if random.randrange(1,10) == 1:
            self.size = self.size + self.adder
            if self.size < 2 or self.size > 3:
                self.adder *= -1



class platform:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.startY = y
        self.offset = 0
        self.adder = random.choice((-1, -0.5, 0, 0.5, 1))
        
        if random.randrange(1,6) == 1:
            self.bounce = True
            self.color = (206,99,255)
        else:
            self.bounce = False
            self.color = (120, 244, 255)
        
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 200, 10))
         
    def collide(self, px, py):
        if px + 20>self.x and px<self.x + 200 and py+20 >self.y and py+20 <self.y + 20:
            return self.y - 20 
        else:
            return False
        
    def update(self, offset):
        self.offset = offset
        if self.x < -900 or self.x > 1700:
            self.adder *= -1
        if random.randrange(1,1199) == 1:
            self.adder *= -1
        self.x = self.x + offset + self.adder
        
        if self.y > self.startY:
            self.y -= 1
        

starbag = list()
for i in range(100):
    starbag.append(star(random.randrange(-1600, 2400), random.randrange(0,800)))
    
enemies = list()
for i in range(20):
    val = random.randrange(1, 40) + (40*i)
    enemies.append(enemy(random.randrange(-1600, 2400), val))    

plats = list()
for i in range(40):
    val = random.randrange(1, 40) + (20*i)
    plats.append(platform(random.randrange(-1600, 2400), val))

jump_sound = pygame.mixer.Sound('jump.wav')
double_jump_sound = pygame.mixer.Sound('double_jump.wav')
music = pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1)

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
                
            if event.key == pygame.K_DOWN:
                keys[DOWN]=True
                
            if event.key == pygame.K_SPACE:
                keys[SPACE]=True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False

            if event.key == pygame.K_UP:
                keys[UP]=False
                
            if event.key == pygame.K_RIGHT:
                keys[RIGHT]= False
                
            if event.key == pygame.K_DOWN:
                keys[DOWN]= False
                
            if event.key == pygame.K_SPACE:
                keys[SPACE]= False
          
    #physics section--------------------------------------------------------------------
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        if xpos > 300:
            vx = -5
            offset = 0
        else:
            xpos = 300
            offset = 5
            vx = 0
        direction = LEFT
        
    elif keys[RIGHT]==True:
        if xpos < 700:
            vx = 5
            offset = 0
        else:
            xpos = 700
            vx = 0
            offset = -5
        direction = RIGHT

    #turn off velocity
    else:
        vx = 0
        offset = 0
        
    
    
    isOnGround = False
    
    for i in range(len(plats)):
        if plats[i].collide(xpos, ypos) != False and keys[DOWN] == False:
            jumps = 1
            if vy > 0:
                vy = 0
            ypos = plats[i].collide(xpos, ypos)
            isOnGround = True
            if plats[i].bounce:
                plats[i].y += 10
                vy -= 15
            else: 
                airJump = False
            
            if xpos > 300 and xpos < 700:
                xpos += plats[i].adder * 2
            else:
                offset -= plats[i].adder * 2
    
    for j in range(len(plats)):
        plats[j].update(offset)
        
    for i in range(len(starbag)):
        starbag[i].update(offset / 2)
        
    for i in range(len(enemies)):
        enemies[i].update(offset)
        
                   
        
        
        #stop falling if on bottom of game screen
    if ypos > 780:
        jumps = 1
        isOnGround = True
        vy = 0
        ypos = 780
        airJump = False
        
    if ypos < -19:
        ypos =+ 750
        lvl += 1
        plats = list()
        for i in range(40):
            val = random.randrange(1, 10) + (20*i)
            plats.append(platform(random.randrange(-1600, 2400), val))
            plats[i].adder = (plats[i].adder * lvl / 4) + plats[i].adder
        starbag = list()
        for i in range(110 + (lvl * 10)):
            starbag.append(star(random.randrange(-1600, 2400), random.randrange(0,800)))
        enemies = list()
        for i in range(40):
            val = random.randrange(1, 40) + (20*i)
            enemies.append(enemy(random.randrange(-1600, 2400), val))

    #JUMPING
    if keys[UP] and jumps > 0 and airJump or keys[UP] and isOnGround: #only jump when on the ground
        vy = -8.8
        direction = UP
        if isOnGround == True and airJump == False:
            isOnGround = False
            #print("groundjump")
            airJump = False
            pygame.mixer.Sound.play(jump_sound)
        elif isOnGround == False and airJump:
            jumps -= 1
            #print("airjump")
            pygame.mixer.Sound.play(double_jump_sound)
    
    
            
    #gravity
    if isOnGround == False:
        vy+=.4 #notice this grows over time, aka ACCELERATION
        if keys[UP] == False:
            airJump = True
    if offset < 0:
        offset+=.2
    elif offset > 0:
        offset-=.2
    if vx < 0:
        vx +=.2
    elif vx > 0:
        vx -= .2
    

    #update player position
    xpos+=vx 
    ypos+=vy
    
    if isOnGround or jumps > 0:
        playerColor = (97, 255, 139)
    else:
        playerColor = (242, 0, 202)
        
    # ANIMATION
    if keys[RIGHT]==True:
        RowNum = 0
        # Ticker is a spedometer. We don't want Link animating as fast as the
        # processor can process! Update Animation Frame each time ticker goes over
        ticker+=1
        if ticker%10==0: #only change frames every 10 ticks
          frameNum+=1
           #If we are over the number of frames in our sprite, reset to 0.
           #In this particular case, there are 10 frames (0 through 9)
        if frameNum>3: 
           frameNum = 0
    elif keys[LEFT]==True: #left animation
        RowNum = 1
        ticker+=1
        if ticker%10==0:
          frameNum+=1
        if frameNum>3: 
           frameNum = 0
        
  
    # RENDER Section--------------------------------------------------------------------------------
            
    screen.fill((fill,fill,fill)) #wipe screen so it doesn't smear
  
    
    for i in range(len(starbag)):
        starbag[i].draw()
        
    for i in range(len(enemies)):
        enemies[i].draw()
        
    screen.blit(player, (xpos, ypos), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))
    
    for i in range(len(plats)):
        plats[i].draw()
                   
    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()