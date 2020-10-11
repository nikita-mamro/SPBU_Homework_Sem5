import reader
import logic
import settings
import printer


def main():
    printer.print_title()

    m = reader.read_m()
    a = reader.read_a()
    h = reader.read_h()

    table = logic.create_table(a, m, h)

    printer.print_table(table)

    d_table = logic.create_d_table(table, h)

    printer.print_d_table(d_table)

    pass


if __name__ == '__main__':
    main()
