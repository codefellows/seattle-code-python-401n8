from ten_thousand.game_logic import GameLogic


def monte_carlo_sim_scores(num_dice, num_simulations=1000000):
    total_score = 0

    for _ in range(num_simulations):
        roll = GameLogic.roll_dice(num_dice)
        total_score += GameLogic.calculate_score(roll)

    return total_score / num_simulations


def monte_carlo_sim_dice(num_dice, num_simulations=1000000):
    remaining_dice_occurrences = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }

    for _ in range(num_simulations):
        roll = GameLogic.roll_dice(num_dice)

        # not a zilch
        if GameLogic.calculate_score(roll):
            dice_remaining = num_dice - len(GameLogic.get_scorers(roll)) or 6
            remaining_dice_occurrences[dice_remaining] += 1
        else:
            remaining_dice_occurrences[0] += 1

    remaining_dice_occurrences = {dice: occurrences / num_simulations for dice, occurrences in remaining_dice_occurrences.items() if occurrences}

    return remaining_dice_occurrences


def compute_expected_values(monte_carlo_function):
    expected = {}

    for num_dice in range(1, 7):
        expected[num_dice] = monte_carlo_function(num_dice, 1000)

    return expected


if __name__ == "__main__":
    expected_scores = compute_expected_values(monte_carlo_sim_scores)
    print("expected_scores is:", expected_scores)
    expected_dice = compute_expected_values(monte_carlo_sim_dice)
    print("expected_dice is:", expected_dice)
