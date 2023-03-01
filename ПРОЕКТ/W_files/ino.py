import pygame


class Ino(pygame.sprite.Sprite):
    '''класс одного врага'''

    def __init__(self, screen, image):
        '''инициализируем и задаём начальную позицию'''
        super(Ino, self).__init__()
        self.screen = screen

        self.image = image
        self.image = pygame.transform.scale(self.image, (82, 50))

        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width

        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        '''вывод врага на экран'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''перемещает врагов'''
        self.y += 0.2  # 0.1
        self.rect.y = self.y
