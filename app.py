# imports
import os
import text2code as t2c
import voice2text as v2t



def main():
    print ("Welcome to Voice2Code")
    variables = []
    while True:
        file = open("./code.py", "a")
        text = v2t.voice2text()
        text = text.translate()
        if text == "exit ":
            break
        # if the users says undo, it will undo the last line of code
        if text == "undo ":
            file = open("./code.py", "r")
            file = file.readlines()
            lines = file[:-1]
            file = open("./code.py", "w")
            file.writelines(lines)
            file.close()
            continue
        if text == "run code ":
            # if the OS is windows, it will run the code in the command line
            if os.name == "nt":
                os.system("python ./code.py")
            else:
                os.system("python3 ./code.py")
            continue
        
        if text == "tab " or text == "tabs " or text == "indent ":
            print ("Indenting")
            file.write("\t")
            continue
        code = t2c.text2code(text, variables)
        code = code.translate()
        print(code)
        file.write(code)
        file.close()


if __name__ == "__main__":
    main()
