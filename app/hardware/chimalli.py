from time import sleep
from gpiozero import LED
from gpiozero import DistanceSensor
from gpiozero import Buzzer
from gpiozero import Servo
from gpiozero import AngularServo

import I2C_LCD_driver

my_lcd = I2C_LCD_driver.lcd()
leds = {
    'blue': LED(15), 
    'green': LED(14)
}
buzzer = Buzzer(18)
ultrasonico = DistanceSensor(16, 7)#echo, trigger

class Chimalli:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def clear_lcd():
        my_lcd.lcd_clear()

    def change_state_led(self, color:str, value:bool=False)-> None:
        #TODO add function for pwm control
        led = leds[color]
        led.on() if value else led.off()

    def read_distance(self) -> float:
        sleep(1)
        cm = ultrasonico.distance * 100
        return cm

    def send_message_lcd(self, message:str, time:int=1,row:int=0) -> None:
        length_message = len(message)
        if length_message > 16:
            pass
        else:
            my_lcd.lcd_display_string(f'{message}', row)
            sleep(time)
            self.clear_lcd()


if __name__=='__main__':
    shield = Chimalli()
    shield.change_state_led('green', True)
    shield.send_message_lcd('Hola!!!!!')
    while True:
        distance_cm = shield.read_distance()
        print(distance_cm)
        
