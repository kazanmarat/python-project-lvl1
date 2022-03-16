#!/usr/bin/env python


"""Do this module main and import functions from other modules."""

from brain_games.games.do_even import do_even
from brain_games.all_dvizh import all_dvizh


def main():
    """Define the main function."""
    all_dvizh(do_even)


if __name__ == '__main__':
    main()
