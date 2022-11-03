# Import pygame to produce the engine as well as using random
from xml.etree.ElementPath import get_parent_map
import pygame as pg
from pygame.sprite import Sprite
import random

import os

# Setup Asset folders

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")

# Creates the settings

WIDTH = 360
HEIGHT = 480
FPS = 30

# Creates the colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pg.sprite.Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN)
        # self.image =pg.image.load(os.path.join(img_folder, "Bellarmine_Logo.jpg")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.xVel = 5
        self.yVel = 5
    def update(self):
        self.rect.x += self.xVel
        self.rect.y += self.yVel
        if self.rect.x < 0:
            self.xVel = 5
        if self.rect.y < 0:
            self.yVel = 5
        if self.rect.x + 50 > WIDTH:
            self.xVel = -5
        if self.rect.x > WIDTH:
            self.rect.x = 5
        if self.rect.y + 50 > HEIGHT:
            self.rect.y = 5

#Intializing pygame and a window

pg.init()
pg.mixer.init
screen = pg.display.set_mode((WIDTH, HEIGHT,))
pg.display.set_caption("My Game")
clock = pg.time.Clock()

# Create a group for all sprites

all_sprites = pg.sprite.Group()

# Will instantiate the Player

player = Player()

# Add the player to the sprites group

all_sprites.add(player)

# Insert the game loop
running = True
while running:
    # Keeps the loop running
    clock.tick(FPS)
    
    for event in pg.event.get():
        # Check if hte window is closed
        if event.type == pg.QUIT:
            running = False

####### Update ##############
# Updates all spirtes 
all_sprites.update()


####### Draw ################
# Draws the screen

screen.fill(GREEN)

# Draws the sprites

all_sprites.draw(screen)

# Buffer : It will flip the display once eveything is drawn.
pg.display.flip()

pg.quit()
