import reader
import settings
import logic
import math
import scipy.optimize as opt
import scipy


def print_res(res, expected, d, M, C, A, B, h):
    print('J(h) = ', res)
    fact = abs(res - expected)
    print('|J - J(h)| = ', fact)
    theor = C * M * (B - A) * math.pow(h, d + 1)
    print('Теоретическая погрешность ', theor)


def main():
    print('Лабораторная работа №4 \n Приближённое вычисление интеграла по составным квадратурным формулам')
    print('Вариант 7')
    a = reader.read_float('Введите A: ', lambda x: True)
    b = reader.read_float('Введите B: ', lambda x: x > a)
    m = reader.read_int('Введите m: ', lambda x: x > 0)
    h = (b - a) / m
    J = settings.expected(a, b)
    print('\nA = ', a)
    print('B = ', b)
    print('m = ', m)
    print('h = (B - A) / m = ', h)
    print('f(x) = ', settings.get_f_as_string())
    print('J = ', J)

    func = settings.f
    f_max = opt.fmin_l_bfgs_b(lambda x: -func(x), 1.0,
                              bounds=[(a, b)], approx_grad=True)[0][0]

    c = 1/2

    print('\nКФ левых прямоугольников')
    left_res = logic.find_left_rectangle_j(a, func, m, h)
    print_res(left_res, J, 0, f_max, c, a, b, h)

    print('\nКФ правых прямоугольников')
    right_res = logic.find_right_rectangle_j(a, func, m, h)
    print_res(right_res, J, 0, f_max, c, a, b, h)

    c = 1/24

    print('\nКФ средних прямоугольников')
    middle_res = logic.find_middle_rectangle_j(a, func, m, h)
    print_res(middle_res, J, 1, f_max, c, a, b, h)

    c = 1/12

    print('\nКФ трапеций')
    trapezoid_res = logic.find_trapezoid_j(a, b, func, m, h)
    print_res(trapezoid_res, J, 1, f_max, c, a, b, h)

    c = 1/2880

    print('\nКФ Симпсона')
    simpson_res = logic.find_simpson_j(a, b, func, m, h)
    print_res(simpson_res, J, 3, f_max, c, a, b, h)


if __name__ == '__main__':
    main()
