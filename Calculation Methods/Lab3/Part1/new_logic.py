import settings


def get_reversed_table(table):
    res = []
    for (j, x, f) in table:
        res.append((j, f, x))

    return res


def get_polynom_newton(x, n, table, f, F):
    def polynom(x):
        table.sort(key=lambda xf: abs(xf[1] - x))

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

                denumerator = newton_table[x_index][0] - newton_table[0][0]

                newton_table[row][col] = numerator / denumerator

        res = 0

        for i in range(0, n + 1):
            ai = newton_table[0][i + 1]

            for j in range(0, i):
                ai *= x - newton_table[j][0]

            res += ai

        return res - F

    return polynom
