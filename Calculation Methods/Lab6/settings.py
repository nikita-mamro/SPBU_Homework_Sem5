import math

H = 0.1
N = 10

X0 = 0
Y0 = 1


def y_expected(x):
    return (math.e ** (-x) + math.sin(x) + math.cos(x)) * 0.5


def d1y(x, y):
    return -y + math.cos(x)


def d2y(x, y):
    return -d1y(x, y) + math.sin(x)


def d3y(x, y):
    return -d2y(x, y) - math.cos(x)


def d4y(x, y):
    return -d3y(x, y) - math.sin(x)
