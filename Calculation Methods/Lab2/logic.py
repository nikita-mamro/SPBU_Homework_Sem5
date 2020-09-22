import settings


def create_table(m, A, B, f):
    table = []
    for j in range(0, m + 1):
        x = settings.x_j(j, m, A, B)
        table.append((j, x, f(x)))

    return table


def get_polynom_value(x, n, table, f):
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

        result += numerator / denominator * f(x_k)

    return result
