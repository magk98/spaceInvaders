import pygame
import os

from model import Main
from model.Character import Character


class Alien(Character):
    def __init__(self, _x, _y, _speed, _gun_speed):
        super(Alien, self).__init__(_x, _y, _speed, _gun_speed)
        self.image_name = 'alien.png'

    def move(self, x_diff, y_diff):
        if 0 <= self.x + x_diff < Main.SCREEN_WIDTH - 15 and 0 <= self.y + y_diff < Main.SCREEN_HEIGHT - 15:
            self.x += x_diff
            self.y += y_diff
