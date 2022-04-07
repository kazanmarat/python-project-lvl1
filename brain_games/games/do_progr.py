"""Module do_progr. Creates list of numbers and returns result to the main."""

from random import choice


def do_progr():
    """Do calculation of missing number from list.
    Create list my_list with quantity of numbs elemetns.
    The step between elements is in list steps.
    In my_list one random element is replaced
    by '..' and user must answer, which element.
    """
    FUNC_TXT = 'What number is missing in the progression?'
    numbs = choice([5, 6, 7, 8, 9, 10])
    steps = choice([2, 3, 4, 5, 6, 7, 8, 9])
    my_list = [i * steps for i in range(numbs)]
    my_element = choice(range(len(my_list) - 1))
    correct_result = my_list[my_element]
    my_list[my_element] = '..'
    chars = []
    for number in my_list:
        chars.append(str(number))
    str_for_numbs = (' '.join(chars))
    operat_question = '{0}'.format(str_for_numbs)
    return (operat_question, correct_result, FUNC_TXT)
