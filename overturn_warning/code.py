from adafruit_circuitplayground.express import cp
import time

cpx.pixels.brightness = 0.8

while True:
    x, y, z = cpx.acceleration
    print((x, y, z))
    time.sleep(0.1)
    if z < -2:
        cpx.pixels.fill((255,0,0))
        cpx.play_tone(1500, 0.25)
    else:
        cpx.pixels.fill((0,0,50))
