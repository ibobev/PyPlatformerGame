import pygame
from pygame.locals import *
import sys
# import random
import os
from common_defined import *

pygame.init()
fps_clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)


def event_quit():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


while True:
    # Time Loop and Event Handling
    fps_clock.tick(FPS)
    event_quit()
    # Update
    all_sprites.update()

    # Draw
    screen.fill(BLACK)
    # screen.blit
    all_sprites.draw(screen)

    pygame.display.flip()
