from ten_thousand.game_logic import GameLogic


def play(roller=GameLogic.roll_dice):
    welcome_user()
    total_score = 0

    for round_number in range(1, 21):
        round_points = start_round(round_number, roller)

        if round_points == "q":
            break

        total_score += round_points
        print_bank(round_points, round_number)

        print(f"Total score is {total_score} points")

    quit_game(total_score)


def start_round(round_number, roller):
    print(f"Starting round {round_number}")
    unbanked_points = 0
    dice_remaining = 6

    while True:
        print(f"Rolling {dice_remaining} dice...")
        roll = roller(dice_remaining)
        print_dice(roll)

        # check for zilch
        if GameLogic.calculate_score(roll) == 0:
            print_zilch()
            return 0

        keepers = keep_or_quit(roll)

        if keepers == "q":
            return "q"

        unbanked_points += GameLogic.calculate_score(keepers)
        dice_remaining -= len(keepers)

        # hot dice
        if dice_remaining == 0:
            dice_remaining = 6

        rbq = roll_bank_or_quit(unbanked_points, dice_remaining)

        if rbq == "b":
            return unbanked_points

        if rbq == "q":
            return "q"


def welcome_user():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    choice = input("> ")

    if choice == "n":
        print("OK. Maybe another time")
        exit()


def quit_game(total_score):
    print(f"Thanks for playing. You earned {total_score} points")
    exit()


def print_dice(roll):
    # print("***", *roll, "***")
    print(f"*** {' '.join([str(i) for i in roll])} ***")


def print_bank(round_points, round_number):
    print(f"You banked {round_points} points in round {round_number}")


def print_zilch():
    print("****************************************")
    print("**        Zilch!!! Round over         **")
    print("****************************************")


def keep_or_quit(roll):
    while True:
        print("Enter dice to keep, or (q)uit:")
        keepers = input("> ")

        if keepers == "q":
            return "q"

        # turns string keepers into tuple of ints keepers
        keepers = tuple(int(num) for num in keepers if num.isnumeric())

        # is user cheating?
        cheating = GameLogic.is_cheating(roll, keepers)

        if not cheating:
            # let them leave the while loop
            break

        print("Cheater!!! Or possibly made a typo...")
        print_dice(roll)

    return keepers


def roll_bank_or_quit(unbanked_points, dice_remaining):
    print(f"You have {unbanked_points} unbanked points and {dice_remaining} dice remaining")
    print("(r)oll again, (b)ank your points or (q)uit:")
    choice = input("> ")
    return choice


if __name__ == "__main__":
    play()
