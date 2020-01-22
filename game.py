import pygame
from classes import *

white = (255,255,255)
black = (0,0,0)

pygame.init()

size = [800, 600]
quit = False
clk_speed = 30

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

player = Player(width=size[0], height=size[1])
ball = Ball(width=size[0], height=size[1])

right = False
left = False

while not quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit = True
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_LEFT:
                left = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_LEFT:
                left = False

    if left: player.x -= 4
    if right: player.x += 4
    ball.step(player.x)
    if (ball.isDead()): quit = True

    screen.fill(black)
    player.draw(screen)
    ball.draw(screen)
    pygame.display.update()
    clock.tick(40)

pygame.quit()
