import haxian

while True:
    text = input("hexian >")
    result , error = haxian.run(text , "<stdin>")

    if error:
        print(error.as_string())
    else:
        print(result)
