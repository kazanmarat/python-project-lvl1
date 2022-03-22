"""Module do_prime. It calculates if the given number is prime."""

from random import randint

LOWER_BOUND = 1
UPPER_BOUND = 100
def do_prime():
    """Calculate number and return True if it is prime.
    Parameter - random_number.
    Returns - operat_question, correct_result.
    """
    random_number = randint(LOWER_BOUND, UPPER_BOUND)
    operat_question = 'Question: {0}'.format(random_number)
    correct_result = 'yes'
    limiter = int((random_number ** 0.5) + 1)
    for i in range(2, limiter):
        if random_number % i == 0:
            correct_result = 'no'
    if random_number == 1:
        correct_result = 'no'
    return (operat_question, correct_result)
