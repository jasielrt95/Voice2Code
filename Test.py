import unittest
import text2code as t2c

class Test(unittest.TestCase):

    """
        This class is used to test keywords and evaluate them with expected result using the
        unittest library.

        ...

        Attributes
        ----------
        testList : list
            The list of variables that are being used in the code
        text : str
            The text that is going to be translated into code
        code : str
            The code that will be generated from the text

        Methods
        -------
        test_define():
            This method will test multiple cases of the define keyword
        test_if():
            This method will test multiple cases of the if keyword
        test_elif():
            This method will test multiple cases of the elif keyword
        test_else():
            This method will test multiple cases of the else keyword
        test_for():
            This method will test multiple cases of the for keyword
        test_while():
            This method will test multiple cases of the while keyword
        test_print():
            This method will test multiple cases of the print keyword 
    """

    def test_define(code):

        """ This method will test multiple cases of the define keyword 

        Parameters
        ----------
        text : str
        The text that is going to be translated into code
        
        code : str
        The code that will be generated from the text
        """

        testList = []

        text = t2c.text2code("define x 4",testList)

        code.assertEqual(text.translate(), "x = 4\n")

        text.set_text("define x string Jasiel es estudioso")

        code.assertEqual(text.translate(), 'x = "jasiel es estudioso"\n')

        text.set_text("Define studios list math cs spanish history")

        code.assertEqual(text.translate(), "studios = [math, cs, spanish, history]\n")

        text.set_text("Define subtitute dictionary a b c d")

        code.assertEqual(text.translate(), "subtitute = {a: b, c: d}\n")


    def test_if(code):

        """ This method will test multiple cases of the if keyword 

        Parameters
        ----------
        text : str
        The text that is going to be translated into code

        code : str
        The code that will be generated from the text
        """

        testList = []

        text = t2c.text2code("if x > 7",testList)

        code.assertEqual(text.translate(), "if x > 7: \n")

        text.set_text("if salaries greater than tax")

        code.assertEqual(text.translate(), "if salaries > tax: \n")

        text.set_text("if salaries greater than tax and tax less than wages")

        code.assertEqual(text.translate(), "if salaries > tax and tax < wages: \n")

    def test_elif(code):

        """ This method will test multiple cases of the elif keyword 

        Parameters
        ----------
        text : str
        The text that is going to be translated into code

        code : str
        The code that will be generated from the text
        """

        testList = []

        text = t2c.text2code("elif x > 6",testList)

        code.assertEqual(text.translate(), "elif x > 6: \n")

        text.set_text("elif counter greater than 2")

        code.assertEqual(text.translate(), "elif counter > 2: \n")

        text.set_text("elif shoeSize greater than 7 and shoeSize less than 11")

        code.assertEqual(text.translate(), "elif shoesize > 7 and shoesize < 11: \n")

    def test_else(code):

        """ This method will test multiple cases of the else keyword 

        Parameters
        ----------
        text : str
        The text that is going to be translated into code

        code : str
        The code that will be generated from the text
        """
        
        testList = []

        text = t2c.text2code("else",testList)

        code.assertEqual(text.translate(), "else: \n")

        text.set_text("else return true")

        code.assertEqual(text.translate(), "else return True: \n")

    def test_for(code):

        """ This method will test multiple cases of the for keyword 

        Parameters
        ----------
        text : str
        The text that is going to be translated into code

        code : str
        The code that will be generated from the text
        """
        
        testList = []

        text = t2c.text2code("for range x 4",testList)

        code.assertEqual(text.translate(), "for x in range(4): \n")

        text.set_text("for list x candy")

        code.assertEqual(text.translate(), "for x in candy: \n")

    def test_while(code):

        """ This method will test multiple cases of the while keyword 

        Parameters
        ----------
        text : str
        The text that is going to be translated into code

        code : str
        The code that will be generated from the text
        """
        
        testList = []

        text = t2c.text2code("while x greater than 6",testList)

        code.assertEqual(text.translate(), "while x > 6: \n")

        text.set_text("while true")

        code.assertEqual(text.translate(), "while True: \n")

    def test_print(code):

        """ This method will test multiple cases of the print keyword 
        
        Parameters
        ----------
        text : str
        The text that is going to be translated into code

        code : str
        The code that will be generated from the text
        """
        
        testList = ["x"]

        text = t2c.text2code("print x",testList)

        code.assertEqual(text.translate(), "print(x)\n")

        text.set_text("print expression 1 plus y")

        code.assertEqual(text.translate(), "print(1 + y)\n")

        text.set_text("print expression x plus y minus z divided by 2 times 4")

        code.assertEqual(text.translate(), "print(x + y - z / 2 * 4)\n")

        text.set_text("print string hello world")

        code.assertEqual(text.translate(), 'print("hello world")\n')



if __name__ == '__main__':
    unittest.main()