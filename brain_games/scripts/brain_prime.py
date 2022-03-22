#!/usr/bin/env python
"""Do this module main and import functions from other modules."""

from brain_games.games.do_prime import do_prime
from brain_games.central_function import central_function


def main():
    """Define the main function."""
    central_function(do_prime)


if __name__ == '__main__':
    main()
