import speech_recognition as sr

lister = sr.Recognizer()

try:
    with sr.Microphone() as source:
        voice = lister.listen(source)
        command = lister.recognize_google(voice)
        print(command)
except Exception as e:
    print(e)