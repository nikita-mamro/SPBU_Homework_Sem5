import codecs


def write_chunked_answer(answer, result_path):
    f_res = codecs.open(
        result_path, 'w', 'utf_8_sig')

    chunks = [answer[i: i + 40]
              for i in range(0, len(answer), 40)]

    for chunk in chunks:
        f_res.write(chunk)
        f_res.write('\n')

    f_res.close()
