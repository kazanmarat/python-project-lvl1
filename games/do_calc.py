"""Do main calculations and send results to the main."""

from games.ask_name import ask_name
from games.give_rand_numb import give_rand_int
from games.text_greeting import text_greeting
from random import choice


def do_calc():
    """Do calculates brain_calc."""
    text_greeting()
    guest_name = ask_name()
    print('Hello, {0}!'.format(guest_name))
    print('What is the result of the expression?')

    text01 = 'Question: {0} {1} {2}'
    text02 = 'Your answer: '
    text03 = "'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!"
    text04 = 'Correct!'
    text05 = 'Congratulations, {0}!'

    n = 0
    while n < 3:
        numb1 = give_rand_int()
        numb2 = give_rand_int()

        my_choice = choice(['add', 'subtr', 'multipl'])
        n = n + 1

        if my_choice == 'add':
            print(text01.format(numb1, '+', numb2))
            answer = int(input(text02))
            result_add = numb1 + numb2

            if answer != result_add:
                print(text03.format(answer, result_add, guest_name))
                break
            else:
                print(text04)

        elif my_choice == 'subtr':
            print(text01.format(numb1, '-', numb2))
            answer = int(input(text02))
            result_subtr = numb1 - numb2

            if answer != result_subtr:
                print(text03.format(answer, result_subtr, guest_name))
                break
            else:
                print(text04)

        elif my_choice == 'multipl':
            print(text01.format(numb1, '*', numb2))
            answer = int(input(text02))
            result_multipl = numb1 * numb2

            if answer != result_multipl:
                print(text03.format(answer, result_multipl, guest_name))
                break
            else:
                print(text04)

        if n == 3:
            print(text05.format(guest_name))
