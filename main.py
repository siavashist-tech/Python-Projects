import pyttsx3  # it is a text-to-speech library. # pip install pyttsx3
import speech_recognition as speech_r  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')  # Speech API, Helps in synthesis and recognition of voice
voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', voices[1])

print("Dyno says: In order for me to work speak commands like:\n", "Sonam Bajwa Wikipedia \n", "open youtube \n",
      "open google chrome\n", "open tutorialspoint\n", "play music\n", "open music application\n", "what is the time")


def speak(audio):  # to convert our text to speech.
    engine.say(audio)
    engine.runAndWait()


def wishMe():  # greet the user
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Hi! Good Morning, Have a great day.")

    elif 12 <= hour < 18:
        speak("Hi! Good Afternoon, Hope You're having a great day.")

    else:
        speak("Hi! Good Evening, I hope you've had a great day")

    speak("I am Dyno - Your Virtual Assistant,How may I help you Sir or Ma'am")


def takeCommand():  # It takes microphone input from the user and returns string output
    r = speech_r.Recognizer()
    with speech_r.Microphone() as source:
        print("DYNO: I am Listening... You can speak now.")
        r.pause_threshold = 1  # Non-speaking audio before a phrase is considered to be complete.
        audio = r.listen(source)

    try:
        print("DYNO: Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f'User said: {query}\n')  # User query will be printed.

    except Exception as e:  # handle errors effectively
        print("DYNO: Could you please repeat with a clear voice...")  # will be printed in case of improper voice
        return "None"  # None string will be returned
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:  # code query for youtube
            webbrowser.open("youtube.com")

        elif 'open google chrome' in query:  # code query for google
            webbrowser.open("google.com")

        elif 'open tutorialspoint' in query:  # code query for study material
            webbrowser.open("www.tutorialspoint.com")

        elif 'open music application' in query:
            codePath = "C:\\Users\\USER-PC\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codePath)

        elif 'play music' in query:  # code query for music
            music_dir = 'C:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'the time' in query:
            stringTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {stringTime}")
            print(stringTime)
