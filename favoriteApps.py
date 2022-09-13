import random
import pygame
pygame.init()
screen = pygame.display.set_mode((400,800))
pygame.display.set_caption("Mo's Phone")

clock = pygame.time.Clock()

Gameloop = True

screen.fill((0,0,0))

class app:
    def __init__(self, color, xpos, ypos):
        self.color = color
        self.xpos = xpos
        self.ypos = ypos

        self.clicks = 0

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.xpos, self.ypos), 50)

appsList = []

for i in range(3):
    for j in range(3):
        appsList.append(app((random.randint(0,255), random.randint(0,255), random.randint(0,255)), 75 + (i * 125), 75 + (j * 125)))

while Gameloop:
    #event logic
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            Gameloop = False
        else:
            Gameloop = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
            for i,j in enumerate(appsList):
                xDist = abs(j.xpos - pos[0])
                yDist = abs(j.ypos - pos[1])

                if (xDist * xDist) + (yDist * yDist) <= 2500:
                    j.clicks = j.clicks + 1

    appsList.sort(key=lambda x: x.clicks, reverse=True)

    #rendering
    screen.fill((0,0,0))

    for i, j in enumerate(appsList):
        j.draw()

        if i < 3:
            pygame.draw.circle(screen, j.color, (75 + (i * 125), 700), 50)

    pygame.display.flip()

pygame.quit()