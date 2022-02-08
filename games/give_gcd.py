"""Returns gcd."""


def give_gcd(a, b):
    """Take numbers a and b and returns gcd."""
    while a != 0 and b != 0:
        if a < b:
            a, b = b, a
        a = a % b
    return (a + b)