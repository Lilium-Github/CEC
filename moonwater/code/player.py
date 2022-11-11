import pygame
from settings import *
from support import *
from timer import Timer

class Player(pygame.sprite.Sprite): #this is a child class of pygame's sprite class
    def __init__(self, pos, group):
        super().__init__(group) # gives the Player class access to the functions inside the Group class

        #sprite stuff
        self.import_assets()
        self.status = 'down_idle'
        self.frame_index = 0

        #general setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)


        #movement stuff!
        self.direction = pygame.math.Vector2() # a vector, in python, is like a more mathy list
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

        #timers
        self.timers = {
            "tool use": Timer(350, self.use_tool)
        }

        #tools
        self.selected_tool = "axe"

    def use_tool(self):
        print(self.selected_tool)

    def import_assets(self):
        self.animations = {'up':[], 'down':[], 'left':[], 'right':[],
                           'up_idle':[], 'down_idle':[], 'left_idle':[], 'right_idle':[], 
                           'up_hoe':[], 'down_hoe':[], 'left_hoe':[], 'right_hoe':[],
                           'up_axe':[], 'down_axe':[], 'left_axe':[], 'right_axe':[],
                           'up_water':[], 'down_water':[], 'left_water':[], 'right_water':[]
        }

        for animation in self.animations.keys():
            full_path = 'moonwater/graphics/character/' + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self, dt): #guess what this does
        self.frame_index += 4*dt

        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]

    def playerInput(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.timers["tool use"].activate()
            self.direction = pygame.math.Vector2()
            self.frame_index = 0

        if not self.timers['tool use'].active:

            if keys[pygame.K_UP]:
                self.direction.y = -1
                self.status = "up"
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status = "down"
            else: self.direction.y = 0

            if keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = "left"
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status = "right"
            else: self.direction.x = 0

            if keys[pygame.K_1]:
                self.selected_tool = "axe"
            elif keys[pygame.K_2]:
                self.selected_tool = "hoe"
            elif keys[pygame.K_3]:
                self.selected_tool = "water"

    def get_status(self):
        if self.direction.magnitude() == 0:
            self.status = self.status.split("_")[0] + "_idle"

            if self.timers['tool use'].active:
                print("tool being used")
                self.status = self.status.split("_")[0] + "_" + self.selected_tool

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()
            

    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

    def update(self, dt):
        self.playerInput()
        self.get_status()
        self.move(dt)
        self.animate(dt)
        self.update_timers()

