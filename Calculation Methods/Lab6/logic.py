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
          'j', 'x', 'Найденный y', 'Погрешность'], tablefmt='orgtbl'))


def print_teylor_table(taylor_y, expected_table):
    print_error_table(taylor_y, expected_table)


def find_adams():
    return []


def print_adams_table():
    return


def find_runge_kutta(N, h, x0, y0, d1y):
    nodes = get_nodes(x0, N, h)
    res = [0] * (N + 1)
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
    return


def find_euler(N, h, x0, y0, d1y):
    nodes = get_nodes(x0, N, h)
    res = [0] * (N + 1)
    res[0] = y0
    non_negative_nodes = nodes[2:]

    for i in range(1, len(res)):
        res[i] = res[i - 1] + h * d1y(non_negative_nodes[i - 1], res[i - 1])

    return res


def print_euler_table(N, h, x0, y0, d1y):
    e_y = find_euler(N, h, x0, y0, d1y)
    return


def find_eulerI(N, h, x0, y0, d1y):
    nodes = get_nodes(x0, N, h)
    res = [0] * (N + 1)
    res[0] = y0
    non_negative_nodes = nodes[2:]
    return res


def print_eulerI_table():
    return


def find_eulerII():
    return []


def print_eulerII_table():
    return
