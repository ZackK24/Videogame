# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import random

vec = pg.math.Vector2

# game settings 
WIDTH = 360
HEIGHT = 480
FPS = 30

# player settings
PLAYER_FRIC = -0.2
PLAYER_GRAV = 0.98
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

# Sprites 
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_s]:
            self.acc.y = 5
        if keys[pg.K_w]:
            self.acc.y = -5
    def jump(self):
        hits = pg.sprite.spritecollide(self, all_platforms, False)
        if hits:
            print("I have collided!")
            self.vel.y = -20
    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        #hits = pg.sprite.spritecollide(self, all_platforms, False)
# When it is set at true, then the platform will disappear
       # if hits:
        #    print("I have collided!")
        self.acc.x += self.vel.x * PLAYER_FRIC
        self.acc.y += self.vel.y * PLAYER_FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

class Platform(Sprite):
    def __init__(self, x, y ,w ,h):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Mob(Sprite):
    def __init__(self, x, y, color):
        Mob.__init__(self)
        self.image = pg.Surface((20, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect.width / 2, self.rect.height / 2)
        self.pos = vec(x, y)
        self.vel = vec(random.randint(-8,8),random.randint(-8,8))
        self.acc = vec(0,0)
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.pos = self.vel
        if (self.pos.x + self.rect.width > WIDTH or self.pos.x < 0):
            self.vel.x *= -1
        if (self.pos.y + self.rect.height > HEIGHT or self.pos.y < 0):
            self.vel.y *= -1

# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...")
clock = pg.time.Clock()
  
# create a group for all sprites
all_sprites = pg.sprite.Group()
all_platforms = pg.sprite.Group()
# instantiate the classes
player = Player()
plat = Platform(WIDTH/2, HEIGHT/3, 100, 35)
enemy1 = Mob()

# add instances to groups
all_sprites.add(player)
all_sprites.add(plat)
all_platforms.add(plat)
all_sprites.add(enemy1)

for i in range(8):
    mob = Mob (random.randint(0, WIDTH), random.randint(0, HEIGHT), (random.randint(0,255)))
    all_sprites.add(mob)
    enemy1.add(mob)
# Game loop
running = True
while running:
    # keep the loop running using clock
    clock.tick(FPS)

    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False
    
    ############ Update ##############
    # update all sprites
    hits = pg.sprite.spritecollide(player, all_platforms, False)
if hits:
    print("I have collided with a platform!")
    mobhits = pg.sprite.spritecollide(player, enemy1 , True)
    if mobhits:
        print("I have collided with a mob!")
        print(mobhits[0].color)
    all_sprites.update()

    ############ Draw ################
    # draw the background screen
    screen.fill(BLACK)
    # draw all sprites
    all_sprites.draw(screen)
    #draw_text( "POINTS: " = str(POINTS), 22, WHITE, WIDTH / 2 , HEIGHT / 2)
    # buffer - after drawing everything, flip display
    pg.display.flip()
    
pg.quit()
        draw_text("You Win!", 22, WHITE, WIDTH/ 2, HEIGHT/ 2)
    if POINTS > 9:
        break