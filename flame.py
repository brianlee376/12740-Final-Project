import RPi.GPIO as GPIO
import time


#port init
def init(DO_pin, AO_pin, SPIMISO, SPICLK, SPICS, SPIMOSI):
    print('Initializing flame sensor...')
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(AO_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(DO_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

    # Set up the SPI interface pins
    GPIO.setup(SPIMOSI, GPIO.OUT)
    GPIO.setup(SPIMISO, GPIO.IN)
    GPIO.setup(SPICLK, GPIO.OUT)
    GPIO.setup(SPICS, GPIO.OUT)
    pass

#read SPI data from MCP3008(or MCP3204) chip,8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    GPIO.output(cspin, True)

    GPIO.output(clockpin, False)  # start clock low
    GPIO.output(cspin, False)     # bring CS low

    commandout = adcnum
    commandout |= 0x18  # start bit + single-ended bit
    commandout <<= 3    # we only need to send 5 bits here
    for i in range(5):
        if (commandout & 0x80):
            GPIO.output(mosipin, True)
        else:
            GPIO.output(mosipin, False)
            commandout <<= 1
            GPIO.output(clockpin, True)
            GPIO.output(clockpin, False)

    adcout = 0
    # read in one empty bit, one null bit and 10 ADC bits
    for i in range(12):
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)
        adcout <<= 1
        if (GPIO.input(misopin)):
            adcout |= 0x1

    GPIO.output(cspin, True)

    adcout >>= 1       # first bit is 'null' so drop it
    return adcout


def main(DO_pin, AO_pin, SPICLK, SPIMISO, SPIMOSI, SPICS):
    flame_value = readadc(AO_pin, SPICLK, SPIMOSI, SPIMISO, SPICS)
    #print(flame_value)
    #print('Flame: ', 1024-flame_value/1024.*3.3)
    #return (1024-flame_value/1024. * 3.3) > 7

    #if GPIO.input(DO_pin) == False:
    #    return False

    #else:
    #    return True
    #print(flame_value)
    #print((1024 - flame_value)/1024.*3.3)
    #return ((1024 - flame_value)/1024.*3.3) > 1
    return GPIO.input(DO_pin)==1

if __name__ =='__main__':
    try:
        main(DO_pin, AO_pin, SPICLK, SPIMISO, SPIMOSI, SPICS)
    except KeyboardInterrupt:
        GPIO.cleanup()
