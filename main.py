from machine import Pin
from time import sleep

# Initialize the LED on GPIO pin (example: GPIO 2 for onboard LED on ESP32/ESP8266)
led = Pin(2, Pin.OUT)

while True:
    led.on()      # Turn LED on
    sleep(1)      # Wait for 1 second
    led.off()     # Turn LED off
    sleep(1)  