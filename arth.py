from Token import TokenType

def evaluate_arithmetic(tokens):
    if tokens and tokens[-1].type == TokenType.EOF:
        tokens = tokens[:-1]

    if not tokens:
        return 0

    infix = []
    for token in tokens:
        if token.type == TokenType.INT:
            infix.append(int(token.literal))
        elif token.type == TokenType.FLOAT:
            infix.append(float(token.literal))
        elif token.type in [TokenType.PLUS, TokenType.MINUS, TokenType.ASTERISK,
                            TokenType.SLASH, TokenType.POWER, TokenType.MODULO]:
            infix.append(token.literal)
        elif token.type == TokenType.LPAREN:
            infix.append('(')
        elif token.type == TokenType.RPAREN:
            infix.append(')')

    return evaluate_infix(infix)


def evaluate_infix(infix):
    if not infix:
        return 0

    while '(' in infix:
        open_idx = infix.index('(')
        close_idx = find_matching_paren(infix, open_idx)

        if close_idx == -1:
            raise ValueError("Mismatched parentheses")

        sub_result = evaluate_infix(infix[open_idx+1:close_idx])

        infix = infix[:open_idx] + [sub_result] + infix[close_idx+1:]

    i = 0
    while i < len(infix):
        if i+2 < len(infix) and infix[i+1] == '^':
            infix[i:i+3] = [pow(infix[i], infix[i+2])]
        else:
            i += 1

    i = 0
    while i < len(infix):
        if i+2 < len(infix) and infix[i+1] in ['*', '/', '%']:
            op = infix[i+1]
            if op == '*':
                infix[i:i+3] = [infix[i] * infix[i+2]]
            elif op == '/':
                if infix[i+2] == 0:
                    raise ValueError("Division by zero")
                infix[i:i+3] = [infix[i] / infix[i+2]]
            elif op == '%':
                infix[i:i+3] = [infix[i] % infix[i+2]]
        else:
            i += 1

    i = 0
    while i < len(infix):
        if i+2 < len(infix) and infix[i+1] in ['+', '-']:
            op = infix[i+1]
            if op == '+':
                infix[i:i+3] = [infix[i] + infix[i+2]]
            elif op == '-':
                infix[i:i+3] = [infix[i] - infix[i+2]]
        else:
            i += 1

    if len(infix) == 1:
        return infix[0]
    else:
        raise ValueError(f"Invalid expression: {infix}")

def find_matching_paren(expr, open_idx):
    count = 1
    for i in range(open_idx + 1, len(expr)):
        if expr[i] == '(':
            count += 1
        elif expr[i] == ')':
            count -= 1
            if count == 0:
                return i
    return -1
