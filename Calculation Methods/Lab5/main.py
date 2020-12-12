import reader
import settings
import logic
import numpy as np
from scipy import integrate


def perform_step():
    f_gauss = settings.fG
    f_meler = settings.fM
    w_gauss = settings.wG

    a = reader.read_float('Введите A: ', lambda x: True)
    b = reader.read_float('Введите B: ', lambda x: x > a)
    m = reader.read_int(
        'Введите число m промежутков для интегрирования по составной КФ Гаусса: ', lambda x: x > 0)
    n = reader.read_int(
        'Введите число N узлов для интегрирования по КФ Мелера: ', lambda x: x > 0)

    g_res = logic.find_gauss(lambda x: f_gauss(x) * w_gauss(x), a, b, m)
    g_like_res = logic.find_gauss_like(f_gauss, w_gauss, a, b, True)
    m_res = logic.find_meler(f_meler, n)

    g_expected = integrate.quad(lambda x: f_gauss(x) * w_gauss(x), a, b)[0]
    m_expected = settings.fM_expected(1) - settings.fM_expected(-1)

    print('Число промежутков для КФ Гаусса: ', m)
    print('Фактическое значение: ', g_expected)

    print('Формула Гаусса')
    print('Вычисленное значение: ', g_res)
    print('Абсолютная погрешность: ', abs(g_res - g_expected))

    print('Формула типа Гаусса')
    print('Вычисленное значение: ', g_like_res)
    print('Абсолютная погрешность: ', abs(g_like_res - g_expected))

    print('Число узлов для КФ Мелера: ', n)

    print('Формула Мелера')
    print('Отрезок интегрирования [-1;1]')
    print('Вычисленное значение: ', m_res)
    print('Абсолютная погрешность: ', abs(m_res - m_expected))

    print('\n\n')

    print('Esc - выход')
    if reader.not_escape_pressed():
        perform_step()


def main():
    print('Лабораторная работа №5 \n Приближённое вычисление интегралов при помощи квадратурных формул Наивысшей Алгебраической Степени Точности(КФ НАСТ)')
    print('Вариант 7')

    print('f(x) = sin(x)')

    print('Вес для интегрирования по КФ Гаусса: p(x) = |x - 1/2|')
    print('Вес для интегрирования по КФ Мелера: p(x) = 1 / sqrt(1 - x^2)')

    print('Параметры: m = ', settings.M, ' N = ', settings.N)

    perform_step()

    return


if __name__ == '__main__':
    main()
