"""Module do_even. Calculates evenness of given number."""

from random import randint
from brain_games.dispatch_all import dispatch_all


LOWER_BOUND = 1
UPPER_BOUND = 100


def do_even():
    """do_even takes argument and returns evenness.
    Parameter: operat_question and correct result.
    Returns:  is random_number is even.
    """
    
    FUNC_TXT = 'Answer "yes" if the number is even, otherwise answer "no".'
    random_number = randint(LOWER_BOUND, UPPER_BOUND)
    if random_number % 2 == 0:
        correct_result = 'yes'
    else:
        correct_result = 'no'
    operat_question = random_number
    
    
    dispatch_all(FUNC_TXT, operat_question, correct_result)



