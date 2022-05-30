import random
from datetime import datetime, time


class Randomizer:
    """Perform probabilistic decision making to mimic human behavior.
    """

    def __init__(self, probability: float):
        """Constructor.

        Args:
            probability (float): the probability 0 <= x <= 1 that the text will
            be sent.
        """
        self.probability = probability

        # check if time of day is night in order to lower the probability
        # that something will be run.
        if self.is_night():
            self.probability = 0.1

    def might_run(self, func, *arg):
        """Runs a given function with a certain probability.

        Args:
            func (function): the function that is in question.

        Returns:
            bool: whether the function ran.
        """
        if random.random() < self.probability:
            func(*arg)
            return True
        return False

    def is_night(self):
        """Checks if the time of day is currently night.

        Returns:
            bool: whether the time of day is night or not.
        """
        now_time = datetime.now().time()
        is_day = time(7, 00) <= now_time >= time(21, 00)
        return not is_day
