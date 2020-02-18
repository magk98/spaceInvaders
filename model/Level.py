from model import Main
from model.Alien import Alien


class Level:
    def __init__(self, _number):
        self.number = _number
        self.score = 0
        self.alive_aliens = self.create_aliens()

    def create_aliens(self):
        aliens = []
        for i in range(0, 2 * self.number):
            aliens += [Alien(i * Main.SCREEN_HEIGHT, 10, 10, 10)]
        return aliens

    def draw_aliens(self, win):
        for alien in self.alive_aliens:
            alien.draw(win)