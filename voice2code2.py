# The goal of this program is to convert a voice command to a code

# Import the necessary libraries
import speech_recognition as sr

from voice2code import main


class voice2text:
    def __init__(self):
        self.voice = None
        self.text = None
        self.recognizer = sr.Recognizer()

    # This method, will listen what the user says and translate it to text using the speech recognition library
    def voice_to_text(self):

        with sr.Microphone() as source:

            # It will keep listening until it understand what the user said
            while True:

                # It will listen for one second and adjust for ambient noise, this improves the accuracy
                self.recognizer.adjust_for_ambient_noise(source)
                print(
                    "> Listening ..."
                )  # let the user know that the program is listening
                self.voice = self.recognizer.listen(source)

                # This is an API call, it can fail, so we need to handle the exception
                try:
                    self.text = self.recognizer.recognize_google(self.voice)
                    self.text = self.text.lower()

                    # we let the user know what the API translated
                    print("You said: " + self.text)
                    break

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
            "print": "print",
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
            "divide": "/",
        }

    # This method, will translate the text to code using the commands dictionary
    def text_to_code(self):

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
        elif self.split_text[0] == "variable":
            self.code += self.split_text[1]

        # if the user input starts with equal, it will handle the rest of the input as the value
        elif self.split_text[0] == "equals" or self.split_text[0] == "equal":
            # # if the user input starts with string or a similar word it will handle the rest of the input as a string
            if (
                self.split_text[1] == "string"
                or self.split_text[0] == "stream"
                or self.split_text[0] == "ring"
            ):
                self.code += ' = "'
                self.code += " ".join(self.split_text[2:])
                self.code += '"'
                self.code += " "
            else:
                self.code += "= "
                self.code += " ".join(self.split_text[1:])

        else:
            return

        # write the code to a file
        with open("code2.py", "a") as file:
            file.write(self.code + " ")


def main():
    # keeps listening until the user says "stop"
    while True:
        text = voice2text().voice_to_text()
        if text == "stop":
            break
        code = text2code(text).text_to_code()


if __name__ == "__main__":
    main()
