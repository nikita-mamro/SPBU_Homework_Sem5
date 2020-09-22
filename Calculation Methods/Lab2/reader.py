import sys
import colors


def read_m():
    sys.stdout.write(colors.GREEN)
    print("Введите m + 1:")
    m = int(input()) - 1
    sys.stdout.write(colors.RESET)
    return m


def read_ab():
    sys.stdout.write(colors.GREEN)
    A = 1
    B = 0

    while A > B:
        print('Введите A и B такие, что A ≤ B')
        print('Введите A:')
        A = float(input())
        print('Введите B:')
        B = float(input())

    sys.stdout.write(colors.RESET)
    return (A, B)


def read_x():
    sys.stdout.write(colors.GREEN)
    print('Введите x:')
    x = float(input())
    sys.stdout.write(colors.RESET)
    return x


def read_n(m):
    sys.stdout.write(colors.GREEN)
    n = m + 1

    while n > m:
        print('Введите степень P n ≤ m = ', m, ':')
        n = int(input())

    sys.stdout.write(colors.RESET)
    return n
