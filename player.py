import pygame as pg
from common_defined import *
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0, 0)  # velocity
        self.acc = vec(0, 0)  # acceleration

    def jump(self):
        self.rect.x += 1
        hit = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hit:
            self.vel.y = -PC_JUMP

    def update(self):
        self.acc = vec(0, PC_GRAVITY)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -PC_ACC
        if keys[pg.K_d]:
            self.acc.x = PC_ACC

        # apply friction
        self.acc.x += self.vel.x * PC_FRICTION
        # physics - motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        #  stay on screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos
