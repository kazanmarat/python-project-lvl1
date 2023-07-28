"""This module asks if the number is even.
Returns a random number and it's evenness."""
import random


def check_even(num):
    """Check the given number for evenness.
    If even, then returns 'yes', otherwise - 'no'."""
    if num % 2 == 0:
        return 'yes'
    return 'no'


def random_and_check():
    """Calls the 'random.randint' function
    to generate a random number between 1 and 50.
    Then calls the 'check_even' function
    to check for evenness.
    Returns a random number and the correct answer
    to a parity question."""
    random_num = random.randint(1, 50)
    right_answer = check_even(random_num)
    return random_num, right_answer


game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'
