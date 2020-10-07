import io
import splitter
import codecs


class Concordance:

    def __init__(self):
        self.__words = {}

    def add_word(self, word, line_number):
        if word not in self.__words:
            self.__words[word] = [line_number]
        elif line_number not in self.__words[word]:
            self.__words[word].append(line_number)

    def read_text(self, stream):
        lines = stream.readlines()

        i = 1

        for line in lines:
            lower_line = line.lower()
            words = splitter.split(
                lower_line, [' ', ',', '.', ':', ';', '\n', '\r', '\t'])

            for word in words:
                self.add_word(word, i)

            i += 1

    def print_result(self):
        f_res = codecs.open(
            'result.txt', 'w', 'utf_8_sig')

        for word in sorted(self.__words):
            chunk = word + '\t' + ' '.join([str(x)
                                            for x in self.__words[word]])
            f_res.write(chunk)
            f_res.write('\n')
