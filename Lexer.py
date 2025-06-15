from Token import Token, TokenType
from typing import List, Optional, Tuple


class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.position = 1
        self.read_position = 0
        self.line_no = 1
        self.current_char = None

        self.__read_char()

    def  __read_char(self):
        if self.read_position >= len(self.source):
            self.current_char = None
        else:
            self.current_char = self.source[self.read_position]

        self.position = self.read_position
        self.read_position += 1

    def  __skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            if self.current_char == '\n':
                self.line_no += 1
            self.__read_char()

    def __new_token(self, tt , literal) -> Token:
        tok = Token(type=tt, literal= literal, line_no=self.line_no, position=self.position)
        return tok

    def __is__digit(self, char):
        return '0' <= char <= '9'

    def ___read_number(self):
        start_pos = self.position
        dot_Count = 0
        output = ""
        while self.__is__digit(self.current_char) or self.current_char == '.':
            if self.current_char == '.':
                dot_Count += 1
            if dot_Count > 1:
                print(f"Error: Multiple dots in number at line {self.line_no}, position {self.position}")
                return self.__new_token(TokenType.ILLEGAL, output)
            output += self.current_char
            self.__read_char()

            if self.current_char is None:
                break
        if dot_Count == 0:
            return self.__new_token(TokenType.INT, int(output))
        else:
            return self.__new_token(TokenType.FLOAT, float(output))

    def __is_letter(self, char):
        return char is not None and (char.isalpha() or char == '_')

    def __read_identifier(self):
        start_pos = self.position
        output = ''
        while self.__is_letter(self.current_char) or (self.current_char is not None and self.current_char.isdigit()):
            output += self.current_char
            self.__read_char()
            if self.current_char is None:
                break
        return self.__new_token(TokenType.IDENTIFIER, output)

    def next_token(self)  -> Token:
        tok : Token = None
        self.__skip_whitespace()

        if self.current_char is not None:
            print(f"DEBUG: current_char='{self.current_char}', ord={ord(self.current_char)}")
        else:
            print("DEBUG: current_char=None")
        match self.current_char:
            case '+':
                tok = self.__new_token(TokenType.PLUS, self.current_char)
            case '-':
                tok = self.__new_token(TokenType.MINUS, self.current_char)
            case  '*':
                tok = self.__new_token(TokenType.ASTERISK, self.current_char)
            case '/':
                tok = self.__new_token(TokenType.SLASH, self.current_char)
            case '^':
                tok = self.__new_token(TokenType.POWER, self.current_char)
            case '%':
                tok = self.__new_token(TokenType.MODULO, self.current_char)
            case '(':
                tok = self.__new_token(TokenType.LPAREN, self.current_char)
            case ')':
                tok = self.__new_token(TokenType.RPAREN, self.current_char)
            case  '{':
                tok = self.__new_token(TokenType.LBRACE, self.current_char)
            case  ';':
                tok = self.__new_token(TokenType.SEMICOLON, self.current_char)
            case None:
                tok = self.__new_token(TokenType.EOF, "")
            case _:
                if self.__is__digit(self.current_char):
                    tok = self.___read_number()
                elif self.__is_letter(self.current_char):
                    tok = self.__read_identifier()
                else:
                    tok = self.__new_token(TokenType.ILLEGAL, self.current_char)
        self.__read_char()
        return tok
