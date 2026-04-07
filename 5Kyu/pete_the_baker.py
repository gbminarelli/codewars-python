# https://www.codewars.com/kata/525c65e51bf619685c000059


def cakes(recipe, available):
    return min(available[k] // v if k in available else 0 for k, v in recipe.items())
