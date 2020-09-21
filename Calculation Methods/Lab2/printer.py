import logic
import settings
import sys
import colors
from tabulate import tabulate


def print_title():
    sys.stdout.write(colors.BOLD)
    print('\nЛабораторная 2\n')
    print('Тема:', settings.TOPIC, '\n')
    print(settings.VARIANT)
    print('Исходные параметры задачи:')
    print('f(x) = ', settings.F_STRING)
    sys.stdout.write(colors.RESET)
    print('\n')


def print_table(table):
    print('\nТаблица значений:\n')
    table_to_print = []

    for (j, x, f) in table:
        table_to_print.append(('x' + str(j), x, f))

    print(tabulate(table_to_print, headers=[
          '', 'x', 'f(x)'], tablefmt='orgtbl'))

    print()


def print_results(x, n, table):
    polynom_value = logic.get_polynom_value(x, n, table)
    f_value = settings.f(x)

    print('Значение многочлена в x: ', polynom_value)
    print('Значение функции в x: ', f_value)
    print('Фактическая погрешность: ', abs(f_value - polynom_value))
