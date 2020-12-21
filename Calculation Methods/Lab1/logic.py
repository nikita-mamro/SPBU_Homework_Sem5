def root_separation(f, N, A, B):
    sections = []
    h = (B - A) / N

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
    mid = (a + b) / 2
    steps = 0

    c = (a + b) / 2

    while b - a > epsilon:
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
        steps += 1
        c = (a + b) / 2

    x = (a + b) / 2
    return (mid, x, steps, b - a)


def newton_method(f, df, a, b, epsilon, p=1):
    mid = (a + b) / 2
    x_k = mid if df(mid) != 0 else mid + epsilon
    x_k1 = x_k - f(x_k) / df(x_k)

    steps = 1

    while abs(x_k1 - x_k) > epsilon:
        x_k = x_k1
        if df(x_k) == 0:
            return newton_method(f, df, a, b, epsilon, p + 1)
        x_k1 = x_k - f(x_k) * p / df(x_k)
        steps += 1

    return (mid, x_k1, steps, abs(x_k1 - x_k))


def modified_newton_method(f, df, a, b, epsilon):
    mid = (a + b) / 2
    x_k = mid if df(mid) != 0 else mid + epsilon
    mid = x_k
    x_k1 = x_k - f(x_k) / df(mid)

    steps = 1

    while abs(x_k1 - x_k) > epsilon:
        x_k = x_k1
        x_k1 = x_k - f(x_k) / df(mid)
        steps += 1

    return (mid, x_k1, steps, abs(x_k1 - x_k))


def secant_method(f, a, b, epsilon):
    x_k = a
    x_k1 = b

    steps = 0

    while abs(x_k1 - x_k) > epsilon:
        x_k1_tmp = x_k1
        x_k1 = x_k - f(x_k) * (x_k - x_k1) / (f(x_k) - f(x_k1))
        x_k = x_k1_tmp
        steps += 1

    return (a, b, x_k1, steps, abs(x_k1 - x_k))
