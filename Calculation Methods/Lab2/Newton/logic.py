import settings


def create_table(m, A, B, f):
    table = []
    for j in range(0, m + 1):
        x = settings.x_j(j, m, A, B)
        table.append((j, x, f(x)))

    return table


def get_polynom_newton(x0, n, table, f):
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

                denumerator = newton_table[x_index][0] - newton_table[0][0]

                newton_table[row][col] = numerator / denumerator

        res = 0

        for i in range(0, n + 1):
            ai = newton_table[0][i + 1]

            for j in range(0, i):
                ai *= x - newton_table[j][0]

            res += ai

        return res

    return polynom
