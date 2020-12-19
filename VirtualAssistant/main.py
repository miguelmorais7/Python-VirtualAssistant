import speech_recognition as sr
import pyttsx3
import pywhatkit
import sys
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def playYT(command):
    song = command.replace('play', '')
    talk('playing' + song)
    pywhatkit.playonyt(song)
    sys.exit()

def timeShow(command):
    time = datetime.datetime.now().strftime('%H:%M')
    print(time)
    talk('Current time is ' + time)

def personWikipedia(command):
    person = command.replace('who is', '')
    info = wikipedia.summary(person, 1)
    print(info)
    talk(info)

def openGmail(command):
    webbrowser.open_new_tab("gmail.com")
    talk('gmail is open now')

def openGoogle(command):
    webbrowser.open_new_tab("google.com")
    talk('google is open now')

def openGithub(command):
    webbrowser.open_new_tab("github.com")
    talk('github is open now')

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_assistant():
    command = take_command()
    if 'play' in command:
        playYT(command)
    elif 'time' in command:
        timeShow(command)
    elif 'who is' in command:
        personWikipedia(command)
    elif 'date' in command:
        talk('sorry, i have a boyfriend')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'gmail' in command:
        openGmail(command)
    elif 'google' in command:
        openGoogle(command)
    elif 'github' in command:
        openGithub(command)
    else:
        talk('Please, say the command again')

while True:
    run_assistant()
