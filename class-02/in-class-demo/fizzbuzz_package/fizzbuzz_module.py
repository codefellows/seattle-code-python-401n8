"""
Fizzbuzz rules:
"1", "2", "fizz", "4", "buzz", "6", "7", ... "fizzbuzz"
"""


def fizzbuzz(n):
    """
    Returns the number as a string, if it's divisible by 3 returns "fizz"
    if it's divisible by 5 returns "buzz", if it's both divisible by 3
    and 5, returns "fizzbuzz"
    :param n: integer
    :return: string
    """
    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    if n % 5 == 0:
        return "buzz"
    if n % 3 == 0:
        return "fizz"
    return str(n)
