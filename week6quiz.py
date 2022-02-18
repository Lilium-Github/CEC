import pygame

pygame.init


#creates game screen and caption
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("simple base code")

#game variables
doExit = False #variable to quit out of game loop

class Butterfly:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        # wings
        pygame.draw.circle(screen, (240,0,200), (self.x - 50, self.y + 70), 80)
        pygame.draw.circle(screen, (240,0,200), (self.x + 100, self.y + 70), 80)
        pygame.draw.circle(screen, (200,0,240), (self.x - 50, self.y + 200), 80)
        pygame.draw.circle(screen, (200,0,240), (self.x + 100, self.y + 200), 80)
        # body
        pygame.draw.ellipse(screen, (250,250,0),  (self.x, self.y, 60, 300))
        # antennae
        pygame.draw.line(screen, (0,0,0), (self.x + 25, self.y + 5), (self.x + 25 - 50, self.y + 5 - 50), 3)
        pygame.draw.line(screen, (0,0,0), (self.x + 35, self.y + 5), (self.x + 35 + 50, self.y + 5 - 50), 3)
        # scales????????? ripples????????????????????????????
        pygame.draw.arc(screen, (100,100,70), (self.x + 5, self.y + 50, 50, 20), (7 * 3.14)/6, (11 * 3.14)/6, 4)
        pygame.draw.arc(screen, (100,100,70), (self.x + 5, self.y + 80, 50, 20), (7 * 3.14)/6, (11 * 3.14)/6, 4)
        pygame.draw.arc(screen, (100,100,70), (self.x + 5, self.y + 110, 50, 20), (7 * 3.14)/6, (11 * 3.14)/6, 4)
        pygame.draw.arc(screen, (100,100,70), (self.x + 5, self.y + 140, 50, 20), (7 * 3.14)/6, (11 * 3.14)/6, 4)
        pygame.draw.arc(screen, (100,100,70), (self.x + 5, self.y + 170, 50, 20), (7 * 3.14)/6, (11 * 3.14)/6, 4)

#BEGIN GAME LOOP######################################################
while not doExit:
      
    #pygame's way of listening for events (key presses, mouse clicks, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           doExit = True #lets you quit program

    #keyboard input-----------------------------------
  
     
     
    buttfly1 = Butterfly(600, 100)
    buttfly2 = Butterfly(300, 450)
    buttfly3 = Butterfly(900, 450)
    #render section-----------------------------------
    screen.fill((150,150,150))


    buttfly1.draw()
    buttfly2.draw()
    buttfly3.draw()



    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()
