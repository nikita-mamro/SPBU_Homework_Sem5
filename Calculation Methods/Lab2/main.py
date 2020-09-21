import printer
import reader
import logic


def main():
    printer.print_title()
    # Get user input
    m = reader.read_m()
    (A, B) = reader.read_ab()
    table = logic.create_table(m, A, B)
    printer.print_table(table)
    x = reader.read_x()
    n = reader.read_n(m)
    # Sort x-s
    printer.print_results(x, n, table)


if __name__ == '__main__':
    main()
