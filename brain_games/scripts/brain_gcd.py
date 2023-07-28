#!/usr/bin/env python3
from brain_games.games.gcd import game_rule, gcd
from brain_games.engine import game


def main():
    game(game_rule, gcd)


if __name__ == '__main__':
    main()
