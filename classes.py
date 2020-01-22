import random
import pygame


class Ball:
    def __init__(self, width, height):
        self.x = width/2
        self.y = height/2
        self.x_vel = 0
        self.y_vel = 5
        self.width = width
        self.height = height
        self.img = pygame.transform.scale(pygame.image.load('ball.png'), [20, 20])

    def bounce(self):
        if self.x <= 1: self.x_vel = random.randrange(3, 8)
        if self.x >= self.width-20: self.x_vel = random.randrange(-8, -3)
        if self.y <= 1: self.y_vel = random.randrange(3, 8)

    def player_bounce(self, x):
        print(self.x-x)
        if self.y >= self.height-35 and self.x-x > 50 and self.x-x <= 100:
            self.y_vel = random.randrange(-8, -3)
            self.x_vel = random.randrange(3, 8)
        if self.y >= self.height-35 and self.x-x <= 50 and self.x-x >= 0:
            self.y_vel = random.randrange(-8, -3)
            self.x_vel = random.randrange(-8, -3)

    def step(self, player_x):
        self.bounce()
        self.player_bounce(player_x)
        self.x += self.x_vel
        self.y += self.y_vel

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def isDead(self):
        return self.y >= self.height


class Brick:
    width = 10  # Trial basis
    height = 5

    def __init__(self, ):
        self.x = 0
        self.y = 0
        self.img = ""  # See img from flappy bird video
        self.powerup = 0  # For later use maybe

    def draw(self, screen):
        # Dont know what to do here yes
        return


class Player:
    def __init__(self, height, width):
        self.x = width/2
        self.img = pygame.transform.scale(pygame.image.load('player.png'), [100, 20])
        self.y = height-15

    def draw(self, screen):
        return screen.blit(self.img, (self.x, self.y))
