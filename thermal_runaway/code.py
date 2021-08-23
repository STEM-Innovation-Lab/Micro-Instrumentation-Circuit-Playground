import time
from adafruit_circuitplayground import cp

color = ( 255, 0, 0 )
OFF = ( 0, 0, 0 )


while True:
    temperature_C = cp.temperature
    print( "Temperature C:", temperature_C )
    temperature_offset = - 25
    for index in range ( 0, 10 ):
        if index < temperature_C + temperature_offset:
            cp.pixels[index] = color
        else:
            cp.pixels[index] = OFF
    time.sleep( .1 )
