"""Project: Level 3 Programming Asessment.

Author: Isaac Smith
School: Hauraki Plains College
Date: 03/06/2024
"""

# Imports
import pygame

#Initialize
pygame.init()
WINDOW = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Dance Dance Dance: Zombie Apocalypsse")
CLOCK = pygame.time.Clock()

#Variables
FRAME_RATE = 60 

background = pygame.image.load('images/DDDZA-Background.png')
background = pygame.transform.scale_by(background, 5)

#Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    WINDOW.blit(background, (0,0))
    
    CLOCK.tick(FRAME_RATE)
    pygame.display.update()