import machine
import time
LED_PIN=2
led=machine.Pin(2,machine.Pin.OUT)
interval =1000
last_update_time=0
try:
    while(True):
        if(time.ticks_ms()-last_update_time)>interval:
           led.value(not led.value())
           print("LED IS ON" if led.value() else "LED IS OFF")
           last_update_time = time.ticks_ms()
except KeyboardInterrupt:
    print("interrupt by user") 
    
    
           
