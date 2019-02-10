# YOUR NAME: Nicolas Ragusa
# NUMBER OF HOURS TO COMPLETE: 4.5 hours
# YOUR COLLABORATION STATEMENT(s): I worked with David Fricke and Patrick Wright.

import microbit
import math as m
from microbit import *

plus = Image("00000:00900:09990:00900:00000")

while True:
    microbit.sleep(200)
    x1 = microbit.accelerometer.get_x()
    y1 = microbit.accelerometer.get_y()
    z1 = microbit.accelerometer.get_z()
    x2 = microbit.accelerometer.get_x()
    y2 = microbit.accelerometer.get_y()
    z2 = microbit.accelerometer.get_z()
    x3 = microbit.accelerometer.get_x()
    y3 = microbit.accelerometer.get_y()
    z3 = microbit.accelerometer.get_z()
    xa = (x1 + x2 + x3)/3
    ya = (y1 + y2 + y3)/3
    za = (z1 + z2 + z3)/3
    radians1 = m.atan2(ya, za)
    d1 = (radians1*180)/m.pi
    radians2 = m.atan2(xa, za)
    d2 = (radians2*180)/m.pi
    print(d1, d2)
    if (abs(d1) + abs(d2)) > 350:
        microbit.display.show(plus)
    elif d1 < -120 and (d2 > 170 or d2 < -175) :
        microbit.display.show(Image.ARROW_N)
    elif d1 < -130 and d2 < -100 :
        microbit.display.show(Image.ARROW_NW)
    elif (d1 > 170 or d1 < -170) and d2 < -110:
        microbit.display.show(Image.ARROW_W)
    elif d1 > 135 and d2 < -100:
        microbit.display.show(Image.ARROW_SW)
    elif d1 > 100 and d2 > 160:
        microbit.display.show(Image.ARROW_S)
    elif d1 > 150 and d2 > 120:
        microbit.display.show(Image.ARROW_SE)
    elif d1 < -160 and d2 > 120:
        microbit.display.show(Image.ARROW_E)
    elif d1 < -120 and d2 > 100:
        microbit.display.show(Image.ARROW_NE)
    else:
        microbit.display.show(Image.CONFUSED)