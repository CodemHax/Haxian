#constants

DIGITS = '0123456789'
#tokens
TT_INT= 'TT_INT'
TT_FLOAT = 'TT_FLOAT'
TT_PlUS = 'TT_PLUS'
TT_MINUS = 'TT_MINUS'
TT_MUL = 'TT_MUL'
TT_DIV = 'TT_DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'

#postion class
class Position:
      def __init__(self , idx , ln , col, fn, ftxt):
          self.idx = idx
          self.ln = ln
          self.col = col
          self.fn = fn
          self.ftxt = ftxt
      def advance(self, current_char):
          self.idx += 1
          self.col += 1

          if current_char == "\n":
             self.ln += 1
             self.col = 0
          return self
      def copy(self):
            return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)



#erroes class
class Error:
    def __init__(self, error_name, details  ,pos_start=None, pos_end=None):
        self.error_name = error_name
        self.details = details
        self.pos_start = pos_start
        self.pos_end = pos_end if pos_end else pos_start.copy() if pos_start else None

    def as_string(self):
        res = f'{self.error_name}: {self.details}'
        res += f' File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        res += f', column {self.pos_start.col + 1}'
        return res

class InvalidCharacterError(Error):
    def __init__(self, details , pos_start=None, pos_end=None):
        super().__init__('Invalid Character', details, pos_start, pos_end)


#token class
class Token:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
       if self.value:
           return f'{self.token_type}:{self.value}'
       else:
           return f'{self.token_type}'

#lexer
class Lexer:
    def __init__(self, text ,fn):
        self.text = text
        self.fn = fn
        self.pos = Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    def make_tokens(self):
        tokens = []
        while self.current_char is not None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(TT_PlUS, self.current_char))
                self.advance()
            elif self.current_char =='-':
                tokens.append(Token(TT_MINUS, self.current_char))
                self.advance()
            elif self.current_char =='*':
                tokens.append(Token(TT_MUL, self.current_char))
                self.advance()
            elif self.current_char =='/':
                tokens.append(Token(TT_DIV, self.current_char))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN, self.current_char))
                self.advance()
            elif self.current_char ==')':
                tokens.append(Token(TT_RPAREN, self.current_char))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], InvalidCharacterError(f"'{char}' is not a valid character", pos_start, self.pos)
        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0
        while self.current_char is not None and (self.current_char in DIGITS or self.current_char == '.'):
            if self.current_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
            num_str += self.current_char
            self.advance()
        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))

def run(text, fn):
    lexer = Lexer(text, fn)
    tokens, error = lexer.make_tokens()
    if error:
        return None, error
    return tokens, None
