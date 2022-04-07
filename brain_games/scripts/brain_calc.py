#!/usr/bin/env python
"""Do this module main and import functions from other modules."""

from brain_games.games.do_calc import do_calc
from dispatch_all import dispatch_all


def main():
    """Define the main function."""
    dispatch_all(do_calc)


if __name__ == '__main__':
    main()
