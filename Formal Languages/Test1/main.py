import concordance
import io
import codecs
import manual_tests


def main():
    #c = concordance.Concordance()
    ## s = io.StringIO('a b;c,d e\na a bd ddx e')
    # f = codecs.open(
    #    'input.txt', 'r', 'utf_8_sig')
    # c.read_text(f)
    # c.print_result()
    manual_tests.run_tests()


if __name__ == '__main__':
    main()
