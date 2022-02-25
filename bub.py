import random
import pygame

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("BubbleGradient")
clock = pygame.time.Clock()


GameLoop = True #variable to run game loop

screen.fill((255,255,255))

myList = []

random.seed

for i in range(200):
    myList.append(random.randint(0,255))

coin = random.randint(1,3)


while GameLoop:
    screen.fill((0,0,0))
    
    clock.tick(15)
    
    # pygame event logic
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            GameLoop = False
        else:
            GameLoop = True
            
    for i in range(len(myList) - 1):
        if myList[i] > myList[i+1]:
            swap = myList[i]
            myList[i] = myList[i+1]
            myList[i+1] = swap
            
            
    for i in range(len(myList)):
        if coin == 1:
            pygame.draw.rect(screen, (150, myList[i], abs(255 - myList[i])), (i*4, 0, 4, 400)) 
        if coin == 2:
            pygame.draw.rect(screen, (myList[i], abs(255 - myList[i]), 150), (i*4, 0, 4, 400))
        if coin == 3:
            pygame.draw.rect(screen, (abs(255 - myList[i]), 150, myList[i]), (i*4, 0, 4, 400))
        
            
            
    pygame.display.flip()        
    
pygame.quit()
