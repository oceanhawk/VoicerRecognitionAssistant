# Voice Recognition Software
# James Prototype Version 1

import speech_recognition as sr # package for the voice recognition
import pyttsx3 # package text to speech
import pywhatkit # Package for youtube searches
import datetime # package for date and time
import wikipedia # package for wikipedia




listener = sr.Recognizer() # recognizes input voice
engine = pyttsx3.init() # initializes text to speech
voices = engine.getProperty("voices") # gets the voices python text to speech (pyttsx3) provides
engine.setProperty("voice", voices[8].id) # sets the voice, different number different voice
engine.setProperty("rate", 180) # sets speed percent, can be more than 100
engine.setProperty("volume", 0.7) # sets volume 0-1
# Convert this into def function later
# Entrance at beginning

engine.say("I am here Sir")
engine.say("What can I do for you?")
engine.runAndWait()

# Function for talking
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source: # Using the default microphone as source
            print("listening...")
            voice = listener.listen(source) # tells the speech recognizer to listen to the microphone
            command = listener.recognize_google(voice) # Uses google Api for the voice
            command = command.lower() # sets command to lower case
            if "james" in command:
                command = command.replace("james", "") # replaces the variable in print output
                print(command)
    except:
        pass
    return command

def run_james():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing " + song)
        pywhatkit.playonyt(song) # plays the song on youtube
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p") # string format of the time
        print(time)
        talk("Current time is " + time)
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1) # number defines sentences from wikipedia
        print(info)
        talk(info)
    elif "okay" in command:
        talk("I am good Sir, how are you")
    elif "good" in command:
        talk("Great to hear you are doing well Sir.")
    elif "weather" in command:
        talk("Why don't you look outside")
    else:
        talk("Can you repeat again Sir")


while True:
    run_james()
