import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install speechRecognition
import wikipedia  # pip install wikipeadia
import webbrowser
import os
import random
import pyaudio  # pip install pyaudio

engine = pyttsx3.init('sapi5')  # here we initialize the engine
# here we get the voice for program speak
voices = engine.getProperty('voices')
# here we set the voice of windows for response
engine.setProperty('voice', voices[1].id)

# we write the speak function for results


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# wishme function is use for wish user according to time


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("good morning! ")

    elif hour >= 12 and hour < 18:
        speak("good afternoon! ")

    else:
        speak("good evening! ")

    speak("I am Alexa , Please tell me how may i help you... ")

# takeCommand function is use for taking command from microphone


def takeCommand():
    # it takes audio as a input and give output according to your input.........

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said {query} \n")

    except Exception as e:
        # print(e)
        print("Say that again...")
        return "None"
    return query


if __name__ == "__main__":
    wishme()  # call of wishme function
    while True:
        query = takeCommand().lower()  # here we convert command into lower case

    # Logic for executing the command that given as a query...

        # for searching something in google with search results
        if "open google and search" in query:
            query = query.replace("open google and search", "")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open(
                "https://google.com/search?q=%s" % query)

        # for open only google
        elif "open google" in query:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open("google.com")

        # for searching something in wikipedia and alexa will speak the results
        elif "wikipedia" in query:
            print("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia....")
            speak(results)

        # for open visual studio code
        elif "open code" in query:
            path = "C:\\Users\\Hemant Gupta\\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        # for open word
        elif "open word" in query:
            path2 = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(path2)

        # for open xampp in computer
        elif "open xampp" in query or "open jamp" in query:
            path1 = "C:\\xampp\\xampp-control.exe"
            "C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
            os.startfile(path1)

        # for open youtube in chrome
        elif "open youtube" in query:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open("youtube.com")

        # open stack overflow website
        elif "open stack overflow" in query:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open("stackoverflow.com")

        # for play songs of particular directry
        elif "play music" in query or "play song" in query or "play songs" in query:
            music_dir = "E:\\dhillo\\dhillo\\music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(
                music_dir, songs[random.randint(0, 453)]))

        # for knowing the current time in hour:minute:second formate
        elif "time now" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")

        # for what user say that repeated by alexa
        elif "repeat me" in query:
            query = query.replace("repeat me", "")
            speak(f"you said that {query}")

        # for exiting the program
        elif 'bye bye' in query or 'bye-bye' in query or 'bye' in query:
            speak("Bye bye....")
            exit()
