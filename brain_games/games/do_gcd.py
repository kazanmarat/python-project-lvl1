"""Module do_gcd. Calculates the greatest common divisor."""


def do_gcd(num1, num2):
    """Take given numbers num1 and num2 and returns gcd.
    Parameters: a and b are random numbers.
    Returns: the greatest common divisor.
    """
    text01 = 'Question: {0} {1}'
    text02 = 'Your answer: '
    print(text01.format(num1, num2))
    while (num2):
        num1, num2 = num2, num1 % num2
    cor_res = num1
    user_res = int(input(text02))
    return (user_res, cor_res)
