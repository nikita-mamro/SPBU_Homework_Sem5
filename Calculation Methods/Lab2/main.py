import printer
import reader
import logic


def start_iteration():
    # Get user input
    m = reader.read_m()
    (A, B) = reader.read_ab()
    table = logic.create_table(m, A, B)
    printer.print_table(table)
    x = reader.read_x()
    n = reader.read_n(m)
    # Print results
    printer.print_results(x, n, table)


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
