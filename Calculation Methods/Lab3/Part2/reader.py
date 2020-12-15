import sys
import colors


def read_m():
    sys.stdout.write(colors.GREEN)
    print("Введите m + 1:")
    m = int(input()) - 1

    while m <= 0:
        print('Введите допустимое m')
        m = int(input()) - 1

    sys.stdout.write(colors.RESET)
    return m


def read_a():
    sys.stdout.write(colors.GREEN)
    print("Введите a:")
    a = float(input())
    sys.stdout.write(colors.RESET)
    return a


def read_h():
    sys.stdout.write(colors.GREEN)
    print("Введите h > 0:")
    h = float(input())

    while h <= 0:
        print('Введите допустимое h')
        h = float(input())

    sys.stdout.write(colors.RESET)
    return h
