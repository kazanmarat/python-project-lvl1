"""Module do_calc. Do main calculations and return results to the main."""

from random import choice
from random import randint

LOWER_BOUND = 1
UPPER_BOUND = 100

def do_calc():
    """Do calculates brain_calc.
    Parameters: - numb1 and numb2 are random numbers.
    Returns: result of mathem. operation.
    """
    
    random_number1 = randint(LOWER_BOUND, UPPER_BOUND)
    random_number2 = randint(LOWER_BOUND, UPPER_BOUND)
    
    
    my_choice = choice(['add', 'subtr', 'multipl'])

    if my_choice == 'add':
        operat_quest = 'Question: {0} {1} {2}'.format(random_number1, '+', random_number2)
        
        cor_res = random_number1 + random_number2
        
    elif my_choice == 'subtr':
        operat_quest = 'Question: {0} {1} {2}'.format(random_number1, '-', random_number2)

        cor_res = random_number1 - random_number2
        
    elif my_choice == 'multipl':
        operat_quest = 'Question: {0} {1} {2}'.format(random_number1, '*', random_number2)
       
        cor_res = random_number1 * random_number2
        
    return(operat_quest, cor_res)
