from machine import Pin
from time import sleep

# Initialize the LED on GPIO pin (example: GPIO 2 for onboard LED on ESP32/ESP8266)
led = Pin(2, Pin.OUT)
led.on