import logic
import settings


def print_title():
    print('\nЛабораторная 1\n')
    print('Тема:', settings.TOPIC, '\n')
    print('Исходные параметры задачи:')
    print('f(x) = ', settings.F_STRING)
    print('[A, B] = [', settings.A, ',', settings.B, ']')
    print('\u03B5 = ', settings.EPSILON, '\n')


def main():
    print_title()

    print('Процедура отделения корней:')
    (sections, counter) = logic.root_separation(
        settings.f, 0.00001, settings.A, settings.B)
    print('Кол-во отрезков смены знака функции: ',
          counter)
    print('Отрезки, содержащие корни')
    for section in sections:
        print('[', section[0], ',', section[1], ']')

    print('\nМетод бисекции')
    for section in sections:
        (x, delta) = logic.bisection_method(
            settings.f, section[0], section[1], settings.EPSILON)
        print('\nx = ', x)
        print('\u0394 = ', delta)
        print('|f(x) - 0| = ', abs(settings.f(x) - 0))

    print('\nМетод Ньютона')
    logic.newton_method()

    print('\nМетод Ньютона (модифицированный)')
    logic.modified_newton_method()

    print('\nМетод секущих')
    logic.secant_method()


if __name__ == '__main__':
    main()
