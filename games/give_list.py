"""Returns the random list with random step."""

from random import choice


def give_list():
    """Take integers. Returns the random list with random step."""
    numbs = choice([5, 6, 7, 8, 9, 10])
    steps = choice([2, 3, 4, 5, 6, 7, 8, 9])
    return [i * steps for i in range(numbs)]