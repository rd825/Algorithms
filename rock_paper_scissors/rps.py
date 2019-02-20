#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    options = ['rock', 'paper', 'scissors']  # the options each player has
    plays = []  # the results of each round

    def find_outcome(rounds, result=[]):
        if rounds == 0:
            plays.append(result)
            return
        for option in options:
            find_outcome(rounds - 1, result + [option])
    find_outcome(n, [])
    return plays


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
