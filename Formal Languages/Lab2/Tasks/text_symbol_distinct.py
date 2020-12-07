import codecs


def find_symbols(text):
    # Вернёт объект типа set, который описывает множество (с учётом спец. символов)
    return set(text)


def main():
    f_text = codecs.open('texts\\text_one.txt')
    text = f_text.read()
    f_text.close()
    symbols = find_symbols(text)
    answer = 'Уникальных символов в тексте text_one.txt ' + \
        str(len(symbols)) + ' штук'
    f_res = codecs.open(
        'results\\text_symbol_distinct_result.txt', 'w', 'utf_8_sig')
    print(answer)
    f_res.write(answer)
    f_res.close()


if __name__ == '__main__':
    main()
