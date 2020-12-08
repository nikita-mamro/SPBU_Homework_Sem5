import printer
import reader
import logic
import settings


def start_iteration():
    # Get user input
    (A, B) = reader.read_ab()
    m = reader.read_m()

    table = logic.create_table(m, A, B, settings.f)
    printer.print_table(table)

    while True:
        x = reader.read_x()
        n = reader.read_n(m)
        # Print results
        printer.print_results_newton(x, n, table, settings.f)
        print("Посчитать для новых x и n? [Y/N]")
        answer = input()

        if answer.capitalize() == 'N':
            break
        else:
            continue


def main():
    printer.print_title()
    start_iteration()

    while True:
        print("Посчитать для нового набора значений? [Y/N]")
        answer = input()

        if answer.capitalize() == 'Y':
            start_iteration()
        elif answer.capitalize() == 'N':
            break
        else:
            continue


if __name__ == '__main__':
    main()
