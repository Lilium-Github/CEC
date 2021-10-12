import random
import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Chaos Game")

GameLoop = True #variable to run game loop

screen.fill((50,50,50))

# initiating points 
x1 = random.randint(30, 350)
y1 = random.randint(30, 370)
x2 = random.randint(30, 370)
y2 = random.randint(370, 770)
x3 = random.randint(370, 770)
y3 = random.randint(370, 770)
x4 = random.randint(370, 770)
y4 = random.randint(30, 370)
rx = random.randint(30, 770)
ry = random.randint(30, 770)

# ignore this, only comment it back in when you need to test something
# x1 = 200
# y1 = 200
# x2 = 200
# y2 = 600
# x3 = 600
# y3 = 200
# x4 = 600
# y4 = 600
# rx = random.randint(30, 770)
# ry = random.randint(30, 770)

# draw initial points
pygame.draw.circle(screen, (255,255,255), (x1,y1), 2)
pygame.draw.circle(screen, (255,255,255), (x2,y2), 2)
pygame.draw.circle(screen, (255,255,255), (x3,y3), 2)
pygame.draw.circle(screen, (255,255,255), (x4,y4), 2)
pygame.draw.circle(screen, (0,0,0), (rx,ry), 1)

#define midpoint function
def halfway(var1, var2):
    point = (var1+var2)/2
    point = (var2+point)/2 #for a triangle, comment out this line
    return point

# GAME LOOP-----------------------------------------------------------
while GameLoop:
    
    # pygame event logic
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            GameLoop = False
        else:
            GameLoop = True
            
    # rng to choose what point to go to       
    num = random.randint(1,4) # for a triangle, set this to (1,3)
    
    # going to the midpoint of current location + chosen point
    if num == 1:
        rx = halfway(rx,x1)
        ry = halfway(ry,y1)
    if num == 2:
        rx = halfway(rx,x2)
        ry = halfway(ry,y2)
    if num == 3:
        rx = halfway(rx,x3)
        ry = halfway(ry,y3)
    if num == 4:
        rx = halfway(rx,x4)
        ry = halfway(ry,y4)
        
    # render point
    pygame.draw.circle(screen, (random.randint(100, 255), random.randint(100,255), random.randint(100,255)), (rx,ry), 1)
    pygame.display.flip()
#END GAME LOOP---------------------------------------------------------
pygame.quit()
