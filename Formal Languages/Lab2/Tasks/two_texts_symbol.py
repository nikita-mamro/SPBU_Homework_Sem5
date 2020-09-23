def find_all_symbols_manual(text_a, text_b):
    symbols = []

    min_text = []
    max_text = []

    if len(text_a) <= len(text_b):
        min_text = text_a
        max_text = text_b
    else:
        min_text = text_b
        max_text = text_a

    for i in range(0, len(min_text)):
        symbols.append(min_text[i])
        symbols.append(max_text[i])

    if len(max_text) > len(min_text):
        for i in range(len(min_text), len(max_text)):
            symbols.append(max_text[i])

    return symbols


def find_all_symbols_lib(text_a, text_b):
    return list(text_a) + list(text_b)


def main():
    print("Введите первый текст:")
    text_a = input()
    print("Введите второй текст:")
    text_b = input()
    symbols_manual = find_all_symbols_manual(text_a, text_b)
    symbols_lib = find_all_symbols_lib(text_a, text_b)
    print("Символы (", len(symbols_manual),
          " шт.), содержащиеся в текстах, первым способом (не исп. библиотечные операции со множествами): ", symbols_manual)
    print("Символы (", len(symbols_lib),
          " шт.), содержащиеся в текстах, вторым способом: ", symbols_lib)


if __name__ == '__main__':
    main()
