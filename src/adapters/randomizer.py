import random

class Randomizer:
    def __init__(self, probability: float):
        self.probability = probability

    def randomize(self, func, *arg):
        if random.random() < self.probability:
            func(*arg)
            return True
        return False
