import math

TOPIC = 'Задача обратного интерполирования'
F_STRING = 'e\u207bˣ - x\u00b2 / 2'


def x_j(j, m, a, b):
    return a + j * (b - a) / m


def f(x):
    return math.e ** x - x ** 2 / 2
