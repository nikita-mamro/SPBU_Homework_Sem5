def find_left_rectangle_j(A, f, m, h):
    res = 0
    for i in range(0, m):
        res += f(A + i * h)

    return res * h


def find_right_rectangle_j(A, f, m, h):
    res = 0
    for i in range(1, m + 1):
        res += f(A + i * h)

    return res * h


def find_middle_rectangle_j(A, f, m, h):
    res = 0
    for i in range(1, m):
        res += f(A + i * h)

    return res * h


def find_trapezoid_j(A, B, f, m, h):
    res = 0
    for i in range(0, m):
        x1 = A + i * h
        x2 = A + (i + 1) * h
        res += (x2 - x1) / 2 * (f(x1) + f(x2))

    return res


def find_simpson_j(A, B, f, m, h):
    res = 0

    for i in range(0, m):
        x1 = A + i * h
        x2 = A + (i + 1) * h
        res += (x2 - x1) / 6 * (f(x1) + 4 * f((x1 + x2) / 2) + f(x2))

    return res
