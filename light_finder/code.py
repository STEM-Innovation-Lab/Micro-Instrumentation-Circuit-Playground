import time
from adafruit_circuitplayground import cp

light_level = cp.light
while True:
    cp.start_tone( light_level*4 )
    time.sleep(0.1)
    light_level = cp.light
    cp.stop_tone()
