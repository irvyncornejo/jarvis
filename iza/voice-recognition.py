import speech_recognition as sr
from time import sleep

lister = sr.Recognizer()

if __name__=='__main__':
    while True:
        try:
            sleep(1)
            with sr.Microphone() as source:
                voice = lister.listen(source)
                command = lister.recognize_google(voice)
                print(command)
        except Exception as e:
            pass
