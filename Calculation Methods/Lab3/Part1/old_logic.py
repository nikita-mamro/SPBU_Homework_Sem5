import settings


def bisection_method(f, a, b, epsilon):
    mid = (a + b) / 2
    steps = 0

    while b - a > 2 * epsilon:
        steps += 1
        c = (a + b) / 2
        if f(a) * f(c) <= 0:
            a = c
        else:
            b = c

    x = (a + b) / 2
    return (mid, x, steps, b - a)


def create_table(m, A, B, f):
    table = []
    for j in range(0, m + 1):
        x = settings.x_j(j, m, A, B)
        table.append((j, x, f(x)))

    return table


def get_polynom_value_lagrange(x, n, table):
    table.sort(key=lambda xf: abs(xf[1] - x))

    result = 0

    for k in range(0, n + 1):
        numerator = 1
        denominator = 1
        x_k = table[k][1]

        # Get numerator
        for i in range(0, n + 1):
            if i != k:
                numerator *= x - table[i][1]
        # Get denominator
        for i in range(0, n + 1):
            if i != k:
                denominator *= x_k - table[i][1]

        result += numerator / denominator * table[k][2]

    return result
