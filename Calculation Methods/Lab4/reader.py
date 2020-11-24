def floatTryParse(value):
    try:
        return float(value), True
    except:
        return value, False


def intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False


def read_float(alert, predicate):
    while True:
        print(alert)
        res = floatTryParse(input())
        if res[1] and predicate(res[0]):
            return res[0]
        print('Введите корректное вещественное число')


def read_int(alert, predicate):
    while True:
        print(alert)
        res = intTryParse(input())
        if res[1] and predicate(res[0]):
            return res[0]
        print('Введите корректное целое число')
