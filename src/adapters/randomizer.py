import random
from datetime import datetime, time


class Randomizer:
    def __init__(self, probability: float):
        self.probability = probability

        # night mode
        if self.is_night():
            self.probability = 0.1

    def randomize(self, func, *arg):
        if random.random() < self.probability:
            func(*arg)
            return True
        return False

    def is_night(self):
        now_time = datetime.now().time()
        is_day = time(8, 00) <= now_time >= time(18, 00)
        return not is_day
