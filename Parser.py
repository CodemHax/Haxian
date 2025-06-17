from Lexer import Lexer
from Token import Token, TokenType
from enum import IntEnum
from typing import Callable

from AST import *


class PrecedenceType(IntEnum):
      P_LOWEST = 1
      P_EQUALS = 2
      P_LESSGREATER = 3
      P_SUM = 4
      P_PRODUCT = 5
      P_EXPONENT = 6
      P_PREFIX = 7
      P_CALL = 8
      P_INDEX = 9
      P_GET = 10
      P_SET = 11

PRECEDENCE = {
    TokenType.PLUS: PrecedenceType.P_SUM,
    TokenType.MINUS: PrecedenceType.P_SUM,
    TokenType.ASTERISK: PrecedenceType.P_PRODUCT,
    TokenType.SLASH: PrecedenceType.P_PRODUCT,
    TokenType.POWER: PrecedenceType.P_EXPONENT,
    TokenType.MODULO: PrecedenceType.P_EXPONENT,
    TokenType.LPAREN: PrecedenceType.P_CALL,
    TokenType.LBRACE: PrecedenceType.P_GET,
}

class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.errors = []
        self.current_token = None
        self.peek_token = None
        self.prefix_parse_fns = {
            TokenType.INT: self.__parse_integer_literal,
            TokenType.FLOAT: self.__parse_float_literal,
            TokenType.LPAREN: self.__parse_grouped_expression,
        }
        self.infix_parse_fns = {
            TokenType.PLUS: self.__parse_infix_expression,
            TokenType.MINUS: self.__parse_infix_expression,
            TokenType.ASTERISK: self.__parse_infix_expression,
            TokenType.SLASH: self.__parse_infix_expression,
            TokenType.POWER: self.__parse_infix_expression,
            TokenType.MODULO: self.__parse_infix_expression,
            TokenType.LPAREN: self.__parse_call_expression,
            TokenType.LBRACE: self.__parse_get_expression,
        }

        # Initialize tokens
        self.__next_token()
        self.__next_token()

    def register_prefix(self, token_type: TokenType, fn: Callable):
        self.prefix_parse_fns[token_type] = fn

    def __next_token(self):
        """
        Fixed recursive method by renaming and updating the implementation
        """
        self.current_token = self.peek_token
        self.peek_token = self.lexer.next_token()

    # Alias for compatibility with existing code
    def __next__Token(self):
        self.__next_token()

    def __peek__Token(self, tt: TokenType):
        return self.peek_token.type == tt

    def __expect__Token(self, tt: TokenType):
        if self.__peek__Token(tt):
            self.__next_token()
            return True
        else:
            self.__peek__error()
            return False

    def __current__precedence(self):
        return PRECEDENCE.get(self.current_token.type, PrecedenceType.P_LOWEST)

    def __next__precedence(self):
        return PRECEDENCE.get(self.peek_token.type, PrecedenceType.P_LOWEST)

    def __peek__error(self):
        self.errors.append(f"Expected {self.peek_token.type}, got {self.current_token.type}")

    def __no_prefix__parse(self, token: Token):
        self.errors.append(f"No prefix parse function for {token.type} found")
        return None

    def parse_program(self):
        program = Program()
        while self.current_token.type != TokenType.EOF:
            statement = self.__parse_statement()
            if statement is not None:
                program.statements.append(statement)
            self.__next_token()

        return program

    def __parse_statement(self):
       return self.__parse_expression_statement()

    def __parse_expression_statement(self):
        expression = self.__parse_expression(PrecedenceType.P_LOWEST)
        if expression is None:
            return None

        if self.current_token.type == TokenType.SEMICOLON:
            self.__next_token()

        smt = ExpressionStatement(expression)
        return smt

    def __parse_expression(self, precedence: PrecedenceType):
        prefix = self.prefix_parse_fns.get(self.current_token.type)
        if prefix is None:
            self.__no_prefix__parse(self.current_token)
            return None

        left_node = prefix()
        if left_node is None:
            return None

        while not self.__peek__Token(TokenType.SEMICOLON) and precedence < self.__next__precedence():
            infix = self.infix_parse_fns.get(self.peek_token.type)
            if infix is None:
                return left_node
            self.__next_token()
            left_node = infix(left_node)
        return left_node

    def __parse_infix_expression(self, left_node: Expression):
        # Create infix expression with correct parameters matching the constructor in AST.py
        operator = self.current_token.literal
        precedence = self.__current__precedence()
        self.__next_token()
        right_node = self.__parse_expression(precedence)
        if right_node is None:
            return None

        return InfixExpression(left_node, operator, right_node)

    def __parse_grouped_expression(self):
        self.__next_token()
        expression = self.__parse_expression(PrecedenceType.P_LOWEST)
        if not self.__expect__Token(TokenType.RPAREN):
            return None
        return expression

    def __parse_integer_literal(self):
        if self.current_token.type != TokenType.INT:
            self.__peek__error()
            return None

        try:
            value = int(self.current_token.literal)
        except ValueError:
            self.errors.append(f"Invalid integer literal: {self.current_token.literal}")
            return None

        integer_literal = IntegerLiteral(value, self.current_token.line_no, self.current_token.position)
        return integer_literal

    def __parse_float_literal(self):
        """
        Add implementation for float literal parsing
        """
        if self.current_token.type != TokenType.FLOAT:
            self.__peek__error()
            return None

        try:
            value = float(self.current_token.literal)
        except ValueError:
            self.errors.append(f"Invalid float literal: {self.current_token.literal}")
            return None

        float_literal = FloatLiteral(value)
        return float_literal

    def __parse_call_expression(self, function: Expression):
        """
        Add implementation for parsing function calls
        """
        # Placeholder implementation - would need to be expanded for real function calls
        self.errors.append("Function calls not yet implemented")
        return function

    def __parse_get_expression(self, object_expr: Expression):
        """
        Add implementation for property access expressions
        """
        # Placeholder implementation - would need to be expanded for real property access
        self.errors.append("Property access not yet implemented")
        return object_expr
