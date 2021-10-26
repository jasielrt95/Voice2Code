# The goal of this program is to convert a voice command to a code

# Import the necessary libraries
import speech_recognition as sr

# Using the speech recognition librarie we receive the voice data
class voice2text:
    def __init__(self):
        self.voice = None
        self.text = None
        self.recognizer = sr.Recognizer()

    # This method, will listen what the user says and translate it to text using the speech recognition library
    def translate(self):

        with sr.Microphone() as source:

            # It will keep listening until it understand what the user said
            while True:

                # It will listen for one second and adjust for ambient noise, this improves the accuracy
                self.recognizer.adjust_for_ambient_noise(source)
                print(
                    "> Listening ...\n"
                )  # let the user know that the program is listening
                self.voice = self.recognizer.listen(source)

                # This is an API call, it can fail, so we need to handle the exception
                try:
                    self.text = self.recognizer.recognize_google(self.voice)
                    self.text = self.text.lower()

                    # we let the user know what the API translated
                    print("> You said: " + self.text + "\n")
                    break

                # in case that the data is inaudible we use .UnknownValueError
                # to let them know
                except sr.UnknownValueError:
                    print("Could not understand audio")

                except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))

        return self.text


class text2code:
    def __init__(self, text):
        self.text = text
        self.split_text = self.text.split()
        self.code = ""
        self.commands = {
            "example": "print(\"Welcome to Voice2Code, I hope you like it\")",
            "print": "print (",
            "open parenthesis": "(",
            "close parenthesis": ")",
            "open parentheses": "(",
            "close parentheses": ")",
            "open bracket": "[",
            "close bracket": "]",
            "open brackets": "[",
            "close brackets": "]",
            "open brace": "{",
            "close brace": "}",
            "open braces": "{",
            "close braces": "}",
            "plus": "+",
            "minus": "-",
            "multiply": "*",
            "multiplied": "*",
            "multiplied by": "*",
            "times": "*",
            "divided": "/",
            "divided by": "/",
            "true": "True",
            "through": "True",
            "two dots": ":",
            "if": "if (",
            "while": "while (",
            "space": "  ",
            "new line": "\n",
            "newline": "\n",
            "next line": "\n",
            "nextline": "\n",
        }

    # This method, will translate the text to code using the commands dictionary
    def translate(self):

        # if the user input is in the commands dictionary, it will write the code
        if self.text in self.commands:
            self.code = self.commands[self.text]

        # if the user input starts with string or a similar word it will handle the rest of the input as a string
        elif (
            self.split_text[0] == "string"
            or self.split_text[0] == "stream"
            or self.split_text[0] == "ring"
        ):
            self.code += '"'
            self.code += " ".join(self.split_text[1:])
            self.code += '"'
            self.code += " "

        # if the user input starts with variable, it will handle the rest of the input as the variable name
        elif self.split_text[0] == "variable" or self.split_text[0] == "bearable":
            self.code += self.split_text[1]

        # if the user input starts with equal, it will handle the rest of the input as the value
        elif self.split_text[0] == "assign" or self.split_text[0] == "assigns":
            # # if the user input starts with string or a similar word it will handle the rest of the input as a string
            if (
                self.split_text[1] == "string"
                or self.split_text[1] == "stream"
                or self.split_text[1] == "ring"
            ):
                self.code += ' = "'
                self.code += " ".join(self.split_text[2:])
                self.code += '"'
                self.code += " "
            else:
                self.code += "= "
                self.code += " ".join(self.split_text[1:])

        elif self.split_text[0] == "equals" or self.split_text[0] == "equal":
            # # if the user input starts with string or a similar word it will handle the rest of the input as a string
            if (
                self.split_text[1] == "string"
                or self.split_text[1] == "stream"
                or self.split_text[1] == "ring"
            ):
                self.code += '== "'
                self.code += " ".join(self.split_text[2:])
                self.code += '"'
                self.code += " "
            else:
                self.code += "== "
                self.code += " ".join(self.split_text[1:])

        elif self.split_text[0] == "for" and self.split_text[1] == "loop":
            self.code += "for "
            self.code += self.split_text[2]
            self.code += " in "
            self.code += " ".join(self.split_text[3:])
        
        elif self.split_text[0] == "list" or self.split_text[0] == "array":
            self.code += "= ["
            self.code += ", ".join(self.split_text[1:])
            self.code += "]"
        else:
            return

        # write the code to a file
        with open("code.py", "a") as file:
            if self.code != "\n":
                file.write(self.code)
            else:
                file.write(self.code + " ")


# this function creates a simple header
def header_generator(title, description=None):
    if description == None:
        print("*" * 50, title, "*" * 50)
        print("*" * 40)
    else:
        # Print centered title
        print(title.center(140, "*"))
        print("\n" + description + "\n")
        print("*" * 140)


def main():

    header_generator(
        "Kavita Project",
        "This program will convert your voice into python code.\n\nTry saying 'Example'\n\nFor a full list of commands say 'help'\n\nTo exit say 'close editor'\n\n***Only talk whe the console displays 'listening ...'***\n",
    )

    # keeps listening until the user says "exit code"
    while True:
        # Taking the data from the voice input and storing it
        voice_translator = voice2text()
        text = voice_translator.translate()

        # While its still listening, if it detects the word "exit code" it will exit
        if text == "close editor":
            break
        code = text2code(text).translate()


if __name__ == "__main__":
    main()
