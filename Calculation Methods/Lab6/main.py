import reader
import logic
import settings
import sys
import colors
import time


def print_divider():
    sys.stdout.write(colors.GREEN)
    print('------------------------------------------------------------------------------------')
    sys.stdout.write(colors.RESET)


def start_iteration():
    h = reader.read_float('Введите h:', lambda x: x > 0)
    N = reader.read_int('Введите N:', lambda x: x >= 3)

    # Parameters
    print_divider()
    print('Длина шага h: ', h)
    print('N: ', N)
    print_divider()

    # Precise answer (j, xj, expected y(xj))
    sys.stdout.write(colors.BOLD)
    print('Точное решение:')
    sys.stdout.write(colors.RESET)
    print_divider()
    logic.print_expected_table(settings.X0, N, h, settings.y_expected)
    print_divider()

    expected_table = logic.get_expected_table(
        settings.X0, N, h, settings.y_expected)

    # Derivatives (f'(x0), f''(x0), f'''(x0), f''''(x0))
    derivatives = []
    derivatives.append(settings.Y0)
    derivatives.append(settings.d1y(settings.X0, settings.Y0))
    derivatives.append(settings.d2y(settings.X0, settings.Y0))
    derivatives.append(settings.d3y(settings.X0, settings.Y0))
    derivatives.append(settings.d4y(settings.X0, settings.Y0))
    sys.stdout.write(colors.BOLD)
    print('Найденные значения производных:')
    sys.stdout.write(colors.RESET)
    print_divider()
    logic.print_derivatives(derivatives)
    print_divider()

    # Teylor results table (j, jx, teylor y(xj), error to expected y(xj))
    # sys.stdout.write(colors.BOLD)
    #print('\n\nМетод разложения в ряд Тейлора')
    # sys.stdout.write(colors.RESET)
    # print_divider()
    # Teylor found y(xj) for x0 - 2h, x0 - h, ...
    # taylor_y = logic.find_taylor(derivatives, settings.X0, N, h)
    # logic.print_teylor_table(taylor_y, expected_table)
    # print_divider()

    # Adams results table ()
    sys.stdout.write(colors.BOLD)
    print('\n\nМетод Адамса 4-го порядка')
    sys.stdout.write(colors.RESET)
    print_divider()
    adams_y = logic.find_adams(
        N, h, settings.X0, settings.Y0, settings.d1y, expected_table)
    logic.print_adams_table(adams_y, expected_table)
    print_divider()

    # Runge-Kutta results table ()
    sys.stdout.write(colors.BOLD)
    print('\n\nМетод Рунге-Кутта 4-го порядка')
    sys.stdout.write(colors.RESET)
    print_divider()
    # Runge-Kutta found y(xj) for x0, x0 + h, ...
    rk_y = logic.find_runge_kutta(N, h, settings.X0, settings.Y0, settings.d1y)
    logic.print_runge_kutta_table(rk_y, expected_table)
    print_divider()

    # Euler results table ()
    # sys.stdout.write(colors.BOLD)
    #print('\n\nМетод Эйлера')
    # sys.stdout.write(colors.RESET)
    # print_divider()
    #eu_y = logic.find_euler(N, h, settings.X0, settings.Y0, settings.d1y)
    ##logic.print_euler_table(eu_y, expected_table)
    # print_divider()

    # Euler I results table ()
    # sys.stdout.write(colors.BOLD)
    #print('\n\nМетод Эйлера I')
    # sys.stdout.write(colors.RESET)
    # print_divider()
    #euI_y = logic.find_eulerI(N, h, settings.X0, settings.Y0, settings.d1y)
    #logic.print_eulerI_table(euI_y, expected_table)
    # print_divider()

    # Euler II results table ()
    # sys.stdout.write(colors.BOLD)
    #print('\n\nМетод Эйлера II')
    # sys.stdout.write(colors.RESET)
    # print_divider()
    #euII_y = logic.find_eulerII(N, h, settings.X0, settings.Y0, settings.d1y)
    #logic.print_eulerII_table(euII_y, expected_table)
    # print_divider()
    print('\n\n')

    # Absolute error for yN
    sys.stdout.write(colors.BOLD)
    print('Абсолютная погрешность для y_N:')
    sys.stdout.write(colors.RESET)
    print_divider()
    # logic.print_yn_absolute_error(
    #    taylor_y, adams_y, rk_y, eu_y, euI_y, euII_y, expected_table)
    logic.print_a_rk_error(adams_y, rk_y, expected_table)
    print_divider()
    print('\n\n')

    sys.stdout.write(colors.RED)
    print('Esc - выход')
    sys.stdout.write(colors.RESET)
    if reader.not_escape_pressed():
        start_iteration()


def main():
    sys.stdout.write(colors.BOLD)
    print('Лабораторная работа №6 \n Численное решение Задачи Коши для обыкновенного дифференциального уравнения первого порядка')
    print('Вариант 7')
    sys.stdout.write(colors.GREEN)
    print('y\'(x) = -y(x) + cos(x), y(0) = 1\n\n')
    sys.stdout.write(colors.RESET)
    start_iteration()


if __name__ == "__main__":
    main()
