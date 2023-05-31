from time import sleep
from typing import Union


import speech_recognition as sr

from hardware.iza import Iza

lister = sr.Recognizer()

class Actions(Iza):
    def __init__(self)->None:
        super().__init__()

    def __process_command(self, command:str):
        _separe_command = command.split(' ')
        if _separe_command[0] == 'isa':
            self.change_state_led('green', True)
            sleep(2)
        self.change_state_led('green', False)
        actions.change_state_led('blue', True)

    def run(self, command:str):
        if command:
            print(command)
            self.__process_command(command.lower())
    

def main()->Union[str, None]:
    try:
        sleep(0.25)
        with sr.Microphone() as source:
            voice = lister.listen(source)
            return lister.recognize_google(voice, language='es-MX')
            
    except Exception as e:
        print(e)
        return None



if __name__=='__main__':
    actions = Actions()

    actions.change_state_led('blue', True)
    actions.send_message_lcd('Escuchando!!!!')

    while True:
        command = main()
        if command or command != '':
            actions.run(command)
        actions.send_message_lcd('Escuchando!!!!')
