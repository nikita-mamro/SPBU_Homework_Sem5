import math


def find_middle_rectangle(a, b, f, m):
    h = (b - a) / m
    res = 0
    for i in range(0, m):
        res += f(a + i * h + h / 2)

    return res * h


def find_gauss(f, a, b, m):
    h = (b - a) / m
    half_h = h / 2
    shift = half_h / math.sqrt(3)

    res = 0
    mid = half_h

    for _ in range(0, m):
        res += f(mid - shift) + f(mid + shift)
        mid += h

    return res * half_h


def find_gauss_like(f, w, a, b, logging_enabled):
    print('----- Построение КФ Гаусса -----')
    m = 100000

    mu0 = find_middle_rectangle(a, b, w, m)
    mu1 = find_middle_rectangle(a, b, lambda x: w(x) * x, m)
    mu2 = find_middle_rectangle(a, b, lambda x: w(x) * x * x, m)
    mu3 = find_middle_rectangle(a, b, lambda x: w(x) * x * x * x, m)

    if logging_enabled:
        print('Моменты 0-3:')
        print('mu0: ', mu0)
        print('mu1: ', mu1)
        print('mu2: ', mu2)
        print('mu3: ', mu3)

    cramer1 = ((mu0 * mu3) - (mu2 * mu1)) / (mu1 ** 2 - mu2 * mu0)
    cramer2 = (mu2 ** 2 - mu3 * mu1) / (mu1 ** 2 - mu2 * mu0)

    if logging_enabled:
        print('Орт. мн-н x^2 + ', cramer1, 'x + ', cramer2)

    sqrtD = math.sqrt(cramer1 ** 2 - 4 * cramer2)

    x1 = (-cramer1 + sqrtD) / 2
    x2 = (-cramer1 - sqrtD) / 2

    if logging_enabled:
        print('Узел 1: ', x1)
        print('Узел 2: ', x2)

    A1 = (mu1 - x2 * mu0) / (x1 - x2)
    A2 = (mu1 - x1 * mu0) / (x2 - x1)

    if logging_enabled:
        print('Коэф. КФ A1: ', A1)
        print('Коэф. КФ A2: ', A2)
        print('A1 + A2 = ', A1 + A2, ' mu0 = ', mu0)

    print('----------------------------')

    return A1 * f(x1) + A2 * f(x2)


def find_meler(f, n, logging_enabled):
    s = 0

    if (logging_enabled):
        print('\n\nКФ Мелера: ')
        print('---------------')

    for i in range(1, n + 1):
        xi = math.cos(math.pi * (2 * i - 1) / (2 * n))
        if (logging_enabled):
            print('Узел ', i, ': ', xi)
        s += f(xi)

    k = math.pi / n
    if (logging_enabled):
        print('Коэффициенты: ', k)

    print('\n\n')

    return s * k
