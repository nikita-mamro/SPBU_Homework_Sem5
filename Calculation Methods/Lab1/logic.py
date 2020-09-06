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
            print("[", x1, ",", x2, "]")

        x1 = x2
        x2 = x1 + h
        y1 = y2

    print("Кол-во отрезков смены знака функции: ",
          sign_switch_sections_count)
    return sections


def bisection_method():
    return 0


def newton_method():
    return 0


def modified_newton_method():
    return 0


def secant_method():
    return 0
