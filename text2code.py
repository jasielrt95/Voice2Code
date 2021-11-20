class text2code:
    """
    This class is used to represent the code that will be generated from the text

    ...

    Attributes
    ----------
    variables : list
        The list of variables that are being used in the code
    text : str
        The text that is going to be translated into code
    split_text : list
        The text that is split into a list of words
    code : str
        The code that will be generated from the text

    Methods
    -------
    translate()
        This method will translate the text into code
    clean_text()
        This method will look for expresions like "plus", "times", etc. and replace them with the correct code
    add_variable()
        This method will add a variable to the list of variables
    print_handler()
        This method will handle the printing command
    if_handler()
        This method will handle the if command
    elif_handler()
        This method will handle the elif command
    else_handler()
        This method will handle the else command
    variable_handler()
        This method will handle variable creation
    """

    def __init__(self, text, variables):

        """
        Parameters
        ----------
        variables : list
            The list of variables that are being used in the code
        text : str
            The text that is going to be translated into code
        split_text : list
            The text that is split into a list of words
        code : str
            The code that will be generated from the text
        """
        self.variables = variables
        self.text = text
        self.clean_text()
        self.split_text = self.text.split()
        self.code = None

    def set_text(self, text):
        self.text = text

    def clean_text(self):
        """
        Look for expresions like "plus", "times", "minus", etc. in the text and replace them with the correct code
        """
        symbols = {
            "plus": "+",
            "minus": "-",
            "times": "*",
            "equals": "==",
            "equal": "==",
            "not equals": "!=",
            "and": "and",
            "or": "or",
            "greater than": ">",
            "less than": "<",
            "divided by": "/",
            "modulo": "%",
            "new line": "\n",
            "tab": "\t",
            "space": " ",
            "next line": "\n",
            "nextline": "\n",
            "newline": "\n",
            "true": "True",
            "false": "False",
        }

        for symbol in symbols:
            self.text = self.text.replace(symbol, symbols[symbol])

    def add_variable(self, variable):
        """
        This method will add a variable to the list of variables.

        Parameters
        ----------
        variable : str
            The variable that is going to be added to the list of variables
        """
        if variable not in self.variables:
            self.variables.append(variable)

    def variable_handler(self):
        code = None
        """
        This method will handle variable creation. It will be called when the users says a command that starts with "Define". For example, "Define salaries 100" -> "salaries = 100".
        """

        # since we are creating a new variable, add that variable to the list of variables
        self.add_variable(self.split_text[1])

        # This will handle definitions like the following: "define salaries 1000" -> "salaries = 1000"
        if len(self.split_text) == 3:
            code = self.split_text[1] + " = " + self.split_text[2] + "\n"
            return code

        # handle string values
        elif self.split_text[2] == "string":
            code = self.split_text[1] + ' = "' + " ".join(self.split_text[3:]) + '"\n'
            return code

        # handle dictionary creation
        elif self.split_text[2] == "dictionary":
            code = self.split_text[1] + " = {"
            for i in range(3, (len(self.split_text) - 1), 2):
                code += self.split_text[i] + ": " + self.split_text[i + 1] + ", "

            code = code[:-2] + "}\n"
            return code

        # handle list creation
        elif self.split_text[2] == "list":
            code = self.split_text[1] + " = ["
            for word in self.split_text[3:]:
                code += word + ", "

            code = code[:-2] + "]\n"
            return code

        # handle more complex variable creations
        elif len(self.split_text) > 3:
            code = self.split_text[1] + " = " + " ".join(self.split_text[2:]) + "\n"
            return code

    def print_handler(self):
        """
        This method will handle the printing command. It will be called when the users says a command that starts with "Print". For example, "Print hello world" -> "print('hello world')". If any of the words in the text are variables, they will be replaced with the correct code.
        """
        code = "print("
        continue_string = False
        if self.split_text[1] == "string":
            for word in self.split_text[2:]:
                code += word + " "
            return code[:-1] + '")\n'
        for word in self.split_text[1:]:
            # if the word is a variable, we print as a variable
            if word in self.variables:
                if continue_string:
                    code += '", ' + word + ","
                else:
                    code += word + ", "
                continue_string = False
            # if its not a variable, we print as a string
            else:
                if continue_string:
                    code += " " + word

                else:
                    code += '"' + word
                continue_string = True

        if continue_string:
            code += '")\n'
            return code
        else:
            code = code[:-2] + ")\n"
            return code

    def if_handler(self):
        """
        This method will handle the if command. It will be called when the users says a command that starts with "If". For example, "If salary greater than 1000" -> "if salary > 1000:".
        """
        code = "if "

        if len(self.split_text) == 2:
            code = "if " + self.split_text[1] + ": \n"
            return code

        elif len(self.split_text) > 2:
            for word in self.split_text[1:-1]:
                code += word + " "

        code += self.split_text[-1] + ": \n"
        return code

    def elif_handler(self):
        """
        This method will handle the elif command. It will be called when the users says a command that starts with "Elif". For example, "Elif salary greater than 1000" -> "elif salary > 1000:".
        """
        code = "elif "

        if len(self.split_text) == 2:
            code = "elif " + self.split_text[1] + ": \n"
            return code

        elif len(self.split_text) > 2:
            for word in self.split_text[1:-1]:
                code += word + " "
        code += self.split_text[-1] + ": \n"
        return code

    def else_handler(self):
        """
        This method will handle the else command. It will be called when the users says a command that starts with "Else". For example, "Else" -> "else:".
        """
        code = "else "

        if len(self.split_text) == 1:
            code = "else: \n"
            return code

        elif len(self.split_text) == 2:
            code = "else " + self.split_text[1] + ": \n"
            return code

        elif len(self.split_text) > 2:
            for word in self.split_text[1:-1]:
                code += word + " "
            code += self.split_text[-1] + ": \n"
            return code

    def while_handler(self):
        """
        This method will handle the while command. It will be called when the users says a command that starts with "While". For example, "While salary greater than 1000" -> "while salary > 1000:".
        """
        code = "while "

        if len(self.split_text) == 2:
            code = "while " + self.split_text[1] + ": \n"
            return code

        elif len(self.split_text) > 2:
            for word in self.split_text[1:-1]:
                code += word + " "

        code += self.split_text[-1] + ": \n"
        return code

    def for_handler(self):
        """
        This method will handle the for command. It will be called when the users says a command that starts with "For". For example, "For i in range(10):" -> "for i in range(10):".
        """
        code = "for "

        if self.split_text[1] == "range":
            code += self.split_text[2] + " in range(" + self.split_text[3] + "): \n"
            return code
        elif self.split_text[1] == "list":
            code += self.split_text[2] + " in " + self.split_text[3] + ": \n"
            return code

    def new_line_handler(self):
        """
        This method will handle the new line command. It will be called when the users says a command that starts with "New line". For example, "New line" -> "\n".
        """
        code = "\n"
        return code

    def tab_handler(self):
        """
        This method will handle the tab command. It will be called when the users says a command that starts with "Tab". For example, "Tab" -> "\t".
        """
        code = "\t"
        return code

    def translate(self):
        """
        This method will translate the text into code. It checks for key words in the user command and calls the appropriate method.
        """
        if len(self.split_text) > 0:

            # Definining variables handler
            if self.split_text[0] == "define" and len(self.split_text) > 2:
                self.code = self.variable_handler()

            # Print handler
            elif self.split_text[0] == "print" and len(self.split_text) > 1:
                self.code = self.print_handler()

            # If handler
            elif self.split_text[0] == "if" and len(self.split_text) >= 2:
                self.code = self.if_handler()

            # Elif handler
            elif self.split_text[0] == "ellis" and len(self.split_text) >= 2:
                self.code = self.elif_handler()

            # Else handler
            elif self.split_text[0] == "else":
                self.code = self.else_handler()

            # While handler
            elif self.split_text[0] == "while" and len(self.split_text) >= 2:
                self.code = self.while_handler()

            # For handler
            elif self.split_text[0] == "for" and len(self.split_text) > 3:
                self.code = self.for_handler()

            else:
                self.code = ""

        else:
            # New line handler
            if self.text == "\n":
                self.code = self.new_line_handler()
            else:
                self.code = ""

        return self.code
