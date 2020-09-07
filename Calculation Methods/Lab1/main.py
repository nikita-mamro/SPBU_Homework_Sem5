import printer
import sys
import colors


def main():
    printer.print_title()

    sections = printer.print_separation()

    for section in sections:
        sys.stdout.write(colors.BLUE)
        print("\nОтрезок [", round(section[0], 6),
              ",", round(section[1], 6), "]")
        sys.stdout.write(colors.RESET)
        printer.print_section_methods(section)


if __name__ == '__main__':
    main()
