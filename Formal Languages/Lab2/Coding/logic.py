import constants

# Таблица для хранения кодов
code_table = {
    ':': 1,
    '(': 2,
    ')': 3,
    '.': 4,
    '*': 5,
    ';': 6,
    ',': 7,
    '#': 8,
    '[': 9,
    ']': 10,
    'Eofgram': 1000
}

# Множества нетерминалов, терминалов и семантик
nonterminals = []
terminals = []
semantics = []


def split_manually(text):
    # Разбиваем текст на множество токенов (симолы-разделители или слова)
    tokens = []

    # Будем хранить позицию последнего обработанного разделителя здесь
    last_separator_index = -1

    i = 0

    while i < len(text):
        if text[i] in constants.SEPARATORS:
            # Если разделитель --- кавычка, ищем структуру 'слово', добавляем кавычки и слово в результат
            if text[i] == '\'':
                # i хранит позицию открывающей кавычки
                tokens.append(text[i])
                # pairedQuote будет хранить позицию закрывающей кавычки
                pairedQuote = i + 1

                while text[pairedQuote] != '\'':
                    if pairedQuote >= len(text):
                        raise Exception('Paired quote not found')

                    pairedQuote += 1

                tokens.append(text[i + 1: pairedQuote])
                tokens.append(text[pairedQuote])

                last_separator_index = pairedQuote
                i = pairedQuote + 1

                continue

            # Добавляем к результату предыдущий разделитель и слово между ним и текущим
            tokens.append(text[i])

            if i - last_separator_index > 1:
                tokens.append(text[last_separator_index + 1: i])

            last_separator_index = i
            i += 1
            continue

        i += 1

    return tokens


def extract_rules(split_text):
    # Выделяем правила из множества токенов, полученных из метода split_manually
    rules = []

    last_dot_index = -1

    i = 0
    while i < len(split_text):
        # Для каждой точки проверяем, является ли она разделителем между правилами
        # Если да, добавляем новое правило в массив rules
        if split_text[i] == '.':
            if i == 0:
                raise Exception('Dot in the beginning error')

            # Если точка в кавычках, это не завершение правила
            if split_text[i - 1] == '\'' and i != len(split_text) - 1 and split_text[i + 1] == '\'':
                i += 1
                continue

            rules.append(split_text[last_dot_index + 1: i + 1])
            last_dot_index = i

            i += 1
            continue
        i += 1

    return rules


def proceed_terminal(token):
    # Обработка терминала
    # Пытаемся добавить терминал в таблицу кодов с проверкой на то, не превышает ли количество терминалов допустимый предел
    token = '\'' + token + '\''
    if not token in terminals:
        if len(terminals) == constants.T_end_index - constants.T_start_index + 1:
            raise Exception('Too many terminals error')

        code_table[token] = constants.T_start_index + len(terminals)
        terminals.append(token)


def proceed_nonterminal(token):
    # Обработка нетерминала
    # Пытаемся добавить нетерминал в таблицу кодов с проверкой на то, не превышает ли количество нетерминалов допустимый предел
    if not token in nonterminals:
        if len(nonterminals) == constants.NT_end_index - constants.NT_start_index + 1:
            raise Exception('Too many nonterminals error')

        code_table[token] = constants.NT_start_index + len(nonterminals)
        nonterminals.append(token)


def proceed_semantic(token):
    # Обработка семантики
    # Пытаемся добавить семантику в таблицу кодов с проверкой на то, не превышает ли количество семантик допустимый предел
    token = '$' + token
    if not token in semantics:
        if len(semantics) == constants.SEM_end_index - constants.SEM_start_index + 1:
            raise Exception('Too many semantics error')

        code_table[token] = constants.SEM_start_index + len(semantics)
        semantics.append(token)


def proceed_rule_nonterminal(rule):
    # Обработка нетерминала слева от двоеточия в данном правиле

    # Избавляемся от пустых символов
    rule = list(filter(lambda c: c != ' ', rule))
    rule = list(filter(lambda c: c != '\n', rule))
    rule = list(filter(lambda c: c != '\t', rule))
    rule = list(filter(lambda c: c != '\r', rule))

    if len(rule) < 2 or rule[1] != ':':
        raise Exception('Wrong rule format to proceed error')

    proceed_nonterminal(rule[0])


def proceed_rule(rule):
    # Обработка правила
    # Заполняем таблицу и генерируем последовательность кодов для данного правила
    # Правило имеет вид expression:formula'.'.
    codes = []

    # Избавляемся от пустых символов
    rule = list(filter(lambda c: c != ' ', rule))
    rule = list(filter(lambda c: c != '\n', rule))
    rule = list(filter(lambda c: c != '\t', rule))
    rule = list(filter(lambda c: c != '\r', rule))

    if len(rule) < 2 or rule[1] != ':':
        raise Exception('Wrong rule format to proceed error')

    # Добавляем в коды нетерминал из начала правила
    codes.append(str(code_table[rule[0]]))

    i = 1

    while i < len(rule):
        # Встретили кавычку --- обрабатываем терминал
        if rule[i] == '\'':
            if i + 2 >= len(rule) or rule[i + 2] != '\'':
                raise Exception('Wrong quotes in rule error')

            proceed_terminal(rule[i + 1])
            codes.append(str(code_table['\'' + rule[i + 1] + '\'']))
            i += 3
            continue

        # Встретили знак $ --- обрабатываем семантику
        if rule[i] == '$':
            if i + 1 == len(rule):
                raise Exception('$ in the end error')

            proceed_semantic(rule[i + 1])
            codes.append(str(code_table['$' + rule[i + 1]]))

            i += 2

            continue

        # Для разделителей добавляем их код из таблицы
        if rule[i] == ' ' or rule[i] in constants.SEPARATORS:
            if rule[i] in constants.SYMBOLS:
                codes.append(str(code_table[rule[i]]))

            i += 1
            continue

        # Для слова строчными буквами проверяем, есть ли оно в таблице кодов (вдруг нетерминал)
        # Если нет, обрабатываем как терминал
        if rule[i].islower():
            if rule[i] in code_table:
                codes.append(str(code_table[rule[i]]))
                i += 1
                continue

            proceed_terminal(rule[i])
            codes.append(str(code_table['\'' + rule[i] + '\'']))
            i += 1
            continue

        # Обрабатываем нетерминал --- слово из заглавных букв
        if rule[i].isupper():
            proceed_nonterminal(rule[i])
            codes.append(str(code_table[rule[i]]))
            i += 1
            continue

        i += 1

    return codes


def generate_codes(text):
    # Генерируем коды для считанного из файла текста
    codes = []
    split_text = split_manually(text)
    rules = extract_rules(split_text)

    for rule in rules:
        proceed_rule_nonterminal(rule)

    for rule in rules:
        proceeded_rule = proceed_rule(rule)
        # Разбиваем на строки длиной не более 20 символов и добавляем к кодам с переносом строки
        chunks = [proceeded_rule[i: i + 20]
                  for i in range(0, len(proceeded_rule), 20)]

        for chunk in chunks:
            codes += chunk
            codes.append('\n')

        # После правила делаем двойной отступ
        codes.append('\n\n')

    codes.append(str(code_table['Eofgram']))

    return codes


def process_expression_file():
    # Основной метод, осуществляет чтение из файла, обработку текста, запись резальтата в файл с результатом

    # Подготовка для чтения/записи в файл
    file = open(constants.EXPRESSION_FILENAME, 'r')
    res_file = open(constants.RESULT_FILENAME, 'w')

    file_content = file.read()
    file.close()

    # Генерация кодов
    try:
        if file_content[-7:] != constants.EOG:
            raise Exception('No Eofgram error')
        codes = generate_codes(file_content)
        res_file.write(' '.join(codes))
    except Exception as inst:
        # Если произошла ошибка (например, в конце нет Eofgram, выводим информацию в файл)
        message = inst.args[0]
        res_file.write(message)
    finally:
        res_file.close()
