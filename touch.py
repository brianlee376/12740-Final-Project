import RPi.GPIO as GPIO
import time
import os
import sys

#sensor pin define
buzzer = 18
touch = 26

def init(touch_pin):
    print('Initializing the touch sensor...')
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(touch_pin,GPIO.IN) #pull_up_down=GPIO.PUD_UP)

def main(touch_pin):
    if GPIO.input(touch_pin) == False:
        return False

    else:
        return True

if __name__ == '__main__':
    try:
        main(touch)

    except KeyboardInterrupt:
        print("Keyboard Interrupt")

    except:
        print("Other errors or exceptions occur")

    finally:
        print("GPIO cleanup")
        GPIO.cleanup()
        sys.exit(0)
