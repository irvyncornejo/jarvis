from time import sleep
from typing import List
from gpiozero import LED
from gpiozero import DistanceSensor
from gpiozero import Buzzer
from gpiozero import AngularServo

from .I2C_LCD_driver import lcd

class Iza:
    def __init__(
        self,
        buzzer_pin:int=18,
        ultrasonic_echo:int=16,
        ultrasonic_trigger:int=7,
        led_blue:int=14,
        led_green:int=15,
        servo_feet_right:int=26,
        servo_feet_left:int=25,
        servo_leg_right:int=13,
        servo_leg_left:int=12
    ) -> None:
        self._my_lcd = lcd()
        self._buzzer = Buzzer(buzzer_pin)
        self._ultrasonico = DistanceSensor(ultrasonic_echo, ultrasonic_trigger)#echo, trigger
        self._feet_right = AngularServo(servo_feet_right, min_angle=-90, max_angle=90)
        self._feet_left = AngularServo(servo_feet_left, min_angle=-90, max_angle=90)
        self._leg_right = AngularServo(servo_leg_right, min_angle=-90, max_angle=90)
        self._leg_left = AngularServo(servo_leg_left, min_angle=-90, max_angle=90)
        self._servo_pins = [servo_feet_right, servo_feet_left, servo_leg_right, servo_leg_left]
        self._leds = {'blue': LED(led_blue), 'green': LED(led_green)}
        self._list_servos:List[AngularServo] = [
            self._feet_right,
            self._feet_left,
            self._leg_right,
            self._leg_left
        ]
        self._set_init_servos()
        

    def __slice_message(self, message:str)->list:
        lenght=len(message)
        messages=[]
        init=0
        final=15 
        messages.append(message[init:final])
        messages.append(message[final:final+1+(lenght%16)])
        return messages

    def _read_analog_channel(self, channel:int)->None:
        pass

    def change_state_led(self, color:str, value:bool=False)-> None:
        #TODO add function for pwm control
        led = self._leds[color]
        led.on() if value else led.off()

    def read_distance(self) -> float:
        try:
            sleep(0.3)
            cm = self._ultrasonico.distance * 100
            return round(cm, 3)        
        except:
            return 0.0

    def send_message_lcd(self, message:str, row:int=1, time:int=1, clear:bool=False) -> None:
        length_message = len(message)
        self._my_lcd.lcd_clear()
        if length_message > 16:
            messages = self.__slice_message(message)
            for message in messages:
                self._my_lcd.lcd_display_string(message, row)
                sleep(time)
                self._my_lcd.lcd_clear()
        
        else:
            self._my_lcd.lcd_display_string(f'{message}', row)
            sleep(time)

        self._my_lcd.lcd_clear() if clear else ''

    def _set_init_servos(self)->None:
        for servo in self._list_servos:
            sleep(0.2)
            servo.angle = 0
        self._close_servos()
    
    def _close_servos(self)->None:
        for servo in self._list_servos:
            servo.close()
    
    def _start_servos(self)->None:
        for i, servo in enumerate(self._list_servos):
            servo.__init__(
                self._servo_pins[i],
                min_angle=-90,
                max_angle=90
            )

    def dance(self, routine:int):
        self._start_servos()
        if routine == 1:
            angles = [(-60, 60), (60, -60)]
            for _ in range(7):
                self._leg_left.angle= angles[0][0]
                self._leg_right.angle = angles[0][1]
                sleep(1)

        self._set_init_servos()

    def show_temperature(self)->None:
        pass
