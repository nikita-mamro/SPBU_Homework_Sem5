import reader
import old_logic
import new_logic
import settings
import printer
import colors
import sys


def start_lagrange_iteration():
    # Get user input
    (A, B) = reader.read_ab()
    m = reader.read_m()

    table = old_logic.create_table(m, A, B, settings.f)

    reversed_table = new_logic.get_reversed_table(table)

    printer.print_table(reversed_table, 'f(x)', 'x')

    while True:
        F = reader.read_F()

        n = reader.read_n(m)

        found_x = old_logic.get_polynom_value_lagrange(
            F, n, reversed_table)

        sys.stdout.write(colors.BOLD)
        print('Решение с помощью \'перевернутой\' таблицы')
        sys.stdout.write(colors.RESET)

        printer.print_results(found_x, F)

        use_bisection(A, B, m, F, n)

        print("Посчитать для новых x и n? [Y/N]")
        answer = input()

        if answer.capitalize() == 'N':
            break
        else:
            continue


def use_lagrange():
    start_lagrange_iteration()

    while True:
        print("Посчитать для нового набора значений? [Y/N]")
        answer = input()

        if answer.capitalize() == 'Y':
            start_lagrange_iteration()
        elif answer.capitalize() == 'N':
            break
        else:
            continue


def use_bisection(A, B, m, F, n):

    table = old_logic.create_table(m, A, B, settings.f)

    sys.stdout.write(colors.BOLD)
    print('\nРешение с помощью бисекции\n')
    sys.stdout.write(colors.RESET)

    print('Введите эпсилон:')
    epsilon = float(input())

    start = table[0][1]
    end = table[len(table) - 1][1]

    for i in range(0, len(table) - 1):
        if (table[i][2] == F):
            start = table[i][1]
            end = start
            break
        if (table[i][2] > F and table[i + 1][2] < F or table[i][2] < F and table[i + 1][2] > F):
            start = table[i][1]
            end = table[i + 1][1]
            break

    left_part = new_logic.get_polynom_newton(
        (start + end) / 2, n, table, settings.f, F)

    sections = old_logic.root_separation(left_part, n, A, B)
    xs = []

    for section in sections:
        (_, found_x, _, _) = old_logic.bisection_method(
            left_part, section[0], section[1], epsilon)
        xs.append(found_x)

    printer.print_results(xs[0], F)


def main():
    printer.print_title()

    use_lagrange()


if __name__ == '__main__':
    main()
