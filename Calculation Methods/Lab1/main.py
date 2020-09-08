import printer
import sys
import colors
import settings


def main():
    printer.print_title()

    sections = printer.print_separation()

    for section in sections:
        sys.stdout.write(colors.BLUE)
        print("\nОтрезок [", round(section[0], settings.ROUNDING_DIGITS),
              ",", round(section[1], settings.ROUNDING_DIGITS), "]")
        sys.stdout.write(colors.RESET)
        printer.print_section_methods(section)


if __name__ == '__main__':
    main()
