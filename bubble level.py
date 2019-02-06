import microbit
import math as m
from microbit import *

plus = Image("00000:00900:09990:00900:00000")


while True:
    microbit.sleep(200)
    x1 = microbit.accelerometer.get_x()
    y1 = microbit.accelerometer.get_y()
    z1 = 981 + microbit.accelerometer.get_z()
    x2 = microbit.accelerometer.get_x()
    y2 = microbit.accelerometer.get_y()
    z2 = 981 + microbit.accelerometer.get_z()
    x3 = microbit.accelerometer.get_x()
    y3 = microbit.accelerometer.get_y()
    z3 = 981 + microbit.accelerometer.get_z()
    xa = (x1 + x2 + x3)/3
    ya = (y1 + y2 + y3)/3
    radians1 = m.atan2(ya, xa)
    d1 = (radians1*180)/m.pi
    radians2 = m.atan2(xa, ya)
    d2 = (radians2*180)/m.pi
    print(d1, d2)
    if (d1 < 1 and d1 > -1 and d2 < 1 and d2 > -1) or (d1 == -90 and d2== 180) or (d1 == 90 and d2 == 0) or (d1 == 45 and d2 == 45) or (d1 == 0 and d2 == 90) or ( d1 == 180 and d2 == 180) :
        microbit.display.show(plus)
    elif d1 < -70 and (d2 > 165 or d2 < -160) :
        microbit.display.show(Image.ARROW_N)
    elif d1 < 10 and d1 > -10 and d2 > 60:
        microbit.display.show(Image.ARROW_E)
    elif (d1 > 75 and d1 < 100 and d2 < 20 and d2 > -12) :
        microbit.display.show(Image.ARROW_S)
    elif d1 < -150 and d2 < -70 and d2 > -115 :
        microbit.display.show(Image.ARROW_W)
    elif d1 < -105 and d1 > -155 and d2 < -110 and d2 > -160 :
        microbit.display.show(Image.ARROW_NW)
    elif d1 > -90 and d1 <-10 :
        microbit.display.show(Image.ARROW_NE)
    elif d1 > 90 :
        microbit.display.show(Image.ARROW_SW)
    elif d1 < 70 and d1 > 20 :
        microbit.display.show(Image.ARROW_SE)
    else:
        microbit.display.show(plus)