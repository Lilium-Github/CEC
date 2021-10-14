import pygame
from math import sin #this is so we don't have to say "math." in front of sin()

pygame.init()

gamescreen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Wave Beam")
clocky = pygame.time.Clock()
PlayingGame = True #variable used to quit game loop

#player position
xpos = 50
ypos = 75
#player speed
vx = 0
vy = 0
#variables to control wave beam
beam = False
beamx1 = 0
beamy1 = 0
angle1 = 0
beamx2 = 0
beamy2 = 0
angle2 = 0
A1 = 10
B1 = .2
C1 = 0
D1 = 0
A2 = 60
B2 = .3
C2 = 0
D2 = 0

#ship image load
ship = pygame.image.load("ship.png") #artwork credit: Mr. Mo
shipRect = ship.get_rect(topleft = (xpos, ypos))

gamescreen.fill((255,255,255))

#BEGIN GAME LOOP#################################################################
while PlayingGame:
  
  clocky.tick(60)
  
  events = pygame.event.get()
 
  for event in events:
    if event.type == pygame.QUIT:
      PlayingGame = False
      
  keys = pygame.key.get_pressed()
      
        
  if keys[pygame.K_LEFT]:
      vx=-5
  elif keys[pygame.K_RIGHT]:
      vx=5
  else:
      vx = 0

  if keys[pygame.K_DOWN]:
      vy =5
  elif keys[pygame.K_UP]:
      vy=-5
  else:
      vy=0

  #fire wave beam
  if keys[pygame.K_SPACE]:
      beam = True
  else:
      beam = False
        
  #PHYSICS SECTION-------------------------------------------------------------
  if beam is True:
      angle1 += 1 #rotate angle
      beamx1 = xpos+angle1*5 #this handles how fast the beam moves to the right
      beamy1 = A1*sin(B1*(angle1-C1))+D1 #this handles the shape and size of the wave
      
      angle2 += 1
      beamx2 = xpos+angle2*5 #this handles how fast the beam moves to the right
      beamy2 = A2*sin(B2*(angle2-C2))+D2
  else:
      angle = 0
        
  #update player position by adding velocity to position      
  xpos += vx
  ypos += vy
  shipRect = ship.get_rect(topleft = (xpos, ypos))
  
  
  #RENDER SECTION-------------------------------------------------------------      
  #gamescreen.fill((0,0,0))
  
  #draw spaceship
  gamescreen.blit(ship, shipRect)
  
  #draw beam when fired
  if beam is True:
      pygame.draw.circle(gamescreen, (200, 0, 100), (beamx1+10, beamy1+ypos+20), 4)
      pygame.draw.circle(gamescreen, (0, 200, 200), (beamx2+10, beamy2+ypos+20), 4)
      
  pygame.display.flip()




  #END GAME LOOP#################################################################
pygame.quit()
        
