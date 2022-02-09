"""Do main calculations and send results to the main."""

from games.ask_name import ask_name
from games.give_list import give_list
from games.numb_to_string import numb_to_string
from games.text_greeting import text_greeting
from random import choice


def do_progr():
    """Do calculates missing number from list."""
    text_greeting()
    guest_name = ask_name()
    print('Hello, {0}!'.format(guest_name))
    print('What number is missing in the progression?')
    text01 = 'Question: {0} '
    text02 = 'Your answer: '
    text03 = "'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!"
    text04 = 'Correct!'
    text05 = 'Congratulations, {0}!'

    n = 0
    while n < 3:
        my_list = give_list()
        my_element = choice(range(len(my_list)))
        my_result = my_list[my_element]
        my_list[my_element] = '..'
        str_list = numb_to_string(my_list)
        n = n + 1

        print(text01.format(str_list))
        answer = int(input(text02))
        if answer != my_result:
            print(text03.format(answer, my_result, guest_name))
            break
        else:
            print(text04)

        if n == 3:
            print(text05.format(guest_name))
