import logic
import settings
import sys
import colors


def print_title():
    sys.stdout.write(colors.BOLD)
    print('\nЛабораторная 1\n')
    print('Тема:', settings.TOPIC, '\n')
    print('Исходные параметры задачи:')
    print('f(x) = ', settings.F_STRING)
    print('[A, B] = [', settings.A, ',', settings.B, ']')
    print('\u03B5 = ', settings.EPSILON, '\n')
    sys.stdout.write(colors.RESET)


def print_section_methods(section):
    print_bisection_method(section)
    print_newton_method(section)
    print_modified_newton_method(section)
    print_secant_method(section)


def print_separation(A=settings.A, B=settings.B):
    sys.stdout.write(colors.GREEN)
    print('Процедура отделения корней:')
    sys.stdout.write(colors.RESET)
    print('Кол-во шагов: ', settings.SEPARATION_STEPS)
    sections = logic.root_separation(
        settings.f, settings.SEPARATION_STEPS, A, B)
    print('Кол-во отрезков смены знака функции: ',
          len(sections))
    print('Отрезки, содержащие корни')
    for section in sections:
        print('[', round(section[0], settings.ROUNDING_DIGITS),
              ',', round(section[1], settings.ROUNDING_DIGITS), ']')

    return sections


def print_bisection_method(section):
    sys.stdout.write(colors.GREEN)
    print('\nМетод бисекции')
    sys.stdout.write(colors.RESET)

    (init_approx, x, steps, last_section_length) = logic.bisection_method(
        settings.f, section[0], section[1], settings.EPSILON)

    print_results(
        init_approx,
        x,
        steps,
        last_section_length)


def print_newton_method(section):
    sys.stdout.write(colors.GREEN)
    print('\nМетод Ньютона')
    sys.stdout.write(colors.RESET)

    (init_approx, x, steps, last_section_length) = logic.newton_method(
        settings.f, settings.df, section[0], section[1], settings.EPSILON)

    print_results(
        init_approx,
        x,
        steps,
        last_section_length)


def print_modified_newton_method(section):
    sys.stdout.write(colors.GREEN)
    print('\nМодифицированный метод Ньютона')
    sys.stdout.write(colors.RESET)

    (init_approx, x, steps, last_section_length) = logic.modified_newton_method(
        settings.f, settings.df, section[0], section[1], settings.EPSILON)

    print_results(
        init_approx,
        x,
        steps,
        last_section_length
    )


def print_secant_method(section):
    sys.stdout.write(colors.GREEN)
    print('\nМетод секущих')
    sys.stdout.write(colors.RESET)

    (init_approx, init_approx_sec,  x, steps, last_section_length) = logic.secant_method(
        settings.f, section[0], section[1], settings.EPSILON
    )

    print_results(
        init_approx,
        x,
        steps,
        last_section_length,
        init_approx_sec
    )

    return


def print_results(init_approx, x, steps, last_section_length, init_approx_sec=None):
    print('\nКол-во шагов: ', steps)

    if (init_approx_sec == None):
        print('Начальное приближение: ', round(
            init_approx, settings.ROUNDING_DIGITS))
    else:
        print('Начальное приближение: x_0 = ',
              round(init_approx, settings.ROUNDING_DIGITS),
              ' x_1 = ', round(init_approx_sec, settings.ROUNDING_DIGITS))

    print('x = ', round(x, settings.ROUNDING_DIGITS))
    print('|f(x) - 0| = ', round(abs(settings.f(x)), settings.ROUNDING_DIGITS))
    print('Длина последнего отрезка: ', round(
        last_section_length, settings.ROUNDING_DIGITS), "\n")
