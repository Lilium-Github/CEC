import random
import pygame
pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Ant-Based Pretest")

clock = pygame.time.Clock()

Gameloop = True

screen.fill((200,200,200))

class ant:
    def __init__(self, isQueen):
        self.x = random.randint(0,400)
        self.y = random.randint(0,400)

        coin = random.randint(1,2)
        if coin == 1:
            self.color = "red"
        else:
            self.color = "black"

        self.isQueen = isQueen\

    def print(self):
        print("I'm a", self.color, "ant. My x is", self.x, "and my y is", self.y)
        
        if self.isQueen:
            print("I'm a queen.")

    def woof(self):
        print("Bark.")

    def move(self):
        movement = random.randint(-5, 5)
        direction = random. randint(1, 2)

        if direction == 1:
            self.x = self.x + movement
        else:
            self.y = self.y + movement

anthill = []

for i in range(10):
    anthill.append(ant(False))

while Gameloop:
    clock.tick(5)

    #event logic
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            Gameloop = False
        else:
            Gameloop = True

    #update ants
    for i in range(len(anthill)):
        anthill[i].move()
        anthill[i].print()
        anthill[i].woof()

    #draw ants
    screen.fill((200,200,200))

    for i in range(len(anthill)):
        if anthill[i].color == "red":
            pygame.draw.circle(screen, ((255,0,0)), (anthill[i].x, anthill[i].y), 2)
        else:
            pygame.draw.circle(screen, ((5,0,0)), (anthill[i].x, anthill[i].y), 2)

    pygame.display.flip()

pygame.quit()