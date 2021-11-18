# imports
import text2code as t2c
import voice2text as v2t


def main():
    variables = []
    while True:
        file = open("./code.py", "a")
        text = v2t.voice2text()
        text = text.translate()
        if text == "exit":
            break
        # if the users says undo, it will undo the last line of code
        if text == "undo":
            file = open("./code.py", "r")
            file = file.readlines()
            lines = file[:-1]
            file = open("./code.py", "w")
            file.writelines(lines)
            file.close()
            continue
        code = t2c.text2code(text, variables)
        code = code.translate()
        print(code)
        file.write(code)
        file.close()


if __name__ == "__main__":
    main()
