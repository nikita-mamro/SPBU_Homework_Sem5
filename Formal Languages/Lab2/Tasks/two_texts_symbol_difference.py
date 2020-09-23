def find_symbols_manual(text_a, text_b):
    symbols = []

    for i in range(0, len(text_a)):
        if text_a[i] not in text_b:
            symbols.append(text_a[i])

    return symbols


def main():
    print("Введите первый текст:")
    text_a = input()
    print("Введите второй текст:")
    text_b = input()
    symbols_manual = find_symbols_manual(text_a, text_b)
    print("Символы (", len(symbols_manual),
          " шт.), содержащиеся в первом тексте, но не содержащиеся во втором: ", symbols_manual)


if __name__ == '__main__':
    main()
