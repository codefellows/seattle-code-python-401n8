"""
Warm-Up Exercise: Lambda Functions

Objective:
    Understand the basics of writing and using lambda functions.

Instructions:
    1. Read the provided documentation and comments carefully.
    2. Complete the TODO sections to implement the lambda functions.
    3. Test your lambda functions using the provided test cases.
"""

# Documentation:

# What is a lambda function?
# Lambda functions are small, anonymous functions that can have any number of arguments, but can only have one expression.
# The expression is evaluated and returned when the lambda function is called.

# Syntax:
# lambda arguments : expression

# Example:
# add = lambda x, y: x + y
# print(add(5, 3))  # Outputs: 8

# TODO 1: Create a lambda function that takes two numbers and returns their product.
multiply = lambda x, y: x * y  # Complete this line.

# TODO 2: Create a lambda function that takes a string and returns its length.
length = None  # Replace 'None' with your lambda function.

# TODO 3: Create a lambda function that takes a list of numbers and returns the maximum number from the list.
find_max = None  # Replace 'None' with your lambda function.

# TODO 4: Create a lambda function that takes two numbers and returns their difference (subtract the second from the first).
subtract = None  # Replace 'None' with your lambda function.

# TODO 5: Create a lambda function that takes a list and returns the number of unique elements in the list.
count_unique = None  # Replace 'None' with your lambda function.

# TODO 6: Create a lambda function that takes a string and returns True if it's a palindrome, otherwise False.
is_palindrome = None  # Replace 'None' with your lambda function.

# Test Cases:

assert multiply(5, 4) == 20, "Test case 1 failed"
assert multiply(0, 100) == 0, "Test case 2 failed"

assert length("Hello") == 5, "Test case 3 failed"
assert length("") == 0, "Test case 4 failed"

assert find_max([1, 2, 3, 4, 5]) == 5, "Test case 5 failed"
assert find_max([-5, -4, -3, -2, -1]) == -1, "Test case 6 failed"

assert subtract(10, 5) == 5, "Test case 7 failed"
assert subtract(5, 10) == -5, "Test case 8 failed"

assert count_unique([1, 2, 2, 3, 4, 4, 4]) == 4, "Test case 9 failed"
assert count_unique([]) == 0, "Test case 10 failed"

assert is_palindrome("radar") == True, "Test case 11 failed"
assert is_palindrome("hello") == False, "Test case 12 failed"

print("All test cases passed!")
