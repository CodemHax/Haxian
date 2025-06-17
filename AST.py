from abc import ABC , abstractmethod


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
            "type": self.type().value,
            "statements": [{self.type().value : stmt.json()} for stmt in self.statements]
        }


class ExpressionStatement(Statement, ABC):
    def __init__(self, expression: Expression):
        self.expression = expression

    def type(self):
        return NodeType.Expression

    def json(self):
        return {
            "type": self.type().value,
            "expression": self.expression.json()
        }


class  InfixExpression(Expression, ABC):
    def __init__(self, left: Expression, operator: str, right: Expression):
        self.left = left
        self.operator = operator
        self.right = right

    def type(self):
        return NodeType.InfixExpression

    def json(self):
        return {
            "type": self.type().value,
            "left": self.left.json(),
            "operator": self.operator,
            "right": self.right.json()
        }


class  FloatLiteral(Expression, ABC):
    def __init__(self, value: float):
        self.value = value

    def type(self):
        return NodeType.FloatLiteral

    def json(self):
        return {
            "type": self.type().value,
            "value": self.value
        }

class IntegerLiteral(Expression, ABC):
    def __init__(self, value: int, line_no: int = 0, position: int = 0):
        self.value = value
        self.line_no = line_no
        self.position = position

    def type(self):
        return NodeType.IntegerLiteral

    def json(self):
        return {
            "type": self.type().value,
            "value": self.value,
            "line_no": self.line_no,
            "position": self.position
        }
