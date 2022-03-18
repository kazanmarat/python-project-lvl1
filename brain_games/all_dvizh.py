"""all_dvizh module. Contains main logic for all brain games."""


from random import randint

import prompt

from brain_games.games.do_calc import do_calc
from brain_games.games.do_even import do_even
from brain_games.games.do_gcd import do_gcd
from brain_games.games.do_prime import do_prime
from brain_games.games.do_progr import do_progr

# flake8: noqa: C901
def all_dvizh(scenario):
    """Do the main logic. In argument scenario - name of function to do."""
    print('Welcome to the Brain Games!')
    MY_CIRCLES = 3
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))

    longtext1 = 'Answer "yes" if the number is even, otherwise answer "no".'
    longtext2 = 'Answer "yes" if given number is prime, otherwise answer "no".'
    var_answers = {
        do_even: longtext1,
        do_calc: 'What is the result of the expression?',
        do_gcd: 'Find the greatest common divisor of given numbers.',
        do_progr: 'What number is missing in the progression?',
        do_prime: longtext2
    }
    print(var_answers[scenario])
    quant = 0
    while quant < MY_CIRCLES:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        if scenario == do_even:
            user_res, cor_res = do_even(num1)
        elif scenario == do_calc:
            user_res, cor_res = do_calc(num1, num2)
        elif scenario == do_gcd:
            user_res, cor_res = do_gcd(num1, num2)
        elif scenario == do_progr:
            user_res, cor_res = do_progr()
        elif scenario == do_prime:
            user_res, cor_res = do_prime(num1)

        if user_res != cor_res:
            print("'{0}' is wrong answer :(.".format(user_res), end='')
            print(" Correct answer was '{0}'.".format(cor_res))
            print("Let's try again, {0}!".format(user_name))
            break

        print('Correct!')
        quant = quant + 1
        if quant == MY_CIRCLES:
            print('Congratulations, {0}!'.format(user_name))
