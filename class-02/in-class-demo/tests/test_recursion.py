import pytest
from recusion_package.factorial_module import factorial


def test_factorial_exists():
    assert factorial


# @pytest.mark.skip()
def test_factorial_five():
    actual = factorial(5)
    expected = 120
    assert actual == expected


# @pytest.mark.skip()
def test_factorial_one():
    actual = factorial(1)
    expected = 1
    assert actual == expected


# @pytest.mark.skip()
def test_factorial_two():
    actual = factorial(2)
    expected = 2
    assert actual == expected


