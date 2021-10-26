# Kavita Project 
- Research experience under Dra. Patricia Ordóñez supervision.
- Create a prototype through the integration of modified versions of open-source assistive technologies for Kavita, a student with spinal muscular atrophy (SMA) to make it easier for her to program by having a voice interface.

## Proof of Concept
The goal behind this project is to create a coding tool for programers with disabilities or who are not able to program (in the typical way). With this program they will be able to record themselves talkinh in a natural way and the program will translate it into code. 


## Requeriments
- Python 3.5+ 
- SpeechRecognition
- PyAudio

To install theses:

- Windows

```
pip install SpeechRecognition
pip install pyaudio
```
- if pip fails to install pyaudio on windows use pipwin ( remember to add the script folder of your Python installation to PATH)
```
pip install pipwin
pipwin install pyaudio
```
- Linux and MacOS
```
pip3 install SpeechRecognition
pip3 install pyaudio
```


Developed by Jasiel Rivera and Juan Hernandez

<br /> <br /> 


 # User Guide for Kavita Proyect: Voice2Code
## Quick Start
Once you run the script, you will be displayed a welcome message.
```
***************************************************************Kavita Project*******************************************

This program will convert your voice into python code.

Try saying 'Example'

For a full list of commands say 'help'

To exit say 'close editor'

***Only talk whe the console displays 'listening ...'***


************************************************************************************************************************
```

After that, the microphone will start to receive input for one second 
(1s) to normalize audio recording (for better results). * Do not talk during this second *

Once the terminal displays: *"Listening..."*, you can talk to the 
microphone.

```
> Listening ...
```

After you hava spoken, the terminal will show you what you 
said (or what it understood) like this:

*"variable x"*

<br /> 

```
> You said: variable x
```

<br /> 

You **MUST** wait until the *"Listening..."* message shows before talking 
again.

The code will be in a .py file that will be generated automatically 

If you want to see an example of the code that the script can generate say "example" 

For a list of commands you can say *"help"*

If you want to stop running the script, you can say *"close editor"*

<br /> 

---

<br /> 

## Creating Variables 

To create a variable you must say the word "variable" before saying the name of the variable.

- Example: *"variable x"*

This will create the following output on the terminal:

<br /> 

```
> You said: variable x
```

<br /> 

And create the following code:

<br /> 

```
x
```

<br /> 

---

<br /> 

## Creating Strings 

To create a string you must say the word "string" followed by the 
actual string.

Example: *"string hello world"*

This will create the following output on the terminal:

<br /> 

```
> You said: string hello world
```

<br /> 

And create the following code:

<br /> 

```
"hello world"
```

<br /> 

---

<br /> 

## Mathematical notation

To create basic mathematical symbols you must say it as shown on the following examples:

### Examples:

- `+`  :  *"plus"*
- `-`  :  *"minus"*
- `*`  :  *"multiply or multiplied by or times"*
- `/`  :  *"divided by or divided"*
- `=` : equals

This will create the following output on the terminal:

### Example: *"a plus b equals c"*

<br /> 

```
> You said: a plus b equals c
```

<br /> 

And create the following code:

<br /> 

```
a + b = c
```

<br /> 

---

<br /> 

