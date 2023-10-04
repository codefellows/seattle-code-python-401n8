import pytest
from dragon_dice.game_logic import GameLogic
from dragon_dice.game import play


def test_play_exists():
    assert play


def test_roller():
    # `actual` is a tuple of dice rolls (ints)
    actual = GameLogic.roll_dice(6)
    assert isinstance(actual, tuple)
    assert len(actual) == 6

    for dice in actual:
        assert isinstance(dice, int)
        assert 1 <= dice <= 6  # __le__


def test_double_ones():
    actual = GameLogic.calculate_damage((1, 1))
    expected = 10
    assert actual == expected


def test_double_twos():
    actual = GameLogic.calculate_damage((2, 2))
    expected = 20
    assert actual == expected


def test_double_threes():
    actual = GameLogic.calculate_damage((3, 3))
    expected = 30
    assert actual == expected


def test_double_fours():
    actual = GameLogic.calculate_damage((4, 4))
    expected = 40
    assert actual == expected


def test_double_fives():
    actual = GameLogic.calculate_damage((5, 5))
    expected = 50
    assert actual == expected


def test_double_sixes():
    actual = GameLogic.calculate_damage((6, 6))
    expected = 60
    assert actual == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ((1, 1, 6, 3), 10),
        ((1, 1, 6, 3, 1), 0),
        ((6, 6, 5, 5), 110),
        ((2, 2, 3, 4), 20),
        ((2, 2, 3, 4), 20),
    ]
)
def test_all_damage(test_input, expected):
    actual = GameLogic.calculate_damage(test_input)
    assert actual == expected
