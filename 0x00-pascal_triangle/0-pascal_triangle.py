#!/usr/bin/python3
""" pascal traingle"""


def pascal_triangle(n):
    """ function that returns the pascal triangle"""
    if n <= 0:
        return []
    triangle = [[1]]
    while len(triangle) < n:
        row = [a + b for a, b in zip([0] + triangle[-1], triangle[-1] + [0])]
        triangle.append(row)
    return triangle
