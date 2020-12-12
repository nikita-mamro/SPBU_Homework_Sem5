import math


TOPIC = 'Нахождение производных таблично-заданной функции по формулам численного дифференцирования'
F_STRING = 'e ^ (4.5 * x)'

K = 4.5


def f(x):
    return math.exp(K * x)


def df(x):
    return K * math.exp(K * x)


def ddf(x):
    return K * K * math.exp(K * x)
