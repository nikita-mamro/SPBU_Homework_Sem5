import concordance
import io
import codecs


def main():
    c = concordance.Concordance()
    # s = io.StringIO('a b;c,d e\na a bd ddx e')
    f = codecs.open(
        'input.txt', 'r', 'utf_8_sig')
    c.read_text(f)
    c.print_result()


if __name__ == '__main__':
    main()
