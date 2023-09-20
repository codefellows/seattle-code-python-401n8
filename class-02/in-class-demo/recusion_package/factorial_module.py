"""
Calculates factorial !

5! == 1 * 2 * 3 * 4 * 5
"""


def factorial(n):
    # base case (when do we stop recursion?)
    if n <= 1:
        return 1

    # recursive case
    return n * factorial(n - 1)
