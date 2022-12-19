import pygame
from pygame.locals import *
import settings

class Goalkeeper(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet):
        pygame.sprite.Sprite.__init__(self)
        self.goalkeeper_images_goal = []
        for i in range(3):
            img = sprite_sheet.subsurface((i * 300,0), (300,280))
            img = pygame.transform.scale(img, (300//1.5, 280//1.5))
            self.goalkeeper_images_goal.append(img)
        
        self.goalkeeper_images_defense = []
        for i in range(3):
            img = sprite_sheet.subsurface((i * 300,0), (300,280))
            img = pygame.transform.scale(img, (300//1.5, 280//1.5))
            self.goalkeeper_images_defense.append(img)

        self.goalkeeper_images_out = []
        for i in range(3):
            img = sprite_sheet.subsurface((i * 300,0), (300,280))
            img = pygame.transform.scale(img, (300//1.5, 280//1.5))
            self.goalkeeper_images_out.append(img)
        self.list_index = 0
        self.image = self.goalkeeper_images_goal[self.list_index]
        self.rect = self.image.get_rect()
        self.x_goalkeeper = 450
        self.y_goalkeeper = 350
        self.rect.center = (self.x_goalkeeper,self.y_goalkeeper)
        self.font = settings.FONT

    def update(self, action: str):
        if self.list_index > 2:
            self.list_index = 0
            self.x_goalkeeper = 420
            self.y_goalkeeper = 350
            self.rect.center = (self.x_goalkeeper,self.y_goalkeeper)

        self.list_index += 0.2

        if action == 'Goal':
            self.x_goalkeeper += 15
            # self.y_goalkeeper -= 15
            self.rect.center = (self.x_goalkeeper,self.y_goalkeeper)
            self.image = self.goalkeeper_images_goal[int(self.list_index)]
        
        if action == 'Defense':
            self.x_goalkeeper += 15
            # self.y_goalkeeper -= 15
            self.rect.center = (self.x_goalkeeper,self.y_goalkeeper)
            self.image = self.goalkeeper_images_defense[int(self.list_index)]

        if action == 'Out':
            self.x_goalkeeper += 15
            # self.y_goalkeeper -= 15
            self.rect.center = (self.x_goalkeeper,self.y_goalkeeper)
            self.image = self.goalkeeper_images_out[int(self.list_index)]

        if action == 'Start':
            self.list_index = 0
            self.image = self.goalkeeper_images_goal[self.list_index]
            self.x_goalkeeper = 420
            self.y_goalkeeper = 350
            self.rect.center = (self.x_goalkeeper,self.y_goalkeeper)
            

    def show_text(self, text: str, size: int, collor, x: int, y: int):
        font = pygame.font.Font(self.font, size)
        text = font.render(text, True, collor)
        text_rect = text.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text, text_rect)

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
        self.font = settings.FONT
    
    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, action: str):
        if self.list_index > 2:
            self.list_index = 0
            self.division_factor = 7
            self.image = pygame.transform.scale(self.soccer_ball_image, (600//self.division_factor, 600//self.division_factor))
            self.x_ball = 450
            self.y_ball = 550
            self.rect.center = (self.x_ball, self.y_ball)

            if action == 'Goal':
                self.goal_icon = pygame.image.load('images\goal_icon.png').convert_alpha()
                self.screen.blit(self.image, (settings.LENGTH/2, 320))
            if action == 'Defense':
                self.defense_icon = pygame.image.load('images\out_icon.png').convert_alpha()
                self.screen.blit(self.image, (settings.LENGTH/2, 320))
            if action == 'Out':
                self.out_icon = pygame.image.load('images\out_icon.png').convert_alpha()
                self.screen.blit(self.image, (settings.LENGTH/2, 320))
            pygame.display.flip()

        self.list_index += 0.2

        if action == 'Goal':
            self.division_factor += 0.4
            self.x_ball -= 15
            self.y_ball -= 10
            self.image = pygame.transform.scale(self.soccer_ball_image, (600//self.division_factor, 600//self.division_factor))
            self.rect.center = (self.x_ball, self.y_ball)

        if action == 'Defense':
            self.division_factor += 0.4
            self.x_ball += 20
            self.y_ball -= 10
            self.image = pygame.transform.scale(self.soccer_ball_image, (600//self.division_factor, 600//self.division_factor))
            self.rect.center = (self.x_ball, self.y_ball)

        if action == 'Out':
            self.division_factor += 0.7
            self.x_ball -= 55
            self.y_ball -= 45
            self.image = pygame.transform.scale(self.soccer_ball_image, (600//self.division_factor, 600//self.division_factor))
            self.rect.center = (self.x_ball, self.y_ball)

        if action == 'Start':
            self.list_index = 0
            self.division_factor = 7
            self.x_ball = 450
            self.y_ball = 550
            self.image = pygame.transform.scale(self.soccer_ball_image, (600//self.division_factor, 600//self.division_factor))
            self.rect.center = (self.x_ball, self.y_ball)
