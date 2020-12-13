import pyttsx3
import datetime
# ==============================================================
# lib speak to talk
# When install pyaudio usually handle error so it's can sovle by 
# Step1: pip install pywin
# Step2: pipwin install pyaudio
# Py audio don't need import
import speech_recognition as sr

import webbrowser as wb

import os
# import sys

# init shuvi object pyttsx3
shuvi = pyttsx3.init()
# get voice for shuvi
voice = shuvi.getProperty('voices')
# voice[1] : female voice, voice[0] : male voice
shuvi.setProperty('voice', voice[1].id)

def speak(audio):
    print('Shuvi: ' + audio)
    # shuvi.say("Shuvi" + audio)
    shuvi.say(audio)
    shuvi.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I: %M: %p")
    speak(Time)

def welcome():
    hour = datetime.datetime.now().hour
    
    if hour >= 6 and hour < 12:
        speak("Good morning Master")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Master")
    elif hour >= 18 and hour < 24:
        speak("Good Night Master")
    
    speak("How can I help you?")

# create command for Master
def command():
    cmd = sr.Recognizer()
    with sr.Microphone() as source:
        # set time stop before next command
        cmd.pause_threshold = 1
        audio = cmd.listen(source)
    try:
        query = cmd.recognize_google(audio, language='en')
        print("Master :" + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command")
        query = str(input("Your order is: "))
    return query


# time()
# speak("Hello Master!")
# welcome()

if __name__ == "__main__":
    welcome()
    while True:
        query = command().lower()
        if "google" in query:
            speak("What should I search Master?")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on google")
        elif "youtube" in query:
            speak("What should I search Master?")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on youtube")
        # elif "open video" in query:
        # 
            # video = r"C:\..."
            os.startfile(video)
        elif "time" in query:
            time()
        elif "quit" in query:
            speak("Shuvi is quitting Master. Googbye Master")
            quit()
            # sys.exit()


