import constants

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

nonterminals = []
terminals = []
semantics = []


def split_manually(text):
    # Turns text into array
    # Desc:
    # Keeps :, $ and '' where expected
    # Keeps combinations of letters
    res = []

    last_separator_index = -1  # to not trim 1st word

    i = 0

    while i < len(text):
        if text[i] in constants.SEPARATORS:
            if text[i] == '\'':
                # i stores left quote position
                res.append(text[i])
                # pairedQuote will store right quote position
                pairedQuote = i + 1

                while text[pairedQuote] != '\'':
                    if pairedQuote >= len(text):
                        raise Exception('Paired quote not found')

                    pairedQuote += 1

                res.append(text[i + 1: pairedQuote])
                res.append(text[pairedQuote])

                last_separator_index = pairedQuote
                i = pairedQuote + 1

                continue

            # Add substring between separators
            res.append(text[i])

            if i - last_separator_index > 1:
                res.append(text[last_separator_index + 1: i])

            last_separator_index = i
            i += 1
            continue

        if i == len(text) - 7:
            if text[i: len(text)] != 'Eofgram':
                raise Exception('No Eofgram error')
            break

        i += 1

    return res


def extract_rules(split_text):
    # Split array into arrays with rules, looking at dots without quotes
    rules = []

    last_dot_index = -1

    i = 0
    while i < len(split_text):
        if split_text[i] == '.':
            if i == 0:
                raise Exception('Dot in the beginning error')

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
    token = '\'' + token + '\''
    if not token in terminals:
        if len(terminals) == constants.T_end_index - constants.T_start_index + 1:
            raise Exception('Too many terminals error')

        code_table[token] = constants.T_start_index + len(terminals)
        terminals.append(token)


def proceed_nonterminal(token):
    if not token in nonterminals:
        if len(nonterminals) == constants.NT_end_index - constants.NT_start_index + 1:
            raise Exception('Too many nonterminals error')

        code_table[token] = constants.NT_start_index + len(nonterminals)
        nonterminals.append(token)


def proceed_semantic(token):
    token = '$' + token
    if not token in semantics:
        if len(semantics) == constants.SEM_end_index - constants.SEM_start_index + 1:
            raise Exception('Too many semantics error')

        code_table[token] = constants.SEM_start_index + len(semantics)
        semantics.append(token)


def proceed_rule_nonterminal(rule):
    rule = list(filter(lambda c: c != ' ', rule))
    rule = list(filter(lambda c: c != '\n', rule))
    rule = list(filter(lambda c: c != '\t', rule))
    rule = list(filter(lambda c: c != '\r', rule))

    if len(rule) < 2 or rule[1] != ':':
        raise Exception('Wrong rule format to proceed error')

    proceed_nonterminal(rule[0])


def proceed_rule(rule):
    # rule --- for example [expression:formula','.]
    codes = []

    rule = list(filter(lambda c: c != ' ', rule))
    rule = list(filter(lambda c: c != '\n', rule))
    rule = list(filter(lambda c: c != '\t', rule))
    rule = list(filter(lambda c: c != '\r', rule))

    if len(rule) < 2 or rule[1] != ':':
        raise Exception('Wrong rule format to proceed error')

    codes.append(str(code_table[rule[0]]))

    i = 1

    while i < len(rule):
        if rule[i] == '\'':
            if i + 2 >= len(rule) or rule[i + 2] != '\'':
                raise Exception('Wrong quotes in rule error')

            proceed_terminal(rule[i + 1])
            codes.append(str(code_table['\'' + rule[i + 1] + '\'']))
            i += 3
            continue

        if rule[i] == '$':
            if i + 1 == len(rule):
                raise Exception('$ in the end error')

            proceed_semantic(rule[i + 1])
            codes.append(str(code_table['$' + rule[i + 1]]))

            i += 2

            continue

        if rule[i] == ' ' or rule[i] in constants.SEPARATORS:
            if rule[i] in constants.SYMBOLS:
                codes.append(str(code_table[rule[i]]))

            i += 1
            continue

        if rule[i].islower():
            if rule[i] in code_table:
                codes.append(str(code_table[rule[i]]))
                i += 1
                continue

            proceed_terminal(rule[i])
            codes.append(str(code_table['\'' + rule[i] + '\'']))
            i += 1
            continue

        if rule[i].isupper():
            proceed_nonterminal(rule[i])
            codes.append(str(code_table[rule[i]]))
            i += 1
            continue

        i += 1

    return codes


def generate_codes(text):
    codes = []
    split_text = split_manually(text)
    rules = extract_rules(split_text)

    for rule in rules:
        proceed_rule_nonterminal(rule)

    for rule in rules:
        codes += proceed_rule(rule)
        codes.append('\n')

    codes.append(str(code_table['Eofgram']))

    return codes


def process_expression_file():
    # Prepare files
    file = open(constants.EXPRESSION_FILENAME, 'r')
    res_file = open(constants.RESULT_FILENAME, 'w')

    file_content = file.read()

    # Generate codes
    try:
        codes = generate_codes(file_content)
        res_file.write(' '.join(codes))
    except Exception as inst:
        message = inst.args[0]
        res_file.write(message)
