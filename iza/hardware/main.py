from iza import Iza

if __name__=='__main__':
    shield = Iza()
    shield.change_state_led('green', True)
    shield.send_message_lcd('¡¡¡¡¡¡Iza!!!!!!')

    while True:
        #shield.move_feet()
        distance_cm = str(shield.read_distance())
        shield.send_message_lcd(distance_cm, 2)