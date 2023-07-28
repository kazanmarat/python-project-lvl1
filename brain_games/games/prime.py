"""This module asks is the number is prime.
Returns a random number and the right answer."""
import random


def check_prime(num):
    """Check if a number is prime.
    If prime, then returns 'yes', otherwise - 'no'."""
    if num == 0 or num == 1:
        return 'no'
    if num == 2:
        return 'yes'
    upper_limit = int(num ** 0.5) + 1
    i = 2
    while i <= upper_limit:
        if num % i == 0:
            return 'no'
        i += 1
    return 'yes'


def random_and_check():
    """Calls the 'random.randint' function
    to generate a random number between 0 and 100.
    Then calls the 'check_prime' function
    to check number is prime.
    Returns a random number and the correct answer."""
    random_num = random.randint(0, 100)
    right_answer = check_prime(random_num)
    return random_num, right_answer


game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
