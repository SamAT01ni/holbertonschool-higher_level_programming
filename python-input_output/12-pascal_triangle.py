#!/usr/bin/python3
""" Pascals triangle module"""


def pascal_triangle(n):
    """pascal was a weird dude"""
    if n <= 0:
        return []

    pascal = [[height for height in range(n) if height < width + 1]
              for width in range(n)]
    for i in range(len(pascal)):
        for j in range(len(pascal[i])):
            val = 1
            if j < i and i > 0 and j > 0:
                val = pascal[i - 1][j] + pascal[i - 1][j - 1]
            pascal[i][j] = val
    return pascal
