import logic
import settings
import sys
import colors


def print_title():
    print('\nЛабораторная 1\n')
    print('Тема:', settings.TOPIC, '\n')
    print('Исходные параметры задачи:')
    print('f(x) = ', settings.F_STRING)
    print('[A, B] = [', settings.A, ',', settings.B, ']')
    print('\u03B5 = ', settings.EPSILON, '\n')


def print_section_methods(section):
    print_bisection_method(section)
    print_newton_method(section)
    print_modified_newton_method(section)
    print_secant_method(section)


def print_separation(A=settings.A, B=settings.B):
    sys.stdout.write(colors.GREEN)
    print('Процедура отделения корней:')
    sys.stdout.write(colors.RESET)
    sections = logic.root_separation(
        settings.f, 0.00001, A, B)
    print('Кол-во отрезков смены знака функции: ',
          len(sections))
    print('Отрезки, содержащие корни')
    for section in sections:
        print('[', round(section[0], 6), ',', round(section[1], 6), ']')

    return sections


def print_bisection_method(section):
    sys.stdout.write(colors.GREEN)
    print('\nМетод бисекции')
    sys.stdout.write(colors.RESET)
    (x, steps, last_section_length) = logic.bisection_method(
        settings.f, section[0], section[1], settings.EPSILON)
    print_results((section[0] + section[1]) / 2, x, steps, last_section_length)


def print_newton_method(section):
    sys.stdout.write(colors.GREEN)
    print('\nМетод Ньютона')
    sys.stdout.write(colors.RESET)
    (x, steps, last_section_length) = logic.newton_method(
        settings.f, settings.df, section[0], section[1], settings.EPSILON)
    print_results((section[0] + section[1]) / 2, x, steps, last_section_length)


def print_modified_newton_method(section):
    sys.stdout.write(colors.GREEN)
    print('\nМодифицированный метод Ньютона')
    sys.stdout.write(colors.RESET)
    return


def print_secant_method(section):
    sys.stdout.write(colors.GREEN)
    print('\nМетод секущих')
    sys.stdout.write(colors.RESET)
    return


def print_results(init_approx, x, steps, last_section_length):
    print('\nКол-во шагов: ', steps)
    print('Начальное приближение: ', round(init_approx, 6))
    print('x = ', round(x, 6))
    print('|f(x) - 0| = ', round(abs(settings.f(x)), 6))
    print('Длина последнего отрезка: ', round(last_section_length, 6), "\n")
