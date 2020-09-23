import codecs


def find_symbols_manual(text):
    symbols = []

    for i in range(0, len(text)):
        if text[i] not in symbols:
            symbols.append(text[i])

    return symbols


def find_symbols_lib(text):
    return set(text)


def main():
    f_one = codecs.open('text_one.txt', 'r', 'utf_8_sig')
    text = f_one.read()
    f_one.close()
    symbols_manual = find_symbols_manual(text)
    symbols_lib = find_symbols_lib(text)
    print("Уникальные символы (", len(symbols_manual),
          " шт.), содержащиеся в тексте, первым способом (не исп. библиотечные операции со множествами): ", symbols_manual)
    print("Уникальные символы (", len(symbols_lib),
          " шт.), содержащиеся в тексте, вторым способом: ", symbols_lib)


if __name__ == '__main__':
    main()
