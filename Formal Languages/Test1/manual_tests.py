import concordance
import io

INPUTS = ['a b c\na b\na  ', '     ', 'Hello, my name\nis John\nHello, John']

OUTPUTS = [{'a': [1, 2, 3], 'b': [1, 2], 'c': [1]}, {}, {
    'Hello': [1, 3], 'my': [1], 'name': [1], 'is': [2], 'John': [2, 3]}]


def run_tests():
    for i in range(0, 1):
        c = concordance.Concordance()
        s = io.StringIO(INPUTS[i])
        c.read_text(s)

        words_dict = c.get_words()

        expected = OUTPUTS[i]

        if (words_dict != expected):
            print('Test ', i, ' failed')

    print('Passed tests')
