#!/usr/bin/env python3
from brain_games.games.progression import game_rule, hide_element
from brain_games.engine import game


def main():
    game(game_rule, hide_element)


if __name__ == '__main__':
    main()
