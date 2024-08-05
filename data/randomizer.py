import random
from time import time


class Randomizer:
    def __init__(self):
        self.default_value = "random-"

    def create_random_string(self, str_from=None):
        current_time = time()
        random.seed(current_time)
        random_id = random.random()
        if str_from is None:
            return self.default_value + str(int(random_id * 10000000))
        else:
            return str_from + str(int(random_id * 10000000))
