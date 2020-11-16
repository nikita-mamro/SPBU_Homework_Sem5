import math


def w(x):
    return 1


def f(x):
    # return x
    return math.sin(x)


def get_f_as_string():
    return 'x'


def expected(A, B):
    # return math.pow(B, 2) / 2 - math.pow(A, 2) / 2
    return -math.cos(B) + math.cos(B)
