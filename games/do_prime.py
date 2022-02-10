"""Do main calculations and send results to the main."""

from games.ask_name import ask_name
from games.give_rand_numb import give_rand_int
from games.is_prime import is_prime
from games.text_greeting import text_greeting

def do_prime():
    """Do calculates is number - prime."""
    text_greeting()
    guest_name = ask_name()
    print('Hello, {0}!'.format(guest_name))
    print('Answer "yes" if given number is prime. ', end='')
    print('Otherwise answer "no".')
    text01 = 'Question: {0} '
    text02 = 'Your answer: '
    text03 = "'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!"
    text04 = 'Correct!'
    text05 = 'Congratulations, {0}!'

    n = 0
    while n < 3:
        numb1 = give_rand_int()
        n = n + 1

        if is_prime(numb1):
            my_result = 'yes'
        else:
            my_result = 'no'
        print(text01.format(numb1))
        answer = input(text02)
        if answer != my_result:
            print(text03.format(answer, my_result, guest_name))
            break
        else:
            print(text04)

        if n == 3:
            print(text05.format(guest_name))
