from time import sleep
import speech_recognition as sr

from hardware.iza import Iza

lister = sr.Recognizer()
iza = Iza()

def main():
    try:
        sleep(0.5)
        with sr.Microphone() as source:
            voice = lister.listen(source)
            command = lister.recognize_google(voice, language='es-MX')
            print(command)
            if command.strip() == 'IC':
                iza.send_message_lcd('Con I de ...', 1, 2)
                iza.send_message_lcd('Inteligencia Artificial!!!!!', 2, 2)
    except Exception as e:
        print(e)

if __name__=='__main__':
    iza.change_state_led('blue', True)
    iza.send_message_lcd('Escuchando!!!!')
    while True:
        iza.send_message_lcd('Di otro comando')
        main()
