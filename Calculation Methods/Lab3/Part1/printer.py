import settings
import sys
import colors
from tabulate import tabulate


def print_title():
    sys.stdout.write(colors.BOLD)
    print('\nЛабораторная 3.1\n')
    print('Тема:', settings.TOPIC, '\n')
    print('Исходные параметры задачи:')
    print('f(x) = ', settings.F_STRING)
    sys.stdout.write(colors.RESET)
    print('\n')


def print_table(table, col_1='x', col_2='f(x)'):
    print('\nТаблица значений:\n')
    table_to_print = []

    for (j, x, f) in table:
        table_to_print.append(('x' + str(j), x, f))

    print(tabulate(table_to_print, headers=[
          '', col_1, col_2], tablefmt='orgtbl'))

    print()


def print_results(X, F):
    print('F = ', F)
    print('Найденный X = ', settings.f(X))
    print('Модуль невязки: ', abs(settings.f(X) - F))
