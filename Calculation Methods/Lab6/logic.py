from tabulate import tabulate


def get_expected_table(x0, N, h, y_expected):
    table = []
    x = x0
    for k in range(-2, N + 1):
        xi = x + k * h
        y = y_expected(xi)
        table.append((k, xi, y))
    return table


def print_expected_table(x0, N, h, y_expected):
    table = get_expected_table(x0, N, h, y_expected)
    print(tabulate(table, headers=[
          'j', 'x', 'y'], tablefmt='orgtbl'))


def print_derivatives(derivatives):
    i = 0
    for d in derivatives:
        print('f^(', i, ') = ', d)
        i += 1


def get_nodes(x0, N, h):
    nodes = []
    x = x0
    for k in range(-2, N + 1):
        xi = x + k * h
        nodes.append(xi)
    return nodes


def find_taylor(derivatives, x0, N, h):
    factorial = 1
    coefs = []

    for i in range(0, len(derivatives)):
        coefs.append(derivatives[i] / factorial)
        factorial *= i + 1

    res = []
    nodes = get_nodes(x0, N, h)

    for i in range(0, len(nodes)):
        res.append(0)
        for j in range(0, len(coefs)):
            res[i] += coefs[j] * (nodes[i] - x0) ** j

    return res


def print_error_table(found_column, expected_table, skip=0):
    table = []
    for i in range(skip, len(found_column)):
        # (j, xj, yj_found, |yj_found - yj_expected|)
        el = (expected_table[i][0], expected_table[i][1], found_column[i],
              abs(expected_table[i][2] - found_column[i]))
        table.append(el)

    print(tabulate(table, headers=[
          'j', 'x', 'Найденный y', 'Погрешность'], tablefmt='orgtbl', floatfmt='.11f'))


def print_teylor_table(taylor_y, expected_table):
    print_error_table(taylor_y, expected_table)


def find_adams(N, h, x0, y0, d1y, expected_table):
    def qj(h, dy, xj, yj):
        return h * dy(xj, yj)

    nodes = get_nodes(x0, N, h)

    first_five_rows = expected_table[0:5]
    # (x-2; y(x_-2)), ..., (x2; y(x2))
    first_five_y = []
    for row in first_five_rows:
        first_five_y.append(row[2])
    # For x_3, x_4, ... find adams res
    res = []

    res = first_five_y + [0] * (N - 2)

    # q_-2, q_-1, ..., q_N
    qjs = [0] * (N + 3)
    for j in range(0, min(len(qjs), 5)):
        qjs[j] = qj(h, d1y, nodes[j], first_five_y[j])

    # qs: table with columns q, d1, d2, d3, d4
    qs = []
    qs.append(qjs)

    for s in range(1, 5):
        dsqs = []
        for j in range(0, len(qs[s - 1]) - 1):
            dsqs.append(qs[s - 1][j + 1] - qs[s - 1][j])
        qs.append(dsqs)

    for j in range(3, N + 3):
        q_m = qs[0][j - 1]
        dq_m1 = qs[1][j - 2]
        d2q_m2 = qs[2][j - 3]
        d3q_m3 = qs[3][j - 4]
        d4q_m4 = qs[4][j - 5]
        res[j] = res[j - 1] + q_m + dq_m1 / 2.0 + 5 * d2q_m2 / \
            12.0 + 3 * d3q_m3 / 8.0 + 251 * d4q_m4 / 720.0

    return res


def print_adams_table(adams_y, expected_table):
    print_error_table(adams_y, expected_table, 5)


def find_runge_kutta(N, h, x0, y0, d1y):
    nodes = get_nodes(x0, N, h)
    res = [0] * N
    res[0] = y0
    non_negative_nodes = nodes[2:]

    for i in range(1, len(res)):
        k1 = h * d1y(non_negative_nodes[i - 1], res[i - 1])
        k2 = h * d1y(non_negative_nodes[i - 1] + h / 2, res[i - 1] + k1 / 2)
        k3 = h * d1y(non_negative_nodes[i - 1] + h / 2, res[i - 1] + k2 / 2)
        k4 = h * d1y(non_negative_nodes[i], res[i - 1] + k3)
        res[i] = res[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return res


def print_runge_kutta_table(rk_y, expected_table):
    rk_y = [0] * 3 + rk_y
    print_error_table(rk_y, expected_table, 3)


def find_euler(N, h, x0, y0, d1y):
    nodes = get_nodes(x0, N, h)
    res = [0] * N
    res[0] = y0
    non_negative_nodes = nodes[2:]

    for i in range(1, len(res)):
        res[i] = res[i - 1] + h * d1y(non_negative_nodes[i - 1], res[i - 1])

    return res


def print_euler_table(eu_y, expected_table):
    eu_y = [0] * 3 + eu_y
    print_error_table(eu_y, expected_table, 3)


def find_eulerI(N, h, x0, y0, d1y):
    nodes = get_nodes(x0, N, h)
    res = [0] * N
    res[0] = y0
    non_negative_nodes = nodes[2:]
    half_h = h / 2

    for i in range(1, len(res)):
        mid = res[i - 1] + half_h * d1y(non_negative_nodes[i - 1], res[i - 1])
        res[i] = res[i - 1] + h * d1y(non_negative_nodes[i - 1] + half_h, mid)

    return res


def print_eulerI_table(euI_y, expected_table):
    euI_y = [0] * 3 + euI_y
    print_error_table(euI_y, expected_table, 3)


def find_eulerII(N, h, x0, y0, d1y):
    nodes = get_nodes(x0, N, h)
    res = [0] * N
    res[0] = y0
    non_negative_nodes = nodes[2:]
    half_h = h / 2

    for i in range(1, len(res)):
        prevD1y = d1y(non_negative_nodes[i - 1], res[i - 1])
        prevVal = res[i - 1] + h * prevD1y
        res[i] = res[i - 1] + half_h * \
            (d1y(non_negative_nodes[i], prevVal) + prevD1y)

    return res


def print_eulerII_table(euII_y, expected_table):
    euII_y = [0] * 3 + euII_y
    print_error_table(euII_y, expected_table, 3)


def print_yn_absolute_error(taylor_y, adams_y, rk_y, eu_y, euI_y, euII_y, expected_table):
    print('Метод разложения в ряд Тейлора: ', abs(
        taylor_y[-1] - expected_table[-1][2]))
    print('Метод Адамса 4-го порядка: ', abs(
        adams_y[-1] - expected_table[-1][2]))
    print('Метод Рунге-Кутта 4-го порядка: ', abs(
        rk_y[-1] - expected_table[-1][2]))
    print('Метод Эйлера: ', abs(
        eu_y[-1] - expected_table[-1][2]))
    print('Метод Эйлера I: ', abs(
        euI_y[-1] - expected_table[-1][2]))
    print('Метод Эйлера II: ', abs(
        euII_y[-1] - expected_table[-1][2]))


def print_a_rk_error(adams_y, rk_y, expected_table):
    print('Метод Адамса 4-го порядка: ', abs(
        adams_y[-1] - expected_table[-1][2]))
    print('Метод Рунге-Кутта 4-го порядка: ', abs(
        rk_y[-1] - expected_table[-1][2]))
