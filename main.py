import pygame
from pygame.locals import *
import settings
import sprites
from time import sleep
import os, random
from voice_detection import VoiceCapture
from voice_recorder import SoundRecord
from HMM_Model import HMMTrainer
import warnings
warnings.filterwarnings("ignore")

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
        # self.screen.blit(self.background_penalty, (0,0))
        self.playing = True
        while self.playing:
            self.clock.tick(settings.FPS)
            self.events()
            # self.update_sprites('Goal')
            # self.draw_sprites()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                self.draw_sprites()
            else:
                word = self.get_random_word()
                if event.type == pygame.KEYDOWN and event.key == K_SPACE:                  
                    
                    sound_path = SoundRecord().record_sound()
                    action = self.evaluate_sound(sound_path, word)
                    
                    kick = pygame.mixer.Sound(os.path.join(settings.BASE_PATH, 'sound_effects', 'kick.wav'))
                    pygame.mixer.Sound.play(kick)

                    size = 10
                    if action == 'Defense':
                        size = 11
                    
                    for i in range(size):
                        self.update_sprites(action)
                        sleep(0.1)
                        self.draw_sprites()

                    if action == 'Goal':
                        pygame.mixer.Sound.play(pygame.mixer.Sound(os.path.join(settings.BASE_PATH, 'sound_effects', 'Goal.wav')), maxtime=2000)
                    elif action == 'Defense':
                        pygame.mixer.Sound.play(kick)

                    sleep(2)
                    self.update_sprites('Start')
                    self.draw_sprites()
                else:
                    self.draw_sprites(show_word=True, word=word)
    
    def update_sprites(self, action):
        self.all_sprites.update(action)
        self.soccer_ball.update(action)

    def draw_sprites(self, show_word=False, word=None):
        self.screen.blit(self.background_penalty, (0,0))
        self.all_sprites.draw(self.screen)
        self.soccer_ball.draw()
        if show_word:
            self.show_text('PRONUNCIE A PALAVRA ' + word , 40, settings.YELLOW, settings.LENGTH/2,70)
            self.show_text('aperte barra de espaço para falar ' , 24, settings.YELLOW, settings.LENGTH/2,110)
        pygame.display.flip()

    def get_random_word(self):
        words_list = ['ENXERGAR', 'MORTADELA', 'RETRÓGRADO', 'BRINCADEIRAS', 'CÉREBRO']
        return random.choice(words_list)
    
    def evaluate_sound(self, sound_path, word):
        hmm_class = HMMTrainer()
        score = hmm_class.get_score(r"audios\apple", sound_path)
        print(score)
        if str(score)[-1] in ('0', '1', '2', '3'):
            return 'Goal'
        elif str(score)[-1] in ('4', '5', '6'):
            return 'Defense'
        else:
            return 'Out'


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
                if event.type == pygame.KEYDOWN:
                    waiting = False

    def game_over_screen(self):
        pass

g = SoccerGame()
g.start_screen()

while g.running:
    g.new_game()
    g.game_over_screen()