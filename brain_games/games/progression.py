"""A list is created with a progression length
of 5 to 10 numbers with the same interval.
The length and spasing are chosen randomly.
The random number is replaced with '..' and
the question is 'What number is missing
in the progression?'"""
import random


def create_list():
    """A list is created with a progression length
of 5 to 10 numbers with the same interval.
The length and spasing are chosen randomly."""
    progression_list = []
    list_length = random.randint(5, 10)
    first_elem = random.randint(1, 20)
    random_step = random.randint(2, 8)
    i = 0
    while i <= list_length:
        progression_list.append(first_elem)
        first_elem += random_step
        i += 1
    return progression_list


def list_to_string(my_list):
    """Converts the elements of a list to a string."""
    string_list = ''
    for i in my_list:
        string_list += str(i) + ' '
    return string_list


def hide_element():
    """Selects a random element from
    the list and replaces it with '..'.
    Returns the string for the question
    to the player and the correct answer."""
    created_list = create_list()
    list_length = len(created_list)
    choice_element = random.randint(0, list_length - 1)
    answer = created_list[choice_element]
    created_list[choice_element] = '..'
    string_list = list_to_string(created_list)
    return string_list, str(answer)


game_rule = 'What number is missing in the progression?'
