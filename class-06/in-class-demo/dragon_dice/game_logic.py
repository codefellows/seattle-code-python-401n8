import random
from collections import Counter


class GameLogic:
    @staticmethod
    def roll_dice(num_dice: int) -> tuple:
        """
        Takes a number of dice to roll, and returns a tuple of dice values.
        :param num_dice: Integer representing number of dice to roll.
        :return: A tuple of integers, representing dice values.
        """
        # dice = []
        #
        # for _ in range(num_dice):
        #     dice.append(random.randint(1, 6))
        #
        # return tuple(dice)
        return tuple(random.randint(1, 6) for _ in range(num_dice))

    @staticmethod
    def calculate_damage(dice_roll: tuple) -> int:
        """
        Calculates damage dealt to the Drag based off a given dice roll.
        :param dice_roll: A tuple of ints, representing rolled dice.
        :return: Int, representing damage dealt.
        """
        dice_counter = Counter(dice_roll)
        print(dice_counter)
        score = 0

        for dice_value, count in dice_counter.items():
            if count == 2:
                score += dice_value * 10
        return score

        # dice_counter = {}
        # score = 0
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
        #         score +=
        #
        # return dice_counter


# # Allows for other roll_dice function/methods
# def roll_dice():
#     pass
#
#
# class AltLogic:
#     @staticmethod
#     def roll_dice():
#         pass

