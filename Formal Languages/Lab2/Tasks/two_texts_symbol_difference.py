import codecs


def find_symbols_manual(text_a, text_b):
    symbols = []

    for i in range(0, len(text_a)):
        if text_a[i] not in text_b:
            symbols.append(text_a[i])

    return symbols


def main():
    f_one = codecs.open('text_one.txt', 'r', 'utf_8_sig')
    f_two = codecs.open('text_two.txt', 'r', 'utf_8_sig')
    text_a = f_one.read()
    text_b = f_two.read()
    f_one.close()
    f_two.close()
    symbols_manual = find_symbols_manual(text_a, text_b)
    print("Символы (", len(symbols_manual),
          " шт.), содержащиеся в первом тексте, но не содержащиеся во втором: ", symbols_manual)


if __name__ == '__main__':
    main()
