from pyttsx3 import init
from datetime import datetime
import speech_recognition as sr


def main():
    engine = init()
    engine.setProperty('rate', 150)
    engine.setProperty("voice", engine.getProperty("voices")[2].id)

    hr = int(datetime.now().hour)
    if hr > -1 and hr < 12:
        engine.say("Good Morning RoMeAh!")
    elif hr > 13 and hr < 18:
        engine.say("Good Afternoon RoMeAh!")
    else:
        engine.say("Good Evening RoMeAh!")
    engine.runAndWait()

    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Shoot! I'm all ears!")
            r.pause_threshold = 2.0
            audio = r.listen(source)

        try:
            recognized = str(r.recognize_google(audio)).lower()
            print(f"You said: {recognized}\n")

            if recognized.startswith("ayup"):
                recognized = recognized.replace("ayup", "")
            else:
                continue
        except Exception as err:
            print(f"Whoops! I encountered a error: {err}")


if __name__ == "__main__":
    main()
