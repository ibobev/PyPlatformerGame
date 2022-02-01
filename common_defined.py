# import pygame
import os
main_folder = os.path.dirname(__file__)
sprites_folder = os.path.join(main_folder, "sprites")

HS = "hs.txt"

# Screen Size
WIDTH = 480
HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (160, 160, 160)

BG_COLOR = GREY

# Title string
TITLE = "Platform3r"

# Font
FONT_FAMILY = 'arial'

# all_sprites = pygame.sprite.Group()
# enemy_sprites = pygame.sprite.Group()

# Physics
PC_ACC = 0.5
PC_FRICTION = -0.12
PC_GRAVITY = 0.7
PC_JUMP = 22

# Platform
PLATFORM_LIST = [(0, HEIGHT-40, WIDTH, 40),
                 (125, 440, 100, 20),
                 (350, 160, 100, 20),
                 (290, 330, 100, 20),
                 (75, 200, 100, 20)]
