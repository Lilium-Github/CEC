from re import S
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
LineList = []

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
    def __init__(self, pos, rgb, side):
        self.pos = pos
        self.rgb = rgb
        self.side = side

        self.connected = False
        self.drawing = True
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
    BoxList.append(Box(LeftPositions[i], LeftColors[i], 'l'))
    BoxList.append(Box(RightPositions[i], RightColors[i], 'r'))

class Line:
    def __init__(self, start, end, rgb):
        self.start = start
        self.end = end
        self.rgb = rgb

        self.drawing = False

    def update(self, mouse):
        self.end = self.mouse

    def draw(self):
        pygame.draw.line(screen, self.rgb, self.start, self.end, 4)

for i in range(4):
    startpoint = (LeftPositions[i][0] + 95, LeftPositions[i][1] + 25)
    LineList.append(Line(startpoint, startpoint, LeftColors[i]))

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
        
    lineExist = False
    currLine = "none"

    for num, line in enumerate(LineList):
        if line.drawing:
            lineExist = True
            line.end = mousePos
            currLine = line
        
    if mouseDown and not lineExist:
        for num, box in enumerate(BoxList):
            if box.side == 'l' and box.drawing and coll(box.pos[0], box.pos[1], mousePos[0], mousePos[1]):
                LineList[int(num / 2)].drawing = True

    elif mouseDown and lineExist:
        clickedOnBox = False
        for num, box in enumerate(BoxList):
            if box.side == 'l' and box.drawing and coll(box.pos[0], box.pos[1], mousePos[0], mousePos[1]):
                clickedOnBox = True
                for i, line in enumerate(LineList):
                    if line.drawing:
                        line.drawing = False
                LineList[int(num / 2)].drawing = True
                currLine = LineList[int(num / 2)]
            if box.side == 'r' and box.drawing and coll(box.pos[0], box.pos[1], mousePos[0], mousePos[1]):
                if box.rgb == currLine.rgb:
                    for i, val in enumerate(BoxList):
                        if val.rgb == currLine.rgb:
                            val.drawing = False

                    currLine.drawing = False
                    currLine = "none"

                else:
                    currLine.drawing = False
                    currLine = "none"
                    lineExist = False

    #------------------- RENDER -------------------
    screen.fill((0,0,0))

    for num, box in enumerate(BoxList):
        if box.drawing:
            box.draw()

    for num, line in enumerate(LineList):
        if line.drawing:
            line.draw()

    pygame.display.flip()
    
pygame.quit()
