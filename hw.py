from gpiozero import LightSensor, LED as Relay, MCP3008
from time import sleep

iluminacion = LightSensor(25)
relay_1 = Relay(4)
relay_2 = Relay(5)

def convert_temp(temperatura_1):
    for value in temperatura_1:
        yield (value * 3.3) * 100

def ventilador():
    relay_1.on()


temperatura_1 = MCP3008(channel=0)
temperatura_2 = MCP3008(channel=1)


while True:
    """
    iluminacion.wait_for_light()
    iluminacion.when_dark = relay_1.off()
    print("It's light! :)")
    iluminacion.wait_for_dark()
    print("It's dark :(")
    iluminacion.when_dark = relay_1.on()
    """
    for temp in convert_temp(temperatura_1.values):
    	print('The temperature is', temp, 'C')
    	sleep(1)
