from machine import ADC

from time import sleep_ms



print("Rasberry Pico - température intégrée")


adc = machine.ADC(4)


while True:

    ADC_voltage = adc.read_u16() * (3.3 / (65536))

    temperature_celcius = 27 - (ADC_voltage - 0.706)/0.001721

    temp_fahrenheit=32+(1.8*temperature_celcius)

    print("Temperature: {}°C {}°F".format(temperature_celcius,temp_fahrenheit))

    sleep_ms(1000)