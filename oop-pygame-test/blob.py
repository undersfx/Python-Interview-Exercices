import random

class Blob:
    '''Blob that lives in the Blodworld'''

    def __init__(self, color, x_max, y_max, size_range=(4, 8), mov_speed=(-1, 2)):
        self.color = color
        self.x_max = x_max
        self.y_max = y_max
        self.x = random.randrange(0, self.x_max)
        self.y = random.randrange(0, self.y_max)
        self.size = random.randrange(*size_range)
        self.mov_speed = mov_speed

    def move(self):
        self.move_x = random.randrange(*self.mov_speed)
        self.move_y = random.randrange(*self.mov_speed)
        self.x += self.move_x
        self.y += self.move_y

    def check_bounds(self):
        if self.x < 0:
        	self.x = 0
        elif self.x > self.x_max:
        	self.x = self.x_max

        if self.y < 0:
        	self.y = 0
        elif self.y > self.y_max:
        	self.y = self.y_max
