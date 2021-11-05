#!/usr/bin/env python


"""Do this module main and import functions from other modules."""


from brain_games.cli import welcome_user


def main():
    """It is the main function."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
