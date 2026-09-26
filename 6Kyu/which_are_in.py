# https://www.codewars.com/kata/550554fd08b86f84fe000a58


def in_array(array1, array2):
    return sorted({a for a in array1 if any(a in b for b in array2)})
