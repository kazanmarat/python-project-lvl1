"""Module do_prime. It calculates if the given number is prime."""

from random import randint

LOWER_BOUND = 1
UPPER_BOUND = 100


def do_prime():
    """Calculate number and return True if it is prime.
    Create inner function.
    Parameter - random_number.
    Returns - operat_question, correct_result.
    """
    FUNC_TXT = 'Answer "yes" if given number is prime, otherwise answer "no".'
    random_number = randint(LOWER_BOUND, UPPER_BOUND)
    operat_question = '{0}'.format(random_number)
    
    def is_prime(any_number):
        limiter = int((any_number ** 0.5) + 1)
        inner_correct_result = 'yes'
        for i in range(2, limiter):
            if any_number % i == 0:
                inner_correct_result = 'no'
        if any_number == 1:
            inner_correct_result = 'no'
        elif any_number == 2:
            inner_correct_result = 'yes'    
        return any_number, inner_correct_result
        
    operat_question, correct_result = is_prime(random_number)
    return (operat_question, correct_result, FUNC_TXT)
