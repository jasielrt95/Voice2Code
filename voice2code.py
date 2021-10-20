
# Importing the libraries
import speech_recognition as sr
import os

# Class for voice2code
class Voice2Code:
    # Initializing the class
    def __init__(self):
        # Initializing the speech recognition
        self.r = sr.Recognizer()
        self.text = ""
        self.code = ""
        self.split_text = []

    # Function to get the voice input
    def get_voice_input(self, audio_file):

        # Opening the audio file
        with sr.AudioFile(audio_file) as source:
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.record(source)

        # Converting the audio to text
        self.text = self.r.recognize_google(audio)
        self.text = self.text.lower()

        print("> Voice input: ",self.text)

        # Returning the text
        return self.text

    # Function to translate the text to code
    def translate_text_to_code(self):

        # Creating a dict of commands (for testing)
        commands = {
            "hello": "print(\"Hello, world\")",
            "if": "if",
            "else": "else",
            "for": "for",
            "while": "while",
            "break": "break",
            "continue": "continue",
            "return": "return",
            "def": "def",
            "class": "class",
            "import": "import",
            "from": "from",
            "print": "print",
            "input": "input",
            "and": "and",
            "or": "or",
            "not": "not",
            "True": "True",
            "False": "False",
            "None": "None",
            "True": "True",
            "False": "False",
            "None": "None",
            "open parentheses": "(",
            "close parentheses": ")",
            "open bracket": "[",
            "close bracket": "]",
            "open curly bracket": "{",
            "close curly bracket": "}",
            "comma": ",",
            "dot": ".",
            "colon": ":",
            "semicolon": ";",
            "plus": "+",
            "minus": "-",
            "multiply": "*",
            "divide": "/",
            "equal": "==",
            "not equal": "!=",
            "greater than": ">",
            "less than": "<",
            "greater than or equal to": ">=",
            "less than or equal to": "<=",
            "increment": "++",
            "decrement": "--",
            "assign": "=",
            "add": "+=",
            "subtract": "-=",
            "multiply": "*=",
            "divide": "/=",
            "modulus": "%",
            "modulus assign": "%=",
            "power": "**",
            "power assign": "**=",
        }

        # Initializing the variables
        self.split_text = self.text.split()


        # Looping through the text
        for word in self.split_text:
            # Checking if the word is in the dict
            if word in commands:
                self.code += commands[word]

            print("> Code: ",self.code)

            # writing code to a python file
            with open("code.py", "w") as code_file:
                print("> Writing Code")
                code_file.write(self.code)


    def run_code(self):
        # Executing the code in the python file
        # if os is windows
        print("> Running code")
        if os.name == "nt":
            os.system("python code.py")
        else:
            os.system("python3 code.py")
            

     



def main():
    # Initializing the voice2code class
    code = Voice2Code()

    # Getting the voice input
    code.get_voice_input('hello.wav')

    # Translating the text to code
    code.translate_text_to_code()

    # Running the code
    code.run_code()

if __name__ == "__main__":
    main()