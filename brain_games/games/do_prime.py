"""Module do_prime. It calculates if the given number is prime."""



def do_prime(num1):
    """Calculate number and return True if it is prime.
    Parameter - random number num1.
    Returns - is it prime.
    """
    text01 = 'Question: {0}'
    text02 = 'Your answer: '
    print(text01.format(num1))
    user_res = input(text02)

    cor_res = 'yes'
    limiter = int((num1 ** 0.5) + 1)
    for i in range(2, limiter):
        if num1 % i == 0:
            cor_res = 'no'

    return (user_res, cor_res)
