#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    req = list(recipe.values())
    avail = list(ingredients.values())
    if len(req) != len(avail):
        return 0
    division = [avail[i]/req[i] for i in range(0, len(req))]
    if min(division) < 1:
        return 0
    else:
        return int(min(division))


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    # print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
    #     batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
