"""This module generate 2 random numbers
and determines the greatest common divisor."""
import random


def gcd():
    """Generates 2 random numbers between 1 and 100.
    Returns the question text to the player and
    the greatest common divisor."""
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    question = f"{first_num} {second_num}"
    while first_num != second_num:
        if first_num > second_num:
            first_num -= second_num
        else:
            second_num -= first_num
    return question, str(second_num)


game_rule = 'Find the greatest common divisor of given numbers.'
