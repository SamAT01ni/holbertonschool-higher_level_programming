#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    val = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    sum = 0
    i = 0
    while i < len(roman_string):
        currentval = val[roman_string[i]]
        if (i+1 < len(roman_string) and
                val[roman_string[i]] < val[roman_string[i + 1]]):
            sum = sum + val[roman_string[i + 1]] - currentval
            i += 2
        else:
            sum += currentval
            i += 1
    return sum
