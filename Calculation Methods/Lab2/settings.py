import math

TOPIC = 'Задача алгебраического интерполирования'
F_STRING = 'e\u207bˣ - x\u00b2 / 2'
VARIANT = '7 вариант'

A = 0
B = 1
x = 0.65
n = 7
m = 15


def x_j(j, m, a, b):
    return a + j * (b - a) / m


def f(x):
    return math.e ** x - x ** 2 / 2
