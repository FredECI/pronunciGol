import pygame
from pygame.locals import *
from sys import exit

pygame.init()

length = 900
width = 600 
screen = pygame.display.set_mode((length, width))
pygame.display.set_caption('Soccer Game')

sprite_sheet = pygame.image.load('images\sprite_sheet_goalkeeper-PhotoRoom.png').convert_alpha()

class Goalkeeper(pygame.sprite.Sprite):
    def __init__(self):
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
    def __init__(self):
        self.division_factor = 7
        self.image = pygame.transform.scale(soccer_ball_image, (600//self.division_factor, 600//self.division_factor))
        self.x_ball = 450
        self.y_ball = 550
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_ball, self.y_ball)
        self.list_index = 0
    
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        if self.list_index > 2:
            self.list_index = 0
            self.division_factor = 7
            self.image = pygame.transform.scale(soccer_ball_image, (600//self.division_factor, 600//self.division_factor))
            self.x_ball = 450
            self.y_ball = 550
        self.list_index += 0.2
        self.division_factor += 0.4
        self.x_ball -= 15
        self.y_ball -= 15
        self.image = pygame.transform.scale(soccer_ball_image, (600//self.division_factor, 600//self.division_factor))
        self.rect.center = (self.x_ball, self.y_ball)

class Button():
    def __init__(self):
        

all_sprites = pygame.sprite.Group()
goalkeeper = Goalkeeper()
all_sprites.add(goalkeeper)

clock = pygame.time.Clock()

background_penalty = pygame.image.load('images\soccer_penalty_background.jpg').convert()
background_penalty = pygame.transform.scale(background_penalty, (length, width))

soccer_ball_image = pygame.image.load('images\soccer_ball.png').convert_alpha()

soccer_ball = Ball()

run = True
while run:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN:
            all_sprites.update()
            soccer_ball.update()
        
    screen.blit(background_penalty, (0,0))
    soccer_ball.draw()
    all_sprites.draw(screen)
    # all_sprites.update()

    pygame.display.flip()

pygame.quit()
