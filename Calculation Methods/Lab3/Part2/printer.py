import sys
import settings
import colors
from tabulate import tabulate


def print_title():
    sys.stdout.write(colors.BOLD)
    print('\nЛабораторная 3.2\n')
    print('Тема:', settings.TOPIC, '\n')
    print('Исходные параметры задачи:')
    print('f(x) = ', settings.F_STRING)
    sys.stdout.write(colors.RESET)
    print('\n')


def print_table(table, col_1='x', col_2='f(x)'):
    print('\nТаблица значений:\n')
    table_to_print = []

    for (j, x, f) in table:
        table_to_print.append((str(j), x, f))

    print(tabulate(table_to_print, headers=[
          'j', col_1, col_2], tablefmt='orgtbl'))

    print()


def print_d_table(table):
    print('\nТаблица производных\n')

    print(tabulate(table, headers=[
          'x', 'f чд', '|f\'т - f\'чд|', 'f\'\'чд', '|f\'\'т - f\'\'чд|'], tablefmt='orgtbl'))
