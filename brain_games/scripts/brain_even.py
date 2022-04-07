#!/usr/bin/env python


"""Do this module main and import functions from other modules."""

from brain_games.games.do_even import do_even
from brain_games.dispatch_all import dispatch_all



def main():
    """Define the main function."""
    dispatch_all(do_even)


if __name__ == '__main__':
    main()
