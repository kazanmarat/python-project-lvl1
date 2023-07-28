#!/usr/bin/env python3
from brain_games.games.prime import game_rule, random_and_check
from brain_games.engine import game


def main():
    game(game_rule, random_and_check)


if __name__ == '__main__':
    main()
