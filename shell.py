from Lexer import Lexer
from Token import TokenType
from arth import evaluate_arithmetic


DEFINE = True
if __name__ == "__main__":
        while True:
            user_input = input("interpreter> ")
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
                lexer = Lexer(user_input)
                tokens = lexer.tokenize()

                if tokens and tokens[0].type != TokenType.EOF:
                    result = evaluate_arithmetic(tokens)
                    print(f"{result}")
