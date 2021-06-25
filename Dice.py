import random


# Class for a dice

class Dice:

    def __init__(self):
        self.value = random.randint(1, 6)

    def roll(self) -> int:
        """

        :rtype: object
        """
        self.value = random.randint(1, 6)
        return self.value
