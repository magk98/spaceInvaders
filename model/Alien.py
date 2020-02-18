from model.Character import Character


class Alien(Character):
    def __init__(self, _x, _y, _speed, _gun_speed):
        super(Alien, self).__init__(_x, _y, _speed, _gun_speed)
        self.image_name = 'alien.png'


    def move(self, x_diff, y_diff):
        self.x += x_diff
        self.y += y_diff
