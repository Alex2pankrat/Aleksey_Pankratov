import pygame
from pythonProject.ПРОЕКТ.W_files import controls
from pythonProject.ПРОЕКТ.W_files.gun import Gun
from pygame.sprite import Group
from stats import Stats
from pythonProject.ПРОЕКТ.W_files.scores import Scores


def run():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("Space War")
    bg_color = (16, 20, 25)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos, imag=pygame.image.load('../Images/enemyBlack1.png'))
    stats = Stats()
    sc = Scores(screen, stats)
    clock = pygame.time.Clock()
    im = pygame.image.load('../Images/image.psd.jpg')
    im = pygame.transform.scale(im, (1000, 800))

    while True:
        controls.events(screen, gun, bullets, inos)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, inos, bullets, im)
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, sc, gun, inos, bullets)
            clock.tick(120)


run()
