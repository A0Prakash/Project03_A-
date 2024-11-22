import numpy as np
from map import Map
import pygame
import cv2
import os

pygame.init()

name = "2024n1"
w = 649*2
h = 319*2
#1041 307

arr = np.zeros((59,29))

m2024 = Map("images/n2024.png", "Crescendo", None)

screen = pygame.display.set_mode((w,h))
imp = pygame.image.load(m2024.get_image()).convert()

isPressed = False
draw = True
run = True
screen.blit(imp, (0, 0))
while run:
    #screen.fill((0,0,0))
    #screen.blit(imp, (0, 0))
    keys=pygame.key.get_pressed()
    if keys[pygame.K_z] == True:
        draw = not draw
    elif keys[pygame.K_c] == True:
        screen.fill((0,0,0))
        screen.blit(imp, (0, 0))
        arr = np.zeros((59,29))
    elif keys[pygame.K_s] == True:
        np.save("arrays/" + name, arr)
        print("saved")
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            isPressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            isPressed = False
        elif event.type == pygame.MOUSEMOTION and isPressed == True and draw == True:         
            (x, y) = pygame.mouse.get_pos()
            x = int(x/22)
            y = int(y/22)
            pygame.draw.rect(screen, (0, 0, 0),
                 [22*x, 22*y, 22, 22], 0)
            
            arr[(x,y)] = 1
        elif event.type == pygame.MOUSEMOTION and isPressed == True and draw == False:         
            (x, y) = pygame.mouse.get_pos()
            x = int(x/22)
            y = int(y/22)
            pygame.draw.rect(screen, (255, 255, 255),
                 [22*x, 22*y, 22, 22], 0)
            
            arr[(x,y)] = 0
        
            
                
            
            
    pygame.display.update()
            
pygame.quit()
