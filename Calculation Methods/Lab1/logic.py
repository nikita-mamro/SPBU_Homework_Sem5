def root_separation(f, h, A, B):
    sections = []

    x1 = A
    x2 = A + h
    y1 = f(x1)

    while x2 <= B:
        y2 = f(x2)
        if y1 * y2 <= 0:
            sections.append((x1, x2))
        x1 = x2
        x2 = x1 + h
        y1 = y2

    return sections


def bisection_method(f, a, b, epsilon):
    steps = 0

    while b - a > 2 * epsilon:
        steps += 1
        c = (a + b) / 2
        if f(a) * f(c) <= 0:
            a = c
        else:
            b = c

    x = (a + b) / 2
    return (x, steps, b - a)


def newton_method(f, df, a, b, epsilon, p=1):
    mid = (a + b) / 2
    x_0 = mid if df(mid) != 0 else mid + epsilon
    x_1 = x_0 - f(x_0) / df(x_0)

    steps = 1

    while abs(x_1 - x_0) > epsilon:
        x_0 = x_1
        if df(x_0) == 0:
            return newton_method(f, df, a, b, epsilon, p + 1)
        x_1 = x_0 - f(x_0) * p / df(x_0)
        steps += 1

    return (x_1, steps, abs(x_1 - x_0))


def modified_newton_method(f, df, a, b):
    return 0


def secant_method(f, df, a, b):
    return 0
