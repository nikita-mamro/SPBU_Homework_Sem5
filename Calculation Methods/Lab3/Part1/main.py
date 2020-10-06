import reader
import old_logic
import new_logic
import settings
import printer


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

        printer.print_results(found_x, F)
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


def use_bisection():
    # Get user input
    (A, B) = reader.read_ab()
    m = reader.read_m()

    table = old_logic.create_table(m, A, B, settings.f)

    printer.print_table(table, 'x', 'f(x)')

    print('Введите эпсилон:')
    epsilon = float(input())

    F = reader.read_F()

    n = reader.read_n(m)

    left_part = new_logic.get_polynom_newton(
        (A + B) / 2, n, table, settings.f, F)
    (_, found_x, _, _) = old_logic.bisection_method(left_part, A, B, epsilon)

    printer.print_results(found_x, F)


def main():
    printer.print_title()

    choice = '0'

    while choice != '1' and choice != '2':
        print(
            'Выберите способ [1(поиск обратной по методу Лагранжа)/2(использование бисекции)]')

        choice = input()

        if choice == '1':
            use_lagrange()
            break
        elif choice == '2':
            use_bisection()
            break


if __name__ == '__main__':
    main()
