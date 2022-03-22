"""Module do_even. Calculates evenness of given number."""

from random import randint

LOWER_BOUND = 1
UPPER_BOUND = 100


def do_even():
    """do_even takes argument and returns evenness.
    Parameter: operat_question and correct result.
    Returns:  is random_number is even.
    """
    random_number = randint(LOWER_BOUND, UPPER_BOUND)
    if random_number % 2 == 0:
        correct_result = 'yes'
    else:
        correct_result = 'no'
    operat_question = 'Question: {0}'.format(random_number)
    return (operat_question, correct_result)
