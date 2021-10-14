import pygame
from math import sin #this is so we don't have to say "math." in front of sin()
from math import cos

pygame.init()

gamescreen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Wave Beam")
clocky = pygame.time.Clock()
PlayingGame = True #variable used to quit game loop

#variables to control wave beam
beam = False
beamx1 = 0
beamy1 = 0
angle1 = 0
beamx2 = 0
beamy2 = 0
angle2 = 0
beamx3 = 0
beamy3 = 0
angle3 = 0
A1 = 60
B1 = .2
C1 = 0
D1 = 0
A2 = 50
B2 = .3
C2 = 0
D2 = 0
A3 = 70
B3 = .4
C3 = 0
D3 = 0

go = "down"

#BEGIN GAME LOOP#################################################################
while PlayingGame:
  
  clocky.tick(60)
  
  events = pygame.event.get()
 
  for event in events:
    if event.type == pygame.QUIT:
      PlayingGame = False

  #fire wave beam
  beam = True
        
  #PHYSICS SECTION-------------------------------------------------------------
  if beam is True:
      angle1 += 1 #rotate angle
      beamx1 = A1*cos(B1*(angle1-C1))+D1 #this handles how fast the beam moves to the right
      beamy1 = A1*sin(B1*(angle1-C1))+D1 #this handles the shape and size of the wave
      
      angle2 += 1
      beamx2 = A2*cos(B2*(angle2-C2))+D2 #this handles how fast the beam moves to the right
      beamy2 = A2*sin(B2*(angle2-C2))+D2
      
      angle3 += 1 #rotate angle
      beamx3 = A3*cos(B3*(angle3-C3))+D3 #this handles how fast the beam moves to the right
      beamy3 = A3*sin(B3*(angle3-C3))+D3 #this handles the shape and size of the wave
  else:
      angle = 0
        
  
  #RENDER SECTION-------------------------------------------------------------      
  #gamescreen.fill((0,0,0))
  
  #draw beam when fired
  if beam is True:
      
      #pygame.draw.circle(gamescreen, (200, 0, 100), (beamx1 + 350, beamy1+250), 5)
      #pygame.draw.circle(gamescreen, (0, 200, 200), (beamx2 + beamx1 + 350, beamy2 + beamy1 + 250), 5)
      pygame.draw.circle(gamescreen, (0, 200, 200), (beamx3 + beamx2 + beamx1 + 350, beamy3 + beamy2 + beamy1 + 250), 5)
  pygame.display.flip()




  #END GAME LOOP#################################################################
pygame.quit()
        

