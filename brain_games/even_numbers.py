"""Return a correct answers."""

from random import randint

import prompt

print('Welcome to the Brain Games!')


def even_numb():
    """Greet and ask a name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

    count = 0
    while count < 3:
        num = randint(0, 100)
        print(num)
        answ = prompt.string('Answer "yes" if the '
                               'number is even, '
                               'ohterwise answer "no". ')
        n_even = num % 2
        if (n_even == 0 and answ == 'yes') or (n_even != 0 and answ == 'no'):
            print('Your answer: {0}\nCorrect!'.format(answ))
            count = count + 1
            if count == 3:
                print('Congratulations, {0}!'.format(name))
        elif (n_even % 2 != 0 and answ != 'no'):
            print(
                "'yes' is wrong answer ;(. Correct "
                "answer was 'no'.\nLet\'s try again, {0}.".format(name))
            break
        elif (n_even % 2 == 0 and answ != 'yes'):
            print(
                "'no' is wrong answer ;(. Correct "
                "answer was 'yes'.\nLet\'s try again, {0}.".format(name))
            break
