import math

TOPIC = "Численные методы решения нелинейных уравнений"
EPSILON = 0.00001
A = -8
B = 2
F_STRING = "10 * cos(x) - 0.1 * x\u00b2"


def f(x):
    return 10 * math.cos(x) - 0.1 * x ** 2


def df(x):
    return -10 * math.sin(x) - 0.2 * x
