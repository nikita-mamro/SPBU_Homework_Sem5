def root_separation(f, h, A, B):
    sections = []
    sign_switch_sections_count = 0

    x1 = A
    x2 = A + h
    y1 = f(x1)

    while x2 <= B:
        y2 = f(x2)
        if y1 * y2 <= 0:
            sign_switch_sections_count += 1
            sections.append((x1, x2))
        x1 = x2
        x2 = x1 + h
        y1 = y2

    return (sections, sign_switch_sections_count)


def bisection_method(f, a, b, epsilon):
    while b - a > 2 * epsilon:
        c = (a + b) / 2
        if f(a) * f(c) <= 0:
            a = c
        else:
            b = c

    x = (a + b) / 2
    delta = (b - a) / 2
    return (x, delta)


def newton_method():
    return 0


def modified_newton_method():
    return 0


def secant_method():
    return 0
