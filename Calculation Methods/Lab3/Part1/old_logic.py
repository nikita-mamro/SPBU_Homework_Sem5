import settings


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

    while b - a > epsilon:
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

    for i in range(0, n + 1):
        x_i = table[i][1]
        y_i = table[i][2]

        mul = 1

        for j in range(0, n + 1):
            if i != j:
                a = x - table[j][1]
                b = x_i - table[j][1]
                mul *= a / b

        result += mul * y_i

    return result


def get_polynom_newton(x0, n, table):
    def polynom(x):
        table.sort(key=lambda xf: abs(xf[1] - x0))

        newton_table = [[None for col in range(0, n + 2)]
                        for row in range(0, n + 1)]

        for row in range(0, n + 1):
            newton_table[row][0] = table[row][1]
            newton_table[row][1] = table[row][2]

        for col in range(2, n + 2):
            for row in range(0, n + 2 - col):
                numerator = newton_table[row + 1][col -
                                                  1] - newton_table[row][col - 1]

                first_index_in_column = col - 1

                x_index = first_index_in_column + row

                denumerator = newton_table[x_index][0] - newton_table[row][0]

                newton_table[row][col] = numerator / denumerator

        res = 0

        for i in range(0, n + 1):
            ai = newton_table[0][i + 1]

            for j in range(0, i):
                ai *= x - newton_table[j][0]

            res += ai

        return res

    return polynom(x0)
