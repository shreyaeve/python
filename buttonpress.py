from machine import Pin
import time

BUTTON_PIN =0
button= Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)
#button press=0, button not pressed=1
count = 0

try:
    while(True):
#        if button.value()==0:
 #           count+=1
  #          print("button press couunt:",count)
        if button.value()==0:
            count+=1
            print("button press couunt:",count)
            #this is also just delay in another form because we are stuck in a loop
                    #isiliye it is better to use the debounce thingy which we are doing with the extra variables 
            while(button.value()==0):
                if button.value()==1:
                    break
                 # time.sleep(0.01)  
            
except KeyboardInterrupt:
    print("interrupt by user")