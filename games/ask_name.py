"""Returns a name of guest."""


import prompt


def ask_name():
    """Ask and returns a name."""
    g_name = prompt.string('May I have your name? ')
    return g_name