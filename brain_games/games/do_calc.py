"""Module do_calc. Do main calculations and return results to the main."""

from random import choice
from random import randint

LOWER_BOUND = 1
UPPER_BOUND = 100


def do_calc():
    """Do calculates brain_calc.
    Parameters: - numb1 and numb2 are random numbers.
    Returns: result of mathem. operation, correct result and text
    of this function.
    """
    FUNC_TXT = 'What is the result of the expression?'
    random_number1 = randint(LOWER_BOUND, UPPER_BOUND)
    random_number2 = randint(LOWER_BOUND, UPPER_BOUND)
    my_choice = choice(['add', 'subtr', 'multipl'])
    dict_of_choice = {
        'add': ['{0} {1} {2}'.format(random_number1, '+', random_number2),
        random_number1 + random_number2],
        'subtr': ['{0} {1} {2}'.format(random_number1, '-', random_number2),
        random_number1 - random_number2],
        'multipl': ['{0} {1} {2}'.format(random_number1, '*', random_number2),
        random_number1 * random_number2]
    }
    operat_quest = dict_of_choice[my_choice][0]
    cor_res = dict_of_choice[my_choice][1]
    return(operat_quest, cor_res, FUNC_TXT)
