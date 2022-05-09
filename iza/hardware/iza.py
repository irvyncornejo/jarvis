from time import sleep
from gpiozero import LED
from gpiozero import DistanceSensor
from gpiozero import Buzzer
from gpiozero import Servo
from gpiozero import AngularServo

import I2C_LCD_driver

my_lcd = I2C_LCD_driver.lcd()
leds = {
    'blue': LED(14), 
    'green': LED(15)
}

buzzer = Buzzer(18)
ultrasonico = DistanceSensor(16, 7)#echo, trigger
feet_right = AngularServo(26, min_angle=-90, max_angle=90)
feet_left = AngularServo(25, min_angle=-90, max_angle=90)

class Iza:
    def __init__(self) -> None:
        feet_right.angle = 0
        feet_left.angle = 0
        sleep(1)
    
    def change_state_led(self, color:str, value:bool=False)-> None:
        #TODO add function for pwm control
        led = leds[color]
        led.on() if value else led.off()

    def read_distance(self) -> float:
        try:
            sleep(0.3)
            cm = ultrasonico.distance * 100
            return round(cm, 3)        
        except:
            return 0.0

    def send_message_lcd(self, message:str, row:int=1, time:int=1, clear:bool=False) -> None:
        length_message = len(message)
        if length_message > 16:
            sleep(time)
        else:
            my_lcd.lcd_display_string(f'{message}', row)
            sleep(time)

        my_lcd.lcd_clear() if clear else ''
    
    def move_feet(self) -> None:
        feet_right.angle = 45
        feet_left.angle = 45
        sleep(2)
        feet_right.angle = -45
        feet_left.angle = -45
        sleep(2)

