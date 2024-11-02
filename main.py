from machine import Pin, ADC
import time

# Define the analog input pin (e.g., GPIO 32)
analog_in = ADC(Pin(32))
analog_in.atten(ADC.ATTN_11DB)  # Set attenuation to read up to 3.3V (or 5V if supported)

# Resistor values in ohms
R1 = 30000.0  # Resistor R1 (30k ohms)
R2 = 7500.0   # Resistor R2 (7.5k ohms)

# Reference voltage (3.3V for ESP32 or adjust accordingly)
ref_voltage = 3.3

# Maximum ADC value for 12-bit resolution (4095)
ADC_MAX_VALUE = 4095

print("DC Voltage Test")

while True:
    # Read the analog input value (0 to 4095 for 12-bit ADC resolution)
    adc_value = analog_in.read()
    
    # Determine voltage at ADC input
    adc_voltage = (adc_value * ref_voltage) / ADC_MAX_VALUE
    
    # Calculate voltage at divider input
    in_voltage = adc_voltage / (R2 / (R1 + R2))
    
    # Print the calculated input voltage to 2 decimal places
    print("Input Voltage = {:.2f} V".format(in_voltage))
    
    # Short delay
    time.sleep(0.5)
