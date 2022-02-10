"""Give number. It calculates - is it prime."""


def is_prime(numb):
    """Give number. Calculates numb and returns True is it prime."""
    if numb <= 1:
        return False
    limiter = int((numb ** 0.5) + 1)
    for i in range (2, limiter):
        if numb % i == 0:
            return False
    return True
