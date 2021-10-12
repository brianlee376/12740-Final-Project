import RPi.GPIO as GPIO
import time

#M_pin = 18 #select the pin for motionsensor
#B_pin = 26 #select the pin for buzzer

def init(pir_pin):
   print('Initializing the PIR motion sensor...')
   GPIO.setwarnings(False)
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(pir_pin,GPIO.IN)
   #GPIO.setup(buzzer_pin,GPIO.OUT)
   pass

def buzzer(pir_pin, buzzer_pin):
   while GPIO.input(pir_pin):
      GPIO.output(buzzer_pin,GPIO.LOW)
      time.sleep(0.1)
      GPIO.output(buzzer_pin,GPIO.HIGH)
      time.sleep(0.1)

def main(pir_pin):

   return GPIO.input(pir_pin) == 1
  # while True:
  #    if GPIO.input(pir_pin):
  #       print("Someone is closing!")
  #       buzzer(pir_pin, buzzer_pin)
  #    else:
  #       GPIO.output(buzzer_pin,GPIO.HIGH)
  #       print("Nobody!")
  #    time.sleep(2)

if __name__ =='__main__':
    try:
        main(pir_pin, buzzer_pin)
    except KeyboardInterrupt:
        pass
        GPIO.cleanup()
