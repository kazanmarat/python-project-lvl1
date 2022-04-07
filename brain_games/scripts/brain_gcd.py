#!/usr/bin/env python
"""Do this module main and import functions from other modules."""


from brain_games.games.do_gcd import do_gcd
from dispatch_all import dispatch_all


def main():
    """Define the main function."""
    dispatch_all(do_gcd)


if __name__ == '__main__':
    main()
