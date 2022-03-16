"""Module do_even. Calculates evenness of given number."""


def do_even(num1):
    """do_even takes argument and returns evenness.
    Parameter: num1 is random number
    Returns:  is num1 is even.
    """
    text01 = 'Question: {0}'
    text02 = 'Your answer: '
    if num1 % 2 == 0:
        cor_res = 'yes'
    else:
        cor_res = 'no'
    print(text01.format(num1))
    user_res = input(text02)
    return (user_res, cor_res)
