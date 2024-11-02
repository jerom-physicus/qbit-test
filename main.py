from machine import Pin, ADC
import time

# Define the analog input pin (use a GPIO pin that supports ADC, e.g., GPIO 32)
adc_pin = ADC(Pin(32))
adc_pin.atten(ADC.ATTN_11DB)  # Set attenuation to measure up to 3.3V (or 5V if supported)

# Constants for ACS712
SENSITIVITY = 185  # mV per amp (use 100 for 20A model, 66 for 30A model)
V_REF = 3.3        # Reference voltage for ADC (3.3V for ESP32)
ADC_MAX_VALUE = 4095  # 12-bit ADC resolution (0-4095 for ESP32)
V_ZERO = V_REF / 2   # Midpoint voltage (assuming no current)

def read_current():
    # Read the raw ADC value
    adc_value = adc_pin.read()
    
    # Convert ADC value to voltage
    voltage = (adc_value / ADC_MAX_VALUE) * V_REF
    
    # Calculate current (voltage above/below V_ZERO indicates current direction)
    current = (voltage - V_ZERO) * 1000 / SENSITIVITY  # Convert mV to A
    
    return current

while True:
    # Read and print the current
    current = read_current()
    print("Current = {:.2f} A".format(current))
    
    # Delay for a short period
    time.sleep(0.5)
