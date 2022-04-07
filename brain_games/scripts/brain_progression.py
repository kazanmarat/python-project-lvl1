#!/usr/bin/env python

"""Do this module main and import functions from other modules."""

from brain_games.games.do_progr import do_progr
from dispatch_all import dispatch_all


def main():
    """Define the main function."""
    dispatch_all(do_progr)


if __name__ == '__main__':
    main()
