import pygame, os

from model import Main
from model.Character import Character


class Ship(Character):
    def __init__(self, _x, _y, _speed, _gun_speed):
        super(Ship, self).__init__(_x, _y, _speed, _gun_speed)
        self.image_name = 'shiip.png'
        self.shots = []

    def shot(self, win):
        self.shots += [Ship.Shot(self.x + Main.SCREEN_WIDTH // 40, self.y)]
        self.draw(win)

    class Shot:
        def __init__(self, _x, _y):
            self.x = _x
            self.y = _y

        def draw(self, win, ship):
            pygame.draw.rect(win, Main.red, (self.x - 1, self.y, 4, 8))
            if self.y > Main.SCREEN_HEIGHT:
                ship.shots.remove(self)

        def move(self):
            x_diff, y_diff = 0, -8
            self.x += x_diff
            self.y += y_diff
