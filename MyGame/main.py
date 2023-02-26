import random

import pygame
from pygame.constants import QUIT

BLACK = 0, 0, 0
WHITE = 255, 255, 255

pygame.init()

screen = width, heigth = 800, 600

main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill(WHITE)
bal_rect = ball.get_rect()
ball_speed = [1, 1]



is_working = True

while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

    bal_rect = bal_rect.move(ball_speed)

    if bal_rect.bottom >= heigth or bal_rect.top <= 0:
        ball_speed[1] = - ball_speed[1]
        ball.fill(RANDOM)

    if bal_rect.right >= width or bal_rect.left <= 0:
        ball_speed[0] = - ball_speed[0]
        ball.fill(RANDOM)

    main_surface.fill(BLACK)
    RANDOM = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    main_surface.blit(ball, bal_rect)

    pygame.display.flip()