# Token definitions for the Haxian math interpreter language
from typing import Any


class TokenType:
    IDENTIFIER = "IDENTIFIER"
    EOF = "EOF"
    ILLEGAL = "ILLEGAL"
    INT = "INT"
    FLOAT = "FLOAT"
    PLUS = "PLUS"
    MINUS = "MINUS"
    ASTERISK = "ASTERISK"
    SLASH = "SLASH"
    POWER = "POWER"
    MODULO = "MODULO"
    ASSIGN = "ASSIGN"
    COMMA = "COMMA"
    # symbols
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    LBRACE = "LBRACE"
    RBRACE = "RBRACE"
    SEMICOLON = "SEMICOLON"


class Token:
      def __init__(self, type: TokenType, literal: Any, line_no : int ,position: int):
        self.type = type
        self.literal = literal
        self.position = position
        self.line_no = line_no

      def __str__(self):
        return f"Token({self.type}, {self.literal}, line: {self.line_no}, pos: {self.position})"

      def __repr__(self):
        return str(self)
