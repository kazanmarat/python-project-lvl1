"""Return a greeting."""


import prompt


def welcome_user():
    """Ask a name."""
    name = prompt.string('May I have your name? ')

    print('Hello, {0}!'.format(name))
