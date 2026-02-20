import time
import machine 

BUTTON_PIN= 0
button = machine.Pin(BUTTON_PIN,machine.Pin.IN,machine.Pin.PULL_UP)
count=0
last_button_time=0
debounce_time