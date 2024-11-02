from machine import Pin, ADC
import time

# Configure the ADC pin (e.g., GPIO 36 is ADC1_CH0 on the ESP32)
adc = ADC(Pin(32))
adc.atten(ADC.ATTN_11DB)  # Set attenuation to read up to 3.3V

# Constants for voltage calculation
ADC_MAX_VALUE = 4095       # Max ADC value for 12-bit resolution
ADC_VOLTAGE_REF = 3.3      # Reference voltage for ADC (3.3V for ESP32)

# Voltage divider constants
R1 = 10000                 # Resistor value R1 (e.g., 10k ohms)
R2 = 10000                 # Resistor value R2 (e.g., 10k ohms)

while True:
    # Read raw ADC value (0 to 4095 for 12-bit resolution)
    adc_value = adc.read()
    
    # Calculate the voltage at the ADC pin
    voltage_at_adc = adc_value / ADC_MAX_VALUE * ADC_VOLTAGE_REF
    
    # Calculate the actual voltage based on the voltage divider
    actual_voltage = voltage_at_adc * (R1 + R2) / R2
    
    print("Measured Voltage: {:.2f} V".format(actual_voltage))
    
    time.sleep(1)
