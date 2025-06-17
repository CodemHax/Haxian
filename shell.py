from Lexer import Lexer, TokenType
from Parser import Parser
from Token import Token
from AST import*

def main():
    while True:
        user_input = input("Haxian> ")
        if user_input.strip().lower() in ("exit", "quit"):
            print("Exiting interpreter.")
            break
        if user_input.strip().endswith('.hax'):
            filename = user_input.strip()
            try:
                with open(filename, "r") as file:
                    source = file.read()
                debug = Lexer(source)
                while True:
                    token = debug.next_token()
                    if token is None:
                        print('Lexer returned None')
                        break
                    print(token)
                    if token.type == TokenType.EOF:
                        break
            except Exception as e:
                print(f"Error: {e}")
        else:
            try:
                lexer = Lexer(user_input)
                tokens = lexer.tokenize()

                if tokens and tokens[0].type != TokenType.EOF:
                    result = evaluate_arithmetic(tokens)

                    parser_lexer = Lexer(user_input)
                    parser = Parser(parser_lexer)

                    if not parser.errors:
                        print(result)
                    else:
                        print(f"Result: {result} (with parser errors)")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()

