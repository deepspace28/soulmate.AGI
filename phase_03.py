# Phase 03: Voice Interaction
import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
speaker = pyttsx3.init()

def listen_and_talk():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            speaker.say(f"You said: {text}")
            speaker.runAndWait()
        except sr.UnknownValueError:
            print("Sorry, I didn't get that.")

if __name__ == "__main__":
    listen_and_talk()