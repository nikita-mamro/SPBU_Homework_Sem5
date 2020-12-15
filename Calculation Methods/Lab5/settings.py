import math

M = 5
N = 100


def fG(x):
    return math.sin(x)


def wG(x):
    return abs(x - 0.5)


def fM(x):
    return math.sin(x)


def fM_expected(x):
    return -math.cos(x)
