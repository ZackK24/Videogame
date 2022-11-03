'''
Goal: Collect the required amount of gold to win (12)
Rules: Cannot go through walls.
Feedback: Will tell you how much gold you collected as well as any powerups/downs you collect
Freedom: Are able to move on your own and chose whether to use hte powerups.

''' 
#  import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint

vec = pg.math.Vector2

# The settings for the window 
WIDTH = 1000
HEIGHT = 900
FPS = 60

# The game settings for the friciton as well as the starting points/powerups
PLAYER_FRIC = -0.2
PLAYER_GRAV = .98
POINTS = 0
BOOSTS = 0
HINDER = 0
# Defines the colors used for the game
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GOLD = (234, 232, 104)
PURPLE = (128, 0, 128)
ORANGE = (255, 127, 0)
''' 
This will create the method for the text in the game. 
It already gives its font, but other characteristics can be changed depending on how the text is used.
'''
def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)

# The Player Class is placed into the Sprite superclass in which its properties are listed such as color and size.
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((55, 60))
        self.screen = pg.Surface((WIDTH, HEIGHT))
        self.image.fill(BLUE)
        self.screen.fill(BLACK)
        self.rect = self.image.get_rect()
        self.screenrect = self.screen.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.hitx = 0
        self.hity = 0
# Gives the controls for the player on how they can move
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -2.5
        if keys[pg.K_d]:
            self.acc.x = 2.5
        if keys[pg.K_w]:
            self.acc.y = -2.5
        if keys[pg.K_s]:
            self.acc.y = 2.5
# Collision detection when it hits the platforms int the game
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, all_platforms, False)
            if hits:
                self.hitx = hits[0].rect.centerx
                self.hity = hits[0].rect.centery
                xdiff = abs(self.rect.centerx - hits[0].rect.centerx)
                ydiff = abs(self.rect.centery - hits[0].rect.centery)
                self.vel.x = 0
                self.centerx = self.pos.x
                self.hitx = hits[0].rect.centerx
                self.hity = hits[0].rect.centery
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, all_platforms, False)
            if hits:
                xdiff = abs(self.rect.centerx - hits[0].rect.centerx)
                ydiff = abs(self.rect.centery - hits[0].rect.centery)
                if hits[0].rect.centery > self.rect.centery and xdiff < ydiff:
                    self.pos.y = hits[0].rect.top - self.rect.height/2
                if hits[0].rect.centery < self.rect.centery and xdiff < ydiff:
                    self.pos.y = hits[0].rect.bottom + self.rect.height/2
                self.vel.y = 0
                self.centery = self.pos.y
                self.hitx = hits[0].rect.centerx
                self.hity = hits[0].rect.centery
# This will tell that when the player hits the platform, then it will tell that you hsve collided in the terminal
    def jump(self):
        hits = pg.sprite.spritecollide(self, all_platforms, False)
        if hits:
            print("i've collided...")
            self.vel.y = -20
# Gives the updates for the player when it collides with the walls/platforms
    def update(self):
        self.acc = vec(0,0)
        self.controls()
        self.rect.center = self.pos
        fric = 0
        fric = PLAYER_FRIC
        self.acc += self.vel * fric
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.centerx = self.pos.x
        self.collide_with_walls('x')
        self.rect.centery = self.pos.y
        self.collide_with_walls('y')
        self.rect.center = self.pos
        self.hitx = self.hitx
        self.hity = self.hity
        if self.rect.x > WIDTH:
            self.rect.x *= -1
        if self.rect.y > HEIGHT:
            self.rect.y *= -1
        


# Classes the Platforms in the game
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
# This will create the mob sprite and its properties
class Mob(Sprite):
    def __init__(self, x, y, w, h, color):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.color = color
        self.image.fill(GOLD)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.rect.x+=1
        if self.rect.x > WIDTH: 
            self.rect.x *= 0
'''
Creates the slowness and boosts powerup classes and places them into the Sprite Superclass. 
It also creates its properties.
'''
class Boost(Sprite):
    def __init__(self, x, y, w, h, color):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.color = color
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.rect.x+=1
        if self.rect.x > WIDTH: 
            self.rect.x *= -1
class Hinder(Sprite):
        def __init__(self, x, y, w, h, color):
            Sprite.__init__(self)
            self.image = pg.Surface((w,h))
            self.color = color
            self.image.fill(PURPLE)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        def update(self):
            self.rect.x+=1
            if self.rect.right > WIDTH or self.rect.left == 0:
                self.rect.x *= -1
# Creates pygame and the window for it
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Coin Collector!")
clock = pg.time.Clock()
  
# Groups all the sprites in the game
all_sprites = pg.sprite.Group()
all_platforms = pg.sprite.Group()
mobs = pg.sprite.Group()
boosts = pg.sprite.Group()
hinders = pg.sprite.Group()
# This forms the player and platform varaibles into the class
player = Player()
plat = Platform(WIDTH/2, HEIGHT/3, 25, 75)
plat1 = Platform(285, 600, 75 ,75)
plat2 = Platform(800, 725, 40, 70)
plat3 = Platform(500, 700, 150, 60)
plat4 = Platform(100, 800, 75, 200)
plat5 = Platform(500, 150, 60, 60)
plat6 = Platform(100, 200, 80, 200)
plat7 = Platform(600, 350, 300, 40)


# adds the sprites into the groups
all_sprites.add(player)
all_sprites.add(plat)
all_sprites.add(plat1)
all_sprites.add(plat2)
all_sprites.add(plat3)
all_sprites.add(plat4)
all_sprites.add(plat5)
all_sprites.add(plat6)
all_sprites.add(plat7)
all_sprites.add(mobs)
all_platforms.add(plat)
all_platforms.add(plat1)
all_platforms.add(plat2)
all_platforms.add(plat3)
all_platforms.add(plat4)
all_platforms.add(plat5)
all_platforms.add(plat6)
all_platforms.add(plat7)
all_sprites.add(boosts)
all_sprites.add(hinders)


for i in range(20):
    # This will add as many mobs/coins
    m = Mob(randint(0, WIDTH), randint(0,HEIGHT), 25, 25, (randint(0,255), randint(0,255) , randint(0,255)))
    all_sprites.add(m)
    mobs.add(m)
print(mobs)
# This will add 2 boosts and 2 hinders/slowness powerups into the game which will be randomly placed.
for i in range(2):
     b = Boost(randint(0, WIDTH), randint(0, HEIGHT), 25, 25, (randint(0, 255), randint(0,255), randint(0,255)))
     all_sprites.add(b)
     boosts.add(b)
print(boosts)
for i in range(2):
    h = Hinder(randint(0, WIDTH), randint(0, HEIGHT), 25, 25, (randint(0,255), randint(0, 255), randint(0, 255)))
    all_sprites.add(h)
    hinders.add(h)
print(hinders)
    
# THe loop for the game
running = True
while running:
    dt = clock.tick(FPS)

    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False
    
    ############ Update ##############
    # The collison detection when a player collects the gold
    mobhits = pg.sprite.spritecollide(player, mobs, True)
    if mobhits:
        POINTS += 1
        print(POINTS)
        print("I've Collected a coin!")
        print(mobhits[0].color)
    # This block will make the powerups disappear once the player touches them
    boosthit = pg.sprite.spritecollide(player, boosts, True)
    hinderhit = pg.sprite.spritecollide(player, hinders, True)

    all_sprites.update()
    
    ############ Draw ################
    # draw the background screen

    screen.fill(BLACK)
    # This will give the intial text of the game ("GOLD:")
    all_sprites.draw(screen)
    draw_text("GOLD: " + str(POINTS), 22, WHITE, WIDTH / 2, HEIGHT / 24)
# This will tell that the player has won once they collect 15 gold
    if POINTS >= 15:
        draw_text("You Win! ", 40, WHITE, 500, 700)
        player.vel.x = 0
        player.vel.y = 0
        player.acc.x = 0
        player.acc.y = 0
# Tells the amount of boost or slowness the player gets when the hit the powerup.
    if boosthit:
        BOOSTS += 1
        player.vel.x *= 5
        player.vel.y *= 5
    if hinderhit:
        HINDER += 1
        player.vel.x *= 0.1
        player.vel.y *= 0.1
# It will draw the text according ot what powerup the player picks up
    if BOOSTS == 1:
      draw_text("BOOSTED!", 20, WHITE, 250, 50)
    if BOOSTS == 2:
        draw_text("ULTRA BOOSTED!", 20, WHITE, 250, 50)
    if HINDER == 1:
        draw_text("SLOWED!", 20, WHITE, 250, 100)
    if HINDER == 2:
        draw_text("ULTRA SLOWED!", 20, WHITE, 250, 100)
# buffer - after drawing everything, flip display
    pg.display.flip()