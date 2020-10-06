import math

TOPIC = 'Задача алгебраического интерполирования (мн-н Ньютона)'
F_STRING = 'e\u207bˣ - x\u00b2 / 2'
VARIANT = '7 вариант'


def x_j(j, m, a, b):
    return a + j * (b - a) / m


def f(x):
    return math.e ** x - x ** 2 / 2


def p(x):
    return (4, 2 * x ** 4 + 0.32 * x ** 3 + x + 10.2)
