import settings


def create_d_table(a, m, h):
    xfdf_table = []

    for i in range(0, m + 1):
        xj = a + i * h
        xfdf_table.append(
            (i, xj, settings.f(xj), settings.df(xj), settings.ddf(xj)))

    d_table = []

    f = settings.f

    for (i, x, fx, df, ddf) in xfdf_table:
        d = 0
        dd = 0
        if i == 0:
            d = (-3 * f(x) + 4 * f(x + h) - f(x + 2 * h)) / (2 * h)
        elif i == len(xfdf_table) - 1:
            d = (3 * f(x) - 4 * f(x + h) - f(x + 2 * h)) / (2 * h)
        else:
            d = (f(x + h) - f(x - h)) / (2 * h)
            dd = (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)

        if i == 0 or i == len(xfdf_table) - 1:
            d_table.append((str(x), str(fx), str(d), str(abs(d - df)), '', ''))
        else:
            d_table.append((str(x), str(fx), str(d), str(
                abs(d - df)), str(dd), str(abs(dd - ddf))))

    return d_table
