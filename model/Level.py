import pygame

from model import Main
from model.Alien import Alien


class Level:
    def __init__(self, _number, _score=0):
        self.number = _number
        self.score = _score
        self.alive_aliens = self.create_aliens()
        self.alien_shots = []

    def create_aliens(self):
        aliens = []
        for i in range(0, 5 * self.number):
            aliens += [Alien((i * Main.SCREEN_WIDTH // 17) % Main.SCREEN_WIDTH + Main.SCREEN_WIDTH // 34,
                             (Main.SCREEN_HEIGHT // 15) * (1 + (i * Main.SCREEN_WIDTH // 17) // Main.SCREEN_WIDTH),
                             10, 10)]
        return aliens

    def draw_aliens(self):
        for alien in self.alive_aliens:
            alien.draw()

    def check_collision(self, ship):
        for shot in ship.shots:
            for alien in self.alive_aliens:
                if abs(shot.x - alien.x - Main.SCREEN_WIDTH // 34) < Main.SCREEN_WIDTH // 34:
                    if abs(shot.y - alien.y - Main.SCREEN_HEIGHT // 30) < Main.SCREEN_HEIGHT // 30:
                        self.alive_aliens.remove(alien)
                        ship.shots.remove(shot)
                        self.score += 1
        for shot in self.alien_shots:
            if abs(shot.x - ship.x - Main.SCREEN_WIDTH // 34) < Main.SCREEN_WIDTH // 34:
                if abs(shot.y - ship.y - Main.SCREEN_HEIGHT // 30) < Main.SCREEN_HEIGHT // 30:
                    self.alien_shots.remove(shot)
                    ship.health -= 1
                    if ship.health < 0:
                        self.print_lose()
                        ship.health = 3

    def move_aliens(self, alien_left_move, alien_down_move):
        for alien in self.alive_aliens:
            if alien_left_move:
                alien.move(Main.SCREEN_WIDTH // 34, 0)
                alien.image_name = 'alien.png' if alien.image_name == 'alien1.png' else 'alien1.png'
            elif alien_down_move:
                alien.move(0, Main.SCREEN_HEIGHT // 30)
            else:
                alien.image_name = 'alien.png' if alien.image_name == 'alien1.png' else 'alien1.png'
                alien.move(-Main.SCREEN_WIDTH // 34, 0)

    def draw_components(self, ship):
        ship.draw()
        ship.draw_health()
        self.draw_aliens()
        for shot in ship.shots:
            shot.draw(ship, Main.red)
            shot.move()
        for shot in self.alien_shots:
            shot.draw(self, Main.green)
            shot.move(0, 8)
        score = Main.font.render(str(self.score), True, Main.red)
        textRect = score.get_rect()
        textRect.center = (Main.SCREEN_WIDTH // 2, Main.SCREEN_HEIGHT // 2)
        Main.win.blit(score, textRect)
        pygame.display.update()
        Main.win.fill(Main.dark_sky)

    def print_lose(self):
        lose_text = Main.font.render("Space invaders won :(", True, Main.red)
        textRect = lose_text.get_rect()
        textRect.center = (Main.SCREEN_WIDTH // 2, Main.SCREEN_HEIGHT // 2)
        Main.win.blit(lose_text, textRect)
        pygame.display.update()
        Main.win.fill(Main.dark_sky)
        pygame.time.delay(1500)
        self.number = 1
        self.score = 0
        self.alive_aliens = self.create_aliens()
