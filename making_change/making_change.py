#!/usr/bin/python

import sys


def making_change(amount, denominations):
    return change(amount, denominations, len(denominations))


def change(amount, denomination, length):
    if amount == 0:
        return 1
    elif amount < 0:
        return 0
    elif (length <= 0 and amount >= 1):
        return 0
    else:
        return change(amount, denomination, length - 1) + change(amount - denomination[length - 1], denomination, length)


print(making_change(10, [1, 5, 10, 25, 50]))

# if __name__ == "__main__":
#     # Test our your implementation from the command line
#     # with `python making_change.py [amount]` with different amounts
#     if len(sys.argv) > 1:
#         denominations = [1, 5, 10, 25, 50]
#         amount = int(sys.argv[1])
#         print("There are {ways} ways to make {amount} cents.".format(
#             ways=making_change(amount, denominations), amount=amount))
#     else:
#         print("Usage: making_change.py [amount]")
