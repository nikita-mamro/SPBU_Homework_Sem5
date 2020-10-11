import settings


def create_table(a, m, h):
    table = []
    f = settings.f
    for j in range(0, m + 1):
        x = a + j * h
        table.append((j, x, f(x)))

    return table


def create_d_table(table, h):
    xfdf_table = []

    for (i, xj, _) in table:
        xfdf_table.append(
            (i, xj, settings.f(xj), settings.df(xj), settings.ddf(xj)))

    d_table = []

    for (i, x, fx, df, ddf) in xfdf_table:
        d = 0
        dd = 0
        if i == 0:
            d = (-3 * table[i][2] + 4 * table[i + 1]
                 [2] - table[i + 2][2]) / (2 * h)
        elif i == len(xfdf_table) - 1:
            d = (3 * table[i][2] - 4 * table[i - 1]
                 [2] + table[i - 2][2]) / (2 * h)
        else:
            d = (table[i + 1][2] - table[i - 1][2]) / (2 * h)
            dd = (table[i + 1][2] - 2 * table[i]
                  [2] + table[i - 1][2]) / (h ** 2)

        if i == 0 or i == len(xfdf_table) - 1:
            d_table.append((str(x), str(fx), str(
                d), str(abs(d - df)), '-', '-'))
        else:
            d_table.append((str(x), str(fx), str(d), str(
                abs(d - df)), str(dd), str(abs(dd - ddf))))

    return d_table
