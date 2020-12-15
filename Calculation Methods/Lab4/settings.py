import math


def w(x):
    return 1


def f(x):
    # return 10
    # return x
    # return 3 * math.pow(x, 2) + 3 * x - 7
    # return 5 * math.pow(x, 3) + math.pow(x, 2) - 9 * x + 1
    return math.sin(x)


def get_f_as_string():
    # return '10'
    # return 'x'
    # return '3x^2 + 3x - 7'
    # return '5x^3 + x^2 - 9x + 1'
    return 'sin(x)'


def expected(A, B):
    # return (10 * B) - (10 * A)
    # return (math.pow(B, 2) / 2) - (math.pow(A, 2) / 2)
    # return (math.pow(B, 3) + 3/2 * math.pow(B, 2) - 7 * B) - (math.pow(A, 3) + 3/2 * math.pow(A, 2) - 7 * A)
    # return (5/4 * math.pow(B, 4) + 1/3 * math.pow(B, 3) - 9/2 * math.pow(B, 2) + B) - (5/4 * math.pow(A, 4) + 1/3 * math.pow(A, 3) - 9/2 * math.pow(A, 2) + A)
    return -math.cos(B) + math.cos(A)
