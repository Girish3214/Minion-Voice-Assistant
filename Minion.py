import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        print("Good morning")
        speak("Good morning")

    elif 12 <= hour < 16:
        print("Good Afternoon")
        speak("Good Afternoon")

    else:
        print("Good Evening")
        speak("Good Evening")

    print("This is Minion ... How may i help u")
    speak("This is Minion ... How may i help u")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ",query)


    except Exception as e:
        print("Please say that again ")
        #speak("Please say that again ")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while (True):
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching in wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open google' in query:
            webbrowser.open('www.google.com')

        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')

        elif 'time' in query:
            tn = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {tn}")
            print(tn)

        #elif 'bye' or 'quit' in query:
          # print("Bye ... catch u later")
        elif 'music' in query:
            music_dir='D:\songs'
            songs=os.listdir(music_dir)
            print("playing song.....")
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'shutdown' in query:
            os.system("shutdown /r /t 1")




