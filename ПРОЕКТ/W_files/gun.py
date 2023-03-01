import pygame
from pygame.sprite import Sprite


class Gun(Sprite):

    def __init__(self, screen):
        '''инициализация пушки'''
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('../Images/playerShip1_orange.png')
        self.image = pygame.transform.scale(self.image, (120, 98))   # (160, 130)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery   # fghj
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)   # thjkl
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False

    def output(self):
        '''отрисовка пушки'''
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        '''обновение позиции пушки'''
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 2.0   # 1,5
        if self.mleft and self.rect.left > 0:
            self.center -= 2.0   # 1,5
        if self.mup:
            self.centery -= 2.0   # 1,5

        self.rect.centerx = self.center

    def create_gun(self):
        '''размещает пушку по центру внизу'''
        self.center = self.screen_rect.centerx



