import pygame
from pygame.locals import *
import settings

class Goalkeeper(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet):
        pygame.sprite.Sprite.__init__(self)
        self.goalkeeper_images = []
        for i in range(3):
            img = sprite_sheet.subsurface((i * 300,0), (300,280))
            img = pygame.transform.scale(img, (300//1.5, 280//1.5))
            self.goalkeeper_images.append(img)

        self.list_index = 0
        self.image = self.goalkeeper_images[self.list_index]
        self.rect = self.image.get_rect()
        self.x_goalkeeper = 450
        self.y_goalkeeper = 350
        self.rect.center = (self.x_goalkeeper,self.y_goalkeeper)

    def update(self):
        if self.list_index > 2:
            self.list_index = 0
            self.x_goalkeeper = 420
            # self.y_goalkeeper = 350
        self.list_index += 0.2
        self.x_goalkeeper += 15
        # self.y_goalkeeper -= 15
        self.rect.center = (self.x_goalkeeper,self.y_goalkeeper)
        self.image = self.goalkeeper_images[int(self.list_index)]

class Ball():
    def __init__(self, soccer_ball_image, screen):
        self.soccer_ball_image = soccer_ball_image
        self.division_factor = 7
        self.image = pygame.transform.scale(soccer_ball_image, (600//self.division_factor, 600//self.division_factor))
        self.x_ball = 450
        self.y_ball = 550
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_ball, self.y_ball)
        self.list_index = 0
        self.screen = screen
    
    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        if self.list_index > 2:
            self.list_index = 0
            self.division_factor = 7
            self.image = pygame.transform.scale(self.soccer_ball_image, (600//self.division_factor, 600//self.division_factor))
            self.x_ball = 450
            self.y_ball = 550
        self.list_index += 0.2
        self.division_factor += 0.4
        self.x_ball -= 15
        self.y_ball -= 15
        self.image = pygame.transform.scale(self.soccer_ball_image, (600//self.division_factor, 600//self.division_factor))
        self.rect.center = (self.x_ball, self.y_ball)