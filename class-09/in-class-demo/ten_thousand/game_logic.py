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
    def roll_dice(n):
        return tuple(random.randint(1, 6) for _ in range(n))

    @staticmethod
    def calculate_score(roll):
        roll = Counter(roll)
        score = 0

        # Check for straight
        if len(roll) == 6:
            return 1500

        # 3 pair
        # if len(roll) == 3 and roll.most_common()[0][1] == roll.most_common()[2][1]:
        if len(roll) == 3 and all(quantity == 2 for quantity in roll.values()):
            return 1500

        # 3 or more of any number
        for i in range(1, 7):  # 1, 2, 3, 4, 5, 6
            quantity = roll[i]  # roll and key i
            if quantity >= 3:
                if i == 1:
                    score += (quantity - 2) * 1000
                else:
                    score += (quantity - 2) * 100 * i

        # 1s and 5s
        score += 100 if roll[1] == 1 else 0
        score += 200 if roll[1] == 2 else 0
        score += 50 if roll[5] == 1 else 0
        score += 100 if roll[5] == 2 else 0

        return score

    @staticmethod
    def is_cheating(roll, keepers):
        return bool(Counter(keepers) - Counter(roll))

    @staticmethod
    def get_scorers(dice):
        # version_3

        all_dice_score = GameLogic.calculate_score(dice)

        if all_dice_score == 0:
            return tuple()

        scorers = []

        # for i in range(len(dice)):

        for i, val in enumerate(dice):
            sub_roll = dice[:i] + dice[i + 1:]
            sub_score = GameLogic.calculate_score(sub_roll)

            if sub_score != all_dice_score:
                scorers.append(val)

        return tuple(scorers)
