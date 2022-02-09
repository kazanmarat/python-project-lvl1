"""Converts list of numbers to list of strings."""


def numb_to_string(numbers):
    """
    Converts list of numbers.
       Another variant:
        (' '.join(map(str.my_list)))
    """
    chars = []
    for number in numbers:
        chars.append(str(number))
    return (' '.join(chars))