# import pygame as pg
import random
# from common_defined import *
from player import *
from game_platform import *
from os import path


class Game:
    def __init__(self):
        # Initialize Screen, Sound, Title, etc
        pg.init()
        pg.mixer.init()
        pg.display.set_caption(TITLE)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.is_running = True
        self.font_family = pg.font.match_font(FONT_FAMILY)
        self.load_data()

    def load_data(self):
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, HS), 'r+') as f:
            try:
                self.high_score = int(f.read())
            except:
                self.high_score = 0

    def new(self):
        # Start/Reset Game Loop
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.pc = Player(self)  # pc => player, playable character
        self.all_sprites.add(self.pc)
        for platform in PLATFORM_LIST:
            p = Platform(*platform)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        # Game Loop
        self.is_playing = True
        while self.is_playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Update Game Loop
        self.all_sprites.update()

        if self.pc.vel.y > 0:
            hit = pg.sprite.spritecollide(self.pc, self.platforms, False)
            if hit:
                self.pc.pos.y = hit[0].rect.top
                self.pc.vel.y = 0

        # Scroll Window and Delete Platforms
        if self.pc.rect.top <= HEIGHT/4:
            self.pc.pos.y += abs(self.pc.vel.y)
            for platform in self.platforms:
                platform.rect.y += abs(self.pc.vel.y)
                if platform.rect.top >= HEIGHT:
                    platform.kill()
                    self.score += 2

        # End Game
        if self.pc.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.pc.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
                if len(self.platforms) == 0:
                    self.is_playing = False

        # Spawn Platforms
        while len(self.platforms) < 5:
            width = random.randrange(45, 85)
            p = Platform(random.randrange(0, WIDTH-width),
                         random.randrange(-75, -30),
                         100, 20)
            self.platforms.add(p)
            self.all_sprites.add(p)

    def events(self):
        # Game Loop Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.is_playing:
                    self.is_playing = False
                self.is_running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.pc.jump()

    def draw(self):
        # Game Loop Draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 22, RED, 240, 10)
        pg.display.flip()

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_family, size)
        txt_surface = font.render(text, True, color)
        txt_rect = txt_surface.get_rect()
        txt_rect.midtop = (x, y)
        self.screen.blit(txt_surface, txt_rect)

    def wait_key_press(self):
        is_waiting = True
        while is_waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    is_waiting = False
                    self.is_running = False
                if event.type == pg.KEYUP:
                    is_waiting = False

    def show_start_scr(self):
        self.screen.fill(BG_COLOR)
        self.draw_text(TITLE, 48, WHITE, WIDTH/2, HEIGHT/4)
        self.draw_text("High Score: " + str(self.high_score), 22, WHITE, WIDTH / 2, 15)
        self.draw_text("MOVEMENT: (LEFT - A; RIGHT - D; JUMP - SPACE)", 20, WHITE, WIDTH/2, HEIGHT/2)
        self.draw_text("Press any key to play", 18, WHITE, WIDTH/2, HEIGHT*3/4)
        pg.display.flip()
        self.wait_key_press()

    def show_game_over_scr(self):
        if not self.is_running:
            return
        self.screen.fill(BG_COLOR)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("SCORE: "+str(self.score), 20, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press any key to play", 18, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        if self.score > self.high_score:
            self.high_score = self.score
            self.draw_text(">>>NEW HIGH SCORE<<<", 22, WHITE, WIDTH/2, HEIGHT/2+40)
            with open(path.join(self.dir, HS), 'w') as f:
                f.write(str(self.high_score))
        else:
            self.draw_text("High Score: " + str(self.high_score), 22, WHITE, WIDTH / 2, 15)
        pg.display.flip()
        self.wait_key_press()


game = Game()
game.show_start_scr()
while game.is_running:
    game.new()
    game.show_game_over_scr()

pg.quit()
