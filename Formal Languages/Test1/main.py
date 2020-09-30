import concordance
import io


def main():
    c = concordance.Concordance()
    s = io.StringIO('a b;c,d e\na a bd ddx e')
    # f = open('filename', 'r', encoding='utf-8')
    c.read_text(s)
    c.print_result()


if __name__ == '__main__':
    main()
