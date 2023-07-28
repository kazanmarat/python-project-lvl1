#!/usr/bin/env python3
from brain_games.games.calc import game_rule, operation_count
from brain_games.engine import game


def main():
    game(game_rule, operation_count)


if __name__ == '__main__':
    main()
