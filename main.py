from machine import Pin, ADC
import time

# Define the analog input pin (GPIO 32 for this example)
adc_pin = ADC(Pin(32))
adc_pin.atten(ADC.ATTN_11DB)  # Set attenuation to measure up to 3.3V

# Constants for ACS712 (choose the correct sensitivity for your model)
SENSITIVITY = 185  # mV per amp (use 100 for 20A model, 66 for 30A model)
V_REF = 3.3        # Reference voltage (3.3V for ESP32)
ADC_MAX_VALUE = 4095  # 12-bit ADC resolution

# Calibrate zero point
def calibrate_zero():
    total = 0
    samples = 100  # Number of samples to average for calibration
    for _ in range(samples):
        total += adc_pin.read()
        time.sleep(0.01)  # Small delay between samples
    zero_adc_value = total / samples
    return (zero_adc_value / ADC_MAX_VALUE) * V_REF

# Measure the midpoint voltage when no current is flowing
V_ZERO = calibrate_zero()

def read_current():
    # Read the ADC value
    adc_value = adc_pin.read()
    
    # Convert ADC value to voltage
    voltage = (adc_value / ADC_MAX_VALUE) * V_REF
    
    # Calculate current (accounting for offset)
    current = (voltage - V_ZERO) * 1000 / SENSITIVITY  # Convert mV to A
    
    return current

print("DC Current Measurement")

while True:
    # Read and print the current
    current = read_current()
    print("Current = {:.2f} A".format(current))
    
    # Short delay
    time.sleep(0.5)
