import temp_humidity
import touch
import flame
import smoke
import photo
import pir
import co
import RPi.GPIO as GPIO
import sys
import time

def init_outs(outs, outnames):
    for out, name in zip(outs, outnames):
        print('Initializing ' + name + '...')
        GPIO.setup(out, GPIO.OUT)

if __name__ == '__main__':
    
    ### Ins
    # Temp in
    temp_pin = 14

    # Touch in
    touch_pin = 6

    # Photoresistor in
    photo_SPICLK = 11
    photo_SPIMISO = 9
    photo_SPIMOSI = 10
    photo_SPICS = 8
    photo_in = 0

    # PIR in
    pir_in = 23

    # Smoke in
    smoke_SPIMOSI = 10
    smoke_SPIMISO = 9
    smoke_SPICLK = 11
    smoke_SPICS = 8
    smoke_mq2_apin = 1

    # CO in
    co_SPIMOSI = 10
    co_SPIMISO = 9
    co_SPICS = 8
    co_SPICLK = 11
    co_mq7_apin = 2

    # Flame in
    flame_AO_pin = 3
    flame_SPICLK = 11
    flame_SPIMISO = 9
    flame_SPIMOSI = 10
    flame_SPICS = 8
    flame_DO_pin = 26
    
    ### Outs
    buzzer_pin = 16
    living_room_relay = 20
    kitchen_relay = 19
    led_blue_pin = 21
    led_yellow_pin = 4
    led_red_pin = 17
    led_green_pin = 27
    led_kitchen = 18

    try:
        # Initialize the sensors
        print('INPUTS:')
        touch.init(touch_pin)
        flame.init(flame_DO_pin, flame_AO_pin, flame_SPIMISO, flame_SPICLK, flame_SPICS, flame_SPIMOSI)
        photo.init(photo_SPICLK, photo_SPIMISO, photo_SPIMOSI, photo_SPICS, photo_in)
        pir.init(pir_in)
        temp_humidity.init(temp_pin)
        smoke.init(smoke_SPIMOSI, smoke_SPIMISO, smoke_SPICLK, smoke_SPICS)
        co.init(co_SPIMOSI, co_SPIMISO, co_SPICS, co_SPICLK)

        # Initialize outputs
        outs = [buzzer_pin, kitchen_relay, living_room_relay, led_blue_pin, led_yellow_pin, led_red_pin, led_green_pin, led_kitchen]
        outnames = ['buzzer', 'kitchen relay', 'living room relay', 'LED-blue', 'LED-yellow', 'LED-red', 'LED-green', 'LED-kitchen']

        print('\nOUTPUTS:')
        init_outs(outs, outnames)
        
        # Keep track of ticks
        i = 0
        
        # These variables keep the fan running for a period after a succesful hit
        temp_check = False
        temp_intervals = 0
        
        # Check if the flame sensor should be outputting
        flame_check = False
        flame_interval = 0
        
        # Make sure the buzzer doesn't get turned off unintentionally
        is_buzzing = False

        # Keep lights on in living room
        lights_on = False

        # Initialize output levels
        GPIO.output(buzzer_pin, GPIO.HIGH)
        GPIO.output(kitchen_relay, GPIO.HIGH)
        GPIO.output(living_room_relay, GPIO.HIGH)

        while True:
            print('\nCheck', (i%21)*'.')
            
            # Smoke and CO sensor
            smoke_sensor = smoke.main(smoke_SPIMOSI, smoke_SPIMISO, smoke_SPICLK, smoke_SPICS, smoke_mq2_apin)
            co_sensor = co.main(co_mq7_apin, co_SPICLK, co_SPIMOSI, co_SPIMISO, co_SPICS)
            
            if smoke_sensor or co_sensor or is_buzzing:
                is_buzzing = True
                GPIO.output(kitchen_relay, GPIO.LOW)
                GPIO.output(buzzer_pin, GPIO.LOW)
            else:
                GPIO.output(kitchen_relay, GPIO.HIGH)
                GPIO.output(buzzer_pin, GPIO.HIGH)
            
            # PIR and Photo Sensor
            pir_sensor = pir.main(pir_in)
            leds = [led_blue_pin, led_red_pin, led_yellow_pin, led_green_pin]
            if pir_sensor or lights_on:
                photo_sensor = photo.main(photo_SPICLK, photo_SPIMISO, photo_SPIMOSI, photo_SPICS, photo_in)
                print('Photo: ', photo_sensor)
                if photo_sensor or lights_on:
                    lights_on = True
                    for led in leds:
                        GPIO.output(led, GPIO.HIGH)
            else:
                for led in leds:
                    GPIO.output(led, GPIO.LOW)
            
            # Touch Sensor
            touch_sensor = touch.main(touch_pin) 
            if touch_sensor or is_buzzing:
                is_buzzing = True
                GPIO.output(buzzer_pin, GPIO.LOW)
            elif not is_buzzing:
                GPIO.output(buzzer_pin, GPIO.HIGH)
             
            # Flame Sensor
            if i%20 == 0 or flame_check:
                if not flame_check:
                    flame_sensor = flame.main(flame_DO_pin, flame_AO_pin, flame_SPICLK, flame_SPIMISO, flame_SPIMOSI, flame_SPICS)
                if flame_sensor or flame_check:
                    if flame_check == False:
                        flame_check = True
                    else:
                        flame_interval += 1
                    is_buzzing = True
                    if (flame_interval%5 == 0):
                        GPIO.output(buzzer_pin, GPIO.LOW)
                        GPIO.output(led_kitchen, GPIO.HIGH)
                        for led in leds:
                            GPIO.output(led, GPIO.HIGH)
                if flame_interval > 30:
                    flame_check = False
                    flame_interval = 0
                    GPIO.output(buzzer_pin, GPIO.HIGH)
                    GPIO.output(led_kitchen, GPIO.LOW)
                    for led in leds:
                        GPIO.output(led, GPIO.LOW)
            
            if not touch_sensor and not smoke_sensor and not co_sensor and not flame_check:
                is_buzzing = False
            
            # Temp-humidity Sensor
            if i%50 == 0 or temp_check:
                if i%50 == 0:
                    temp_humidity_sensor = temp_humidity.main(temp_pin)
                    print('Temp: ', temp_humidity_sensor)
                else:
                    temp_humidity_sensor = False

                if temp_humidity_sensor:
                    temp_check = True
                    temp_intervals = 0
                
                if temp_check:
                    GPIO.output(living_room_relay, GPIO.LOW)
                    temp_intervals += 1

                if temp_intervals > 100:
                    temp_intervals = 0
                    temp_check = False
                    GPIO.output(living_room_relay, GPIO.HIGH)

            print('Touch: ', touch_sensor)
            print('PIR: ', pir_sensor)
            print('CO: ', co_sensor)
            print('Smoke: ', smoke_sensor)
            print('Flame: ', flame_sensor)
            time.sleep(0.1)
            i += 1

    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        GPIO.cleanup()
    finally:    
        GPIO.cleanup()
