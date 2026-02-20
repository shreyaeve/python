from machine import Pin
import time
import random

# Pins
BUTTON_PIN = 0
led = Pin(2, Pin.OUT)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

# Timing variables (ms)
LED_BLINK_TIME = 1000
RANDOM_PRINT_TIME = 2000
DEBOUNCE_TIME = 50

# Button state tracking
last_button_state = 1
last_button_time = 0
count = 0

# Timing tracking
last_led_time = 0
last_random_time = 0

try:
    while True:
        current_time = time.ticks_ms()
        
        # Button debouncing (50ms)
        if time.ticks_diff(current_time, last_button_time) > DEBOUNCE_TIME:
            current_button_state = button.value()
            if current_button_state == 0 and last_button_state == 1:
                count += 1
                print("Button press count:", count)
            last_button_state = current_button_state
            last_button_time = current_time
        
        # LED blink (1 second)
        if time.ticks_diff(current_time, last_led_time) > LED_BLINK_TIME:
            led.value(not led.value())
            print("LED ON" if led.value() else "LED OFF")
            last_led_time = current_time
        
        # Random temperature print (2 seconds)
        if time.ticks_diff(current_time, last_random_time) > RANDOM_PRINT_TIME:
            print("temp:", random.randint(35, 55))
            last_random_time = current_time

except KeyboardInterrupt:
    print("Stopped by user")

    
    
           
