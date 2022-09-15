import random
import pygame

def randomColor():
    return (random.randint(0,225), random.randint(0,225), random.randint(0,225))

pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Liliopolis Skyline")

clock = pygame.time.Clock()

quit = False

screen.fill((200,200,200))

totWidth = 0

while totWidth < 400:

    width = random.randrange(60, 140, 20)

    if width + totWidth > 400:
        width = 400 - totWidth


    height = random.randrange(210, 361, 30)
    left = totWidth
    top = 400 - height

    for i in range(int(height / 20)):
        pygame.draw.rect(screen, randomColor(), (left, top, width, 30))

        window = left
        windowColor = randomColor()
        for j in range(int(width / 20)):
            pygame.draw.rect(screen, windowColor, (window + 3, top + 8, 14, 14))
            window = window + 20
        top = top + 30

    pygame.draw.polygon(screen, randomColor(), ((left, 400 - height), (left + width, 400 - height), (left + int(width / 2), 400 - height - (width / 2))))

    totWidth = totWidth + width

while not quit:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            quit = True
        else:
            quit = False

    pygame.display.flip()

pygame.quit()