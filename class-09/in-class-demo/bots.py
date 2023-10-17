from abc import ABC, abstractmethod
import builtins
import random
import re
from ten_thousand.game import play
from ten_thousand.game_logic import GameLogic


class BaseBot(ABC):
    """Base class for Game bots"""

    def __init__(self, print_all=False):
        self.last_print = ""
        self.last_roll = []
        self.print_all = print_all
        self.dice_remaining = 0
        self.unbanked_points = 0

        self.real_print = print
        self.real_input = input
        builtins.print = self._mock_print
        builtins.input = self._mock_input
        self.total_score = 0

    def reset(self):
        """restores the real print and input builtin functions"""

        builtins.print = self.real_print
        builtins.input = self.real_input

    def report(self, text):
        """Prints out final score, and all other lines optionally"""

        if self.print_all:
            self.real_print(text)
        elif text.startswith("Thanks for playing."):
            score = re.sub("\D", "", text)
            self.total_score += int(score)

    def _mock_print(self, *args, **kwargs):
        """steps in front of the real builtin print function"""

        line = " ".join(args)

        if "unbanked points" in line:

            # parse the proper string
            # E.g. "You have 700 unbanked points and 2 dice remaining"
            unbanked_points_part, dice_remaining_part = line.split("unbanked points")

            # Hold on to unbanked points and dice remaining for determining rolling vs. banking
            self.unbanked_points = int(re.sub("\D", "", unbanked_points_part))

            self.dice_remaining = int(re.sub("\D", "", dice_remaining_part))

        elif line.startswith("*** "):
            self.last_roll = [int(ch) for ch in line if ch.isdigit()]

        else:
            self.last_print = line

        self.report(*args, **kwargs)

    def _mock_input(self, *args, **kwargs):
        """steps in front of the real builtin print function"""

        if self.last_print == "(y)es to play or (n)o to decline":

            return "y"

        elif self.last_print == "Enter dice to keep, or (q)uit:":

            return self._enter_dice()

        elif self.last_print == "(r)oll again, (b)ank your points or (q)uit:":

            return self._roll_bank_or_quit()

        raise ValueError(f"Unrecognized last print {self.last_print}")

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""

        roll = GameLogic.get_scorers(self.last_roll)

        roll_string = ""

        for value in roll:
            roll_string += str(value)

        self.report("> " + roll_string)

        return roll_string

    @abstractmethod
    def _roll_bank_or_quit(self):
        """decide whether to roll the dice, bank the points, or quit"""

        # subclass MUST implement this method
        pass

    @classmethod
    def play(cls, num_games=1):
        """Tell Bot play game a given number of times.
        Will report average score"""

        mega_total = 0

        for _ in range(num_games):
            player = cls()

            try:
                play()
            except SystemExit:
                # in game system exit is fine
                # because that's how they quit.
                pass

            mega_total += player.total_score
            player.reset()

        print(
            f"{cls.__name__}: {num_games} games played with average score of {mega_total // num_games}"
        )


class NervousNellie(BaseBot):
    """NervousNellie banks the first roll always"""

    def _roll_bank_or_quit(self):
        return "b"


class MiddlingMargaret(BaseBot):
    """MiddlingMargaret has a moderate playing style"""

    def _roll_bank_or_quit(self):

        if self.unbanked_points >= 500 or self.dice_remaining < 3:
            return "b"

        return "r"


class RandomAdam(BaseBot):

    def _roll_bank_or_quit(self):
        random_number = random.randint(1, 2)

        if random_number == 1:
            return "b"
        elif random_number == 2:
            return "r"


class AwesomeAdam(BaseBot):

    # How much ya gonna score if you roll
    expected_scores = {
        1: 25,
        2: 50,
        3: 86.9128,
        4: 143.618,
        5: 225.7611,
        6: 408.486
    }

    # What are the chances you'll have x dice after you roll
    expected_dice_remaining = {
        1: {0: 0.666667, 6: 0.333333},
        2: {0: 0.444168, 1: 0.444491, 6: 0.111341},
        3: {0: 0.277464, 1: 0.222381, 2: 0.444624, 6: 0.055531},
        4: {0: 0.157112, 1: 0.135785, 2: 0.296150, 3: 0.370474, 6: 0.040479},
        5: {0: 0.076889, 1: 0.110279, 2: 0.211568, 3: 0.308638, 4: 0.262208, 6: 0.030418},
        6: {0: 0.023137, 1: 0.094805, 2: 0.178191, 3: 0.246948, 4: 0.224745, 5: 0.154664, 6: 0.07751}
    }

    def _rolling_eu(self):
        """
        Looks 2 steps into the future
        :return: Boolean, representing whether the bot should roll again (True) or bank (False)
        """
        eu = self.unbanked_points
        current_dice_remaining = self.dice_remaining

        for remaining, odds in self.expected_dice_remaining[current_dice_remaining].items():
            # chance of zilch
            if remaining == 0:
                eu -= odds * self.unbanked_points

            # add the expected utility of the next roll of dice
            else:
                second_roll_utility = self.expected_scores[remaining]
                for r, o in self.expected_dice_remaining[remaining].items():
                    # chance of zilch in second roll
                    if r == 0:
                        second_roll_utility -= o * second_roll_utility
                    else:
                        second_roll_utility += o * self.expected_scores[r]

                eu += odds * max(second_roll_utility, self.expected_scores[remaining])

        return eu > self.unbanked_points

    def _roll_bank_or_quit(self):
        if self._rolling_eu():
            return "r"
        else:
            return "b"


class Bank2650_Roll3_Bot(BaseBot):
    def _roll_bank_or_quit(self):
        """your logic here"""
        if self.unbanked_points >= 2650:
            return 'b'
        elif self.dice_remaining <= 3:
            return 'b'
        else:
            return 'r'


    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""

        return super()._enter_dice()


class Bank2000_Roll3_Bot(BaseBot):
    def _roll_bank_or_quit(self):
        if self.unbanked_points >= 2000:
            return 'b'
        if self.dice_remaining <= 3:
            return 'b'
        else:
            return 'r'

    def _enter_dice(self):

        return super()._enter_dice()


class Bank2000_Roll2_Bot(BaseBot):
    def _roll_bank_or_quit(self):
        if self.unbanked_points >= 2000:
            return 'b'
        if self.dice_remaining <= 2:
            return 'b'
        else:
            return 'r'

    def _enter_dice(self):

        return super()._enter_dice()


class Bank500_Bot(BaseBot):
    def _roll_bank_or_quit(self):
        if self.unbanked_points >= 500:
            return 'b'
        else:
            return 'r'

    def _enter_dice(self):

        return super()._enter_dice()


if __name__ == "__main__":
    num_games = 1000
    NervousNellie.play(num_games)
    MiddlingMargaret.play(num_games)
    RandomAdam.play(num_games)
    AwesomeAdam.play(num_games)
    Bank2650_Roll3_Bot.play(num_games)
    Bank2000_Roll3_Bot.play(num_games)
    Bank2000_Roll2_Bot.play(num_games)
    Bank500_Bot.play(num_games)
