"""Module do_gcd. Calculates the greatest common divisor."""

from random import randint

LOWER_BOUND = 1
UPPER_BOUND = 100
def do_gcd():
    """Take given numbers num1 and num2 and returns gcd.
    Parameters: a and b are random numbers.
    Returns: the greatest common divisor.
    """
    
    random_number1 = randint(LOWER_BOUND, UPPER_BOUND)
    random_number2 = randint(LOWER_BOUND, UPPER_BOUND)
    
    
    operat_quest = ('Question: {0} {1}'.format(random_number1, random_number2))
    while (random_number2):
        random_number1, random_number2 = random_number2, random_number1 % random_number2
    correct_result = random_number1
    
    return (operat_quest, correct_result)
