import pygame, sys
from pythonProject.ПРОЕКТ.W_files.bullet import Bullet
from ino import Ino
import time


imag = pygame.image.load('../Images/enemyBlack1.png')
SPAWNBULLET = pygame.USEREVENT + 1


def events(screen, gun, bullets, inos):
    '''обработка событий'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                pygame.time.set_timer(SPAWNBULLET, 200)

            elif event.key == pygame.K_w:
                gun.mup = True
                ino = Ino(screen, imag)
                inos.add(ino)
        elif event.type == SPAWNBULLET:
            new_bullet = Bullet(screen, gun)
            bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False


def update(bg_color, screen, stats, sc, gun, inos, bullets, im):
    '''обновление экрана'''
    screen.fill(bg_color)

    screen.blit(im, (0, 0))

    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)

    pygame.display.flip()


def update_bullets(screen, stats, sc, inos, bullets):
    '''обновление позиции пуль(удаление)'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        for i in collisions.values():
            stats.score += 5 * len(i)
        sc.image_score()
        check_high_score(stats, sc)
        # sc.image_guns()     # HELTH
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos, imag)


def gun_kill(stats, screen, sc, gun, inos, bullets):
    '''столкновение пушки и армии'''
    if stats.guns_left > 0:
        stats.guns_left -= 1   # Вычитание жизней пушки
        inos.empty()
        bullets.empty()
        create_army(screen, inos, imag)  # Создаём новую армию
        gun.create_gun()
        time.sleep(0.9)
    else:
        stats.run_game = False
        sys.exit()


def update_inos(stats, screen, sc, gun, inos, bullets):
    '''обновляет позицию врагов'''
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, sc, gun, inos, bullets)
    inos_check(stats, screen, sc, gun, inos, bullets)


def inos_check(stats, screen, sc, gun, inos, bullets):
    """добралась ли армия до края"""
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, inos, bullets)
            break


def create_army(screen, inos, imag):
    '''создание армии врагов'''
    ino = Ino(screen, imag)
    ino_width = ino.rect.width + 10    # чтобы не касались друг друга +10
    number_ino_x = int((1000 - 1 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((800 - 189 - (2 * ino_height) / ino_height))

    for row_number in range(number_ino_y - 603):   # -600 чтобы не заходили за корабль
        for ino_number in range(number_ino_x):
            ino = Ino(screen, imag)
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_number
            inos.add(ino)


def check_high_score(stats, sc):
    '''Проверка новых рекордов'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('../Text/high_score.txt', 'w') as f:
            f.write(str(stats.high_score))