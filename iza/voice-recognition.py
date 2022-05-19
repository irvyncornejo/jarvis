from time import sleep
import speech_recognition as sr

from hardware.iza import Iza

lister = sr.Recognizer()
iza = Iza()

def main():
    try:
        sleep(1)
        with sr.Microphone() as source:
            voice = lister.listen(source)
            command = lister.recognize_google(voice)
            print(command)
    except Exception as e:
        pass

if __name__=='__main__':
    iza.change_state_led('green', True)
    iza.send_message_lcd('¡¡¡¡¡¡Iza!!!!!!')
    while True:
        main()
