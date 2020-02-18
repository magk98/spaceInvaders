import pygame

from model import Main
from model.Alien import Alien


class Level:
    def __init__(self, _number):
        self.number = _number
        self.score = 0
        self.alive_aliens = self.create_aliens()

    def create_aliens(self):
        aliens = []
        for i in range(0, 5 * self.number):
            aliens += [Alien((i * Main.SCREEN_WIDTH // 17) % Main.SCREEN_WIDTH + Main.SCREEN_WIDTH // 34,
                             10 + Main.SCREEN_HEIGHT // 15 * (1 + (i * Main.SCREEN_WIDTH // 17) // Main.SCREEN_WIDTH),
                             10, 10)]
        return aliens

    def draw_aliens(self, win):
        for alien in self.alive_aliens:
            alien.draw(win)

    def check_collision(self, ship):
        for shot in ship.shots:
            for alien in self.alive_aliens:
                if abs(shot.x - alien.x - Main.SCREEN_WIDTH // 34) < Main.SCREEN_WIDTH // 34:
                    if abs(shot.y - alien.y - Main.SCREEN_HEIGHT // 30) < Main.SCREEN_HEIGHT // 30:
                        self.alive_aliens.remove(alien)
                        ship.shots.remove(shot)
                        self.score += 1

    def move_aliens(self, alien_left_move, alien_down_move):
        for alien in self.alive_aliens:
            if alien_left_move:
                alien.move(Main.SCREEN_WIDTH // 34, 0)
            elif alien_down_move:
                alien.move(0, Main.SCREEN_HEIGHT // 30)
            else:
                alien.move(-Main.SCREEN_WIDTH // 34, 0)

    def draw_components(self, win, ship):
        ship.draw(win)
        ship.draw_health(win)
        self.draw_aliens(win)
        for shot in ship.shots:
            shot.draw(win, ship)
            shot.move()
        score = Main.font.render(str(self.score), True, Main.red)
        textRect = score.get_rect()
        textRect.center = (Main.SCREEN_WIDTH // 2, Main.SCREEN_HEIGHT // 2)
        win.blit(score, textRect)
        pygame.display.update()
        win.fill(Main.dark_sky)