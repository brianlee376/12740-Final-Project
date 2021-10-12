# _____ _____ _____ __ __ _____ _____
#|     |   __|     |  |  |     |     |
#|  |  |__   |  |  |_   _|  |  |  |  |
#|_____|_____|_____| |_| |_____|_____|
#
# Use Raspberry Pi to get temperature/humidity from DHT11 sensor
#
import numpy as np
import time
import dht11
import RPi.GPIO as GPIO
import sys
from collections import Counter

def init(sensor_in):
   print('Initializing temp_humidity sensor...')
   GPIO.setwarnings(False)
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(sensor_in,GPIO.IN)

def main(sensor_in):
    # Main program block

    instance = dht11.DHT11(pin=sensor_in)

    #temperatures = []
    #humidities = []
    result = instance.read()
    temperature = result.temperature
    humidity = result.humidity
    print("Temp: " + str(temperature) +  "  Humidity: " + str(humidity))
    return (temperature > 28) or (humidity > 65)

    #while True:
        #result = instance.read()
        #temperature = result.temperature
        #humidity = result.humidity

        #temperatures.append(temperature)
        #humidities.append(humidity)

        #if len(temperatures) >= 5:
            #count_temps = Counter(temperatures)
            #count_humidities = Counter(humidities)

            #filtered_temp = count_temps.most_common(1)[0][0]
            #filtered_humidity = count_humidities.most_common(1)[0][0]

            #temperatures.pop(0)
            #humidities.pop(0)

        #print('step')

        #time.sleep(2)

if __name__ == '__main__':
    #try:
    main(sensor_in)
    #except KeyboardInterrupt:
    #    print("Keyboard Interrupt")
    #except:
    #    print("Other errors or exceptions occur")
    #finally:
    #    print("GPIO cleanup")
    #    GPIO.cleanup()
    #    sys.exit(0)

