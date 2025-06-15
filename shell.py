from Lexer import Lexer


DEFINE = True
if __name__ == "__main__":
        while True:
            user_input = input("interpreter> ")
            if user_input.strip().lower() in ("exit", "quit"):  # Allow user to exit
                print("Exiting interpreter.")
                break
            if user_input.strip().endswith('.hax'):
                filename = user_input.strip()
                if filename.endswith('.hax'):
                    print('Detected Haxian program file.')
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
                        if hasattr(token, 'type') and getattr(token.type, 'name', None) == "EOF":
                            break
                except FileNotFoundError:
                    print(f"File not found: {filename}")
                continue
            debug = Lexer(user_input)
            while True:
                token = debug.next_token()
                if token is None:
                    print('Lexer returned None')
                    break
                print(token)
                if hasattr(token, 'type') and getattr(token.type, 'name', None) == "EOF":
                    break
