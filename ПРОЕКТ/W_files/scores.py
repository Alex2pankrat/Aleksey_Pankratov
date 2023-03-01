import pygame.font


class Scores:
    '''вывод игровой информации'''
    def __init__(self, screen, stats):
        '''инициализируем подсчёт очков'''
        self.score_rect = None
        self.score_img = None
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('', 40)
        self.image_score()
        self.image_high_score()
        # self.image_guns()

    def image_score(self):
        '''преобразовывает текст счёта в графическое изображение'''
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (16, 20, 25))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.score_rect.right + 40
        self.score_rect.top = 15

    def image_high_score(self):
        '''Преобразует рекорд в графическое изображение'''
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (16, 20, 25))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx + 330
        self.high_score_rect.top = self.screen_rect.top + 20


    def show_score(self):
        '''вывод счёта на экран'''
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)