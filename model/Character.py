import pygame
import os

from model import Main


class Character:
    def __init__(self, _x, _y, _speed, _gun_speed):
        self.x = _x
        self.y = _y
        self.speed = _speed
        self.gun = _gun_speed
        self.image_name = ''

    def move(self, x_diff, y_diff):
        if 0 <= self.x + x_diff < Main.SCREEN_WIDTH - 15 and 0 <= self.y + y_diff < Main.SCREEN_HEIGHT - 15:
            self.x += x_diff
            self.y += y_diff

    def draw(self):
        image = pygame.image.load(os.path.join('images', self.image_name))
        image = pygame.transform.scale(image, (Main.SCREEN_WIDTH // 17, Main.SCREEN_HEIGHT // 15)).convert_alpha()
        Main.win.blit(image, (self.x, self.y))

    class Shot:
        def __init__(self, _x, _y):
            self.x = _x
            self.y = _y

        def draw(self, ship, color):
            pygame.draw.rect(Main.win, color, (self.x - 1, self.y, 4, 8))
            if self.y < 0:
                ship.shots.remove(self)
            if self.y > Main.SCREEN_HEIGHT:
                ship.alien_shots.remove(self)

        def move(self, x_diff=0, y_diff=-8):
            self.x += x_diff
            self.y += y_diff

