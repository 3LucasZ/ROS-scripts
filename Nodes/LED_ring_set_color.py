import time
from rpi_ws281x import *
# import argparse
 
# LEDring configuration:
LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 19      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 1       # set to '1' for GPIOs 13, 19, 41, 45 or 53
 
# Define functions which animate LEDs in various ways.
def setColor(LEDring, color):
    for i in range(LEDring.numPixels()):
        LEDring.setPixelColor(i, color)
    LEDring.show()
# Main program logic follows:
if __name__ == '__main__':
    
    # Create NeoPixel object with appropriate configuration.
    LEDring = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    LEDring.begin()
 
    setColor(LEDring, Color(255, 255, 255))  # Red wipe
 

