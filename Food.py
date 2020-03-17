import random


class Food(object):

    def __init__(self, width, height, division_size):
        self.x = random.randint(0, width//division_size - 1) * division_size
        self.y = random.randint(0, height/division_size - 1) * division_size

    def generate(self, width, height, division_size):
        self.x = random.randint(0, width // division_size - 1) * division_size
        self.y = random.randint(0, height / division_size - 1) * division_size
