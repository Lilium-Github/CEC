from operator import truediv
from pickle import REDUCE
import pygame
import random

pygame.init()
pygame.display.set_caption("Wires")
screen = pygame.display.set_mode((800,800))
screen.fill((0,0,0))

COLOR1 = (random.randint(0,250),random.randint(0,250),random.randint(0,250))
COLOR2 = (random.randint(0,250),random.randint(0,250),random.randint(0,250))
COLOR3 = (random.randint(0,250),random.randint(0,250),random.randint(0,250))
COLOR4 = (random.randint(0,250),random.randint(0,250),random.randint(0,250))

BoxList = []

LeftPositions = [(100,100),(100, 300),(100, 500),(100, 700)]
RightPositions = [(550,100),(550, 300),(550, 500),(550, 700)]

LeftColors = [COLOR1, COLOR2, COLOR3, COLOR4]
RightColors = [COLOR1, COLOR2, COLOR3, COLOR4]

listsList = [LeftPositions, RightPositions, LeftColors, RightColors]

for i, val in enumerate(listsList):
    random.shuffle(val)

mouseDown = False
mousePos = (0,0)

def coll(xpos, ypos, mouseX, mouseY):
    if (mouseX < xpos + 100 and mouseX > xpos) and (mouseY < ypos + 50 and mouseY > ypos):
        return True
    return False

class Box():
    def __init__(self, pos, rgb):
        self.pos = pos
        self.rgb = rgb

        self.connected = False
        #self.draw = False
        self.hovering = False

    def isHovering(self, mouse):
        if coll(self.pos[0], self.pos[1], mouse[0], mouse[1]):
            self.hovering = True
        else:
            self.hovering = False

    def draw(self):
        pygame.draw.rect(screen, self.rgb, (self.pos[0], self.pos[1], 100, 50))
        if self.hovering:
            pygame.draw.rect(screen, (255,255,255), (self.pos[0], self.pos[1], 100, 50), 5)
        
for i in range(4):
    BoxList.append(Box(LeftPositions[i], LeftColors[i]))
    BoxList.append(Box(RightPositions[i], RightColors[i]))

while True:
    #------------------- EVENTS -------------------
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.MOUSEBUTTONDOWN:
        mouseDown = True
    elif event.type == pygame.MOUSEBUTTONUP:
        mouseDown = False
    elif event.type == pygame.MOUSEMOTION:
        mousePos = event.pos

    #------------------- UPDATE -------------------
    for num, box in enumerate(BoxList):
        box.isHovering(mousePos)

    #------------------- RENDER -------------------
    screen.fill((0,0,0))

    for num, box in enumerate(BoxList):
        box.draw()

    pygame.display.flip()
    
pygame.quit()