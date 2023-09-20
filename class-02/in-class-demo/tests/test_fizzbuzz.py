# import pytest and the functions I want to test
import pytest
from fizzbuzz_package.fizzbuzz_module import fizzbuzz


# @pytest.mark.skip()
def test_fizzbuzz_exists():
    assert fizzbuzz


def test_fizzbuzz_one():
    actual = fizzbuzz(1)
    expected = "1"
    assert actual == expected


def test_fizzbuzz_three():
    actual = fizzbuzz(3)
    expected = "fizz"
    assert actual == expected


def test_fizzbuzz_five():
    actual = fizzbuzz(5)
    expected = "buzz"
    assert actual == expected


def test_fizzbuzz_fifteen():
    actual = fizzbuzz(15)
    expected = "fizzbuzz"
    assert actual == expected
