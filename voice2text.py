# Jasiel Rivera - jasiel.rivera@upr.edu
# The goal of this program is to convert a voice command to a code


import speech_recognition as sr
import json
import googleapiclient


class voice2text:

    """

    This class stores what the user says and translates it to text.

    ...

    Attributes
    ----------
    voice : str
        The sound that the user said
    text : str
        The text translated from the sound
    recognizer : speech_recognition
        The speech recognition library

    Methods
    -------
    translate()
        This method will listen what the user says and translate it to text using the speech recognition library
    """

    def __init__(self):
        self.voice = None
        self.text = None
        self.recognizer = sr.Recognizer()
        self.phrases = [
            "print",
            "if",
            "else",
            "elif",
            "define",
            "for",
            "while",
            "string",
            "list",
            "dictionary",
            "tab",
            "modulo",
            "two",
            "remainder",
            "variable",
            "run code",
        ]

    def translate(self):
        """
        This method will listen what the user says and translate it to text using the speech recognition library.
        """

        with sr.Microphone() as source:

            # It will keep listening until it understand what the user said
            while True:

                # It will listen for one second and adjust for ambient noise, this improves the accuracy.
                self.recognizer.adjust_for_ambient_noise(source)
                # let the user know when to speak
                print("\nSpeak some code!")
                self.voice = self.recognizer.listen(source)

                # This is an API call, it can fail, so we need to handle the exception
                try:
                    # self.text = self.recognizer.recognize_google(
                    #     self.voice, language="en-US"
                    # )
                    self.text = self.recognizer.recognize_google_cloud(
                        self.voice,
                        credentials_json=None,
                        language="en-US",
                        preferred_phrases=self.phrases,
                    )
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
