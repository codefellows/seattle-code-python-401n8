import random
from collections import Counter


class GameLogic:
    def __init__(self, mock_rolls):
        """
        Initialize an instance of the GameLogic class for testing. Accepts argument of a list of mock rolls.
        :param mock_rolls: List a tuples, each tuple is a collection of integers representing a mocked roll
        """
        self.mock_rolls = mock_rolls

    def mock_roller(self, _):
        """
        Acts like `roll_dice`
        :return: A tuple of integers, representing dice values.
        """
        return self.mock_rolls.pop(0)

    @staticmethod
    def roll_dice(num_dice: int) -> tuple:
        """
        Takes a number of dice to roll, and returns a tuple of dice values.
        :param num_dice: Integer representing number of dice to roll.
        :return: A tuple of integers, representing dice values.
        """
        return tuple(random.randint(1, 6) for _ in range(num_dice))

    @staticmethod
    def calculate_damage(dice_roll: tuple) -> int:
        """
        Calculates damage dealt to the Drag based off a given dice roll.
        :param dice_roll: A tuple of ints, representing rolled dice.
        :return: Int, representing damage dealt.
        """
        dice_counter = Counter(dice_roll)
        damage = 0

        for dice_value, count in dice_counter.items():
            if count == 2:
                damage += dice_value * 10
        return damage

        # dice_counter = {}
        # damage = 0
        #
        # for dice in dice_roll:
        #     if dice in dice_counter:
        #         dice_counter[dice] += 1
        #     else:
        #         dice_counter[dice] = 1
        #
        # for dice_value, count in dice_counter.items():
        #     print(dice_value, count)
        #     if count == 2:
        #         damage += dice_value * 10
        #
        # return damage


# # Allows for other roll_dice function/methods
# def roll_dice():
#     pass
#
#
# class AltLogic:
#     @staticmethod
#     def roll_dice():
#         pass

