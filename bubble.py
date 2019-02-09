#Kristina Puzak
#partner: Brett Silverberg

from microbit import *
from math import *
import time

while True:
    time.sleep(0.1)
    xtilt = atan2(accelerometer.get_x(), accelerometer.get_z()) * 180 / pi
    ytilt = atan2(accelerometer.get_y(), accelerometer.get_z()) * 180 / pi
    print(xtilt, ytilt)


    if xtilt > 10:
        if ytilt > 10:
            display.show(Image.ARROW_NW)
        elif ytilt < -10 and ytilt > -170:
            display.show(Image.ARROW_SW)
        else:
            display.show(Image.ARROW_W)
    elif xtilt < -10 and xtilt > -170:
        if ytilt < -10 and ytilt > -170:
            display.show(Image.ARROW_SE)
        elif ytilt > 10:
            display.show(Image.ARROW_NE)
        else:
            display.show(Image.ARROW_E)
    elif ytilt > 10 and ytilt <170:
        display.show(Image.ARROW_N)
    elif ytilt < -10 and ytilt > -170:
        display.show(Image.ARROW_S)
    else:
        display.show(Image.HAPPY)