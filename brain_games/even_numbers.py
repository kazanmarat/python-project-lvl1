"""Return a correct answers."""

from random import randint

import prompt

print('Welcome to the Brain Games!')

text01 = 'Answer "yes" if the number is even, otherwise answer "no. '
text_wrong_ans1 = "'yes' is wrong answer ;(. Correct answer was 'no'."
text_wrong_ans2 = "Let\'s try again, {0}!"


def even_numb():
    """Greet and ask a name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

    count = 0
    while count < 3:
        num = randint(0, 100)
        answ = prompt.string
        print(text01)
        print('Question: {0}'.format(num))
        answ = input('Your answer: ')
        n_even = num % 2
        if (n_even == 0 and answ == 'yes') or (n_even != 0 and answ == 'no'):
            print('Correct!')
            count = count + 1
            if count == 3:
                print('Congratulations, {0}!'.format(name))
        elif (n_even % 2 != 0 and answ != 'no'):
            print(text_wrong_ans1)
            print(text_wrong_ans2.format(name))
            break
        elif (n_even % 2 == 0 and answ != 'yes'):
            print(text_wrong_ans1)
            print(text_wrong_ans2.format(name))
            break
