import pygame
from pygame.locals import *
import settings
import sprites


class SoccerGame:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((settings.LENGTH, settings.WIDTH))
        pygame.display.set_caption(settings.GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.match_font(settings.FONT)
        self.load_files()

    def new_game(self):
        self.all_sprites = pygame.sprite.Group()
        self.goalkeeper = sprites.Goalkeeper(self.sprite_sheet)
        self.all_sprites.add(self.goalkeeper)
        self.soccer_ball = sprites.Ball(self.soccer_ball_image, self.screen)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(settings.FPS)
            self.events()
            self.update_sprites()
            self.draw_sprites()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
    
    def update_sprites(self):
        self.all_sprites.update()

    def draw_sprites(self):
        self.screen.blit(self.background_penalty, (0,0))
        self.all_sprites.draw(self.screen)
        self.soccer_ball.update()
        self.soccer_ball.draw()
        pygame.display.flip()

    def load_files(self):
        self.background_penalty = pygame.image.load('images\soccer_penalty_background.jpg').convert()
        self.background_penalty = pygame.transform.scale(self.background_penalty, (settings.LENGTH, settings.WIDTH))
        self.background_stadium = pygame.image.load('images\soccer_stadium_background.jpg').convert()
        self.background_stadium = pygame.transform.scale(self.background_stadium, (settings.LENGTH, settings.WIDTH))
        self.logo = pygame.image.load('images\soccer_logo.png').convert_alpha()
        self.sprite_sheet = pygame.image.load('images\sprite_sheet_goalkeeper-PhotoRoom.png').convert_alpha()
        self.soccer_ball_image = pygame.image.load('images\soccer_ball.png').convert_alpha()
        # self.logo = pygame.transform.scale(self.logo, (settings.LENGTH, settings.WIDTH))

    def show_text(self, text: str, size: int, collor, x: int, y: int):
        font = pygame.font.Font(self.font, size)
        text = font.render(text, True, collor)
        text_rect = text.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text, text_rect)

    def show_start_logo(self, x, y):
        start_logo_rect = self.logo.get_rect()
        start_logo_rect.midtop = (x, y)
        self.screen.blit(self.logo, start_logo_rect)

    def start_screen(self):
        self.screen.blit(self.background_stadium, (0,0))
        self.show_start_logo(settings.LENGTH/2, 20)
        self.show_text(
            'Pressione uma tecla para jogar',
            32,
            settings.YELLOW,
            settings.LENGTH/2,
            320
        )
        self.show_text(
            'Developed by Frederico Lisbôa, Antonny Victor and Bernardo Oliveira',
            20,
            settings.WHITE,
            settings.LENGTH/2,
            570
        )
        pygame.display.flip()
        self.wait_for_player()

    def wait_for_player(self):
        waiting = True
        while waiting:
            self.clock.tick(settings.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYUP:
                    waiting = False

    def game_over_screen(self):
        pass

g = SoccerGame()
g.start_screen()

while g.running:
    g.new_game()
    g.game_over_screen()