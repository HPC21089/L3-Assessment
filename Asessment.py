"""Project: Level 3 Programming Asessment.

Author: Isaac Smith
School: Hauraki Plains College
Date: 03/06/2024
"""

# Imports
import pygame

#Initialize
pygame.init()
window = pygame.display.set_mode(1280, 720)
pygame.display.set_caption("Dance Dance Dance: Zombie Apocalypsse")
clock = pygame.time.Clock()

#Variables
FRAME_RATE = 60 #caps because it is a constant

#Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    clock.tick(FRAME_RATE)
    pygame.display.update()