import codecs
import writer.file_writer as fw


def find_all_symbols(text_a, text_b):
    # Вернёт результат сложения двух списков (элементы могут повторяться) с учётом спец. символов
    return list(text_a) + list(text_b)


def main():
    f_one = codecs.open('texts\\text_one.txt', 'r', 'utf_8_sig')
    f_two = codecs.open('texts\\text_two.txt', 'r', 'utf_8_sig')
    text_a = f_one.read()
    text_b = f_two.read()
    f_one.close()
    f_two.close()
    symbols = find_all_symbols(text_a, text_b)

    answer = "Символы (" + str(len(symbols)) + \
        " шт.), содержащиеся в текстах: " + str(symbols)

    print(answer)
    fw.write_chunked_answer(
        answer, 'results\\two_texts_symbol_result.txt')


if __name__ == '__main__':
    main()
