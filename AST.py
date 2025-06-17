from abc import ABC, abstractmethod
from Token import TokenType

class NodeType:
     program = "Program"
     Expression = "Expression"
     InfixExpression = "InfixExpression"
     FloatLiteral = "FloatLiteral"
     IntegerLiteral = "IntegerLiteral"

class Node(ABC):
    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def json(self):
        pass

    @abstractmethod
    def evaluate(self):
        pass

class Statement(Node, ABC):
    pass

class Expression(Node, ABC):
    pass

class Program(Node):
    def __init__(self):
        self.statements = []

    def type(self):
        return NodeType.program

    def json(self):
        return {
            "type": self.type(),
            "statements": [stmt.json() for stmt in self.statements]
        }

    def evaluate(self):
        if not self.statements:
            return None
        return self.statements[-1].evaluate()

class ExpressionStatement(Statement):
    def __init__(self, expression: Expression):
        self.expression = expression

    def type(self):
        return NodeType.Expression

    def json(self):
        return {
            "type": self.type(),
            "expression": self.expression.json()
        }

    def evaluate(self):
        return self.expression.evaluate()

class InfixExpression(Expression):
    def __init__(self, left: Expression, operator: str, right: Expression):
        self.left = left
        self.operator = operator
        self.right = right

    def type(self):
        return NodeType.InfixExpression

    def json(self):
        return {
            "type": self.type(),
            "left": self.left.json(),
            "operator": self.operator,
            "right": self.right.json()
        }

    def evaluate(self):
        left_val = self.left.evaluate()
        right_val = self.right.evaluate()

        if self.operator == '+':
            return left_val + right_val
        elif self.operator == '-':
            return left_val - right_val
        elif self.operator == '*':
            return left_val * right_val
        elif self.operator == '/':
            if right_val == 0:
                raise ValueError("Division by zero")
            return left_val / right_val
        elif self.operator == '^':
            return pow(left_val, right_val)
        elif self.operator == '%':
            return left_val % right_val
        else:
            raise ValueError(f"Unknown operator: {self.operator}")

class FloatLiteral(Expression):
    def __init__(self, value: float):
        self.value = value

    def type(self):
        return NodeType.FloatLiteral

    def json(self):
        return {
            "type": self.type(),
            "value": self.value
        }

    def evaluate(self):
        return self.value

class IntegerLiteral(Expression):
    def __init__(self, value: int, line_no: int = 0, position: int = 0):
        self.value = value
        self.line_no = line_no
        self.position = position

    def type(self):
        return NodeType.IntegerLiteral

    def json(self):
        return {
            "type": self.type(),
            "value": self.value
        }

    def evaluate(self):
        return self.value

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

def build_ast(tokens):
    if not tokens:
        return None

    program = Program()
    current_pos = 0

    while current_pos < len(tokens) and tokens[current_pos].type != TokenType.EOF:
        expression = parse_expression(tokens, current_pos)
        if expression[0]:
            stmt = ExpressionStatement(expression[0])
            program.statements.append(stmt)
        current_pos = expression[1]

    return program

def parse_expression(tokens, pos):
    if pos >= len(tokens):
        return None, pos

    left = parse_primary(tokens, pos)
    if not left[0]:
        return None, left[1]

    return parse_binary_op(tokens, left[0], left[1], 0)

def parse_primary(tokens, pos):
    if pos >= len(tokens):
        return None, pos

    token = tokens[pos]

    if token.type == TokenType.INT:
        return IntegerLiteral(int(token.literal), token.line_no, token.position), pos + 1
    elif token.type == TokenType.FLOAT:
        return FloatLiteral(float(token.literal)), pos + 1
    elif token.type == TokenType.LPAREN:
        pos += 1
        expr = parse_expression(tokens, pos)
        if not expr[0]:
            return None, expr[1]
        pos = expr[1]
        if pos < len(tokens) and tokens[pos].type == TokenType.RPAREN:
            return expr[0], pos + 1
        return None, pos

    return None, pos + 1

def parse_binary_op(tokens, left, pos, precedence):
    while pos < len(tokens) and tokens[pos].type != TokenType.EOF and tokens[pos].type != TokenType.RPAREN:
        token = tokens[pos]
        current_precedence = get_precedence(token.type)

        if current_precedence < precedence:
            break

        operator = token.literal
        pos += 1

        right = parse_primary(tokens, pos)
        if not right[0]:
            return left, right[1]

        pos = right[1]

        next_precedence = 0
        if pos < len(tokens) and tokens[pos].type != TokenType.EOF and tokens[pos].type != TokenType.RPAREN:
            next_precedence = get_precedence(tokens[pos].type)

        if current_precedence < next_precedence:
            right = parse_binary_op(tokens, right[0], pos, current_precedence + 1)
            pos = right[1]

        left = InfixExpression(left, operator, right[0])

    return left, pos

def get_precedence(token_type):
    if token_type in [TokenType.PLUS, TokenType.MINUS]:
        return 1
    elif token_type in [TokenType.ASTERISK, TokenType.SLASH, TokenType.MODULO]:
        return 2
    elif token_type == TokenType.POWER:
        return 3
    return 0
