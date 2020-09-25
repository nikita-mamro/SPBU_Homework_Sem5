import codecs
import writer.file_writer as fw


def find_symbols(text_a, text_b):
    # Поиск символов из первого текста, не входящих во второй (с учётом спец. символов)
    symbols = []

    for i in range(0, len(text_a)):
        # Если во втором тексте нет текущего символа из первого, добавляем в результат
        if text_a[i] not in text_b:
            symbols.append(text_a[i])

    return symbols


def main():
    f_text_one = codecs.open('texts\\text_one.txt', 'r', 'utf_8_sig')
    f_text_two = codecs.open('texts\\text_two.txt', 'r', 'utf_8_sig')
    text_a = f_text_one.read()
    text_b = f_text_two.read()
    f_text_one.close()
    f_text_two.close()

    symbols = find_symbols(text_a, text_b)
    answer = "Символы (" + str(len(symbols)) + \
        " шт.), содержащиеся в тексте text_one,txt, но не содержащиеся в text_two.txt: " + \
        str(symbols)

    print(answer)
    fw.write_chunked_answer(
        answer, 'results\\two_texts_symbol_difference_result.txt')


if __name__ == '__main__':
    main()
