from microbit import *

while True:
    with open('data.csv', 'w') as csvfile:
        csvfile.write(temperature(), compass.heading())

        if button_a.is_pressed:
            display.scroll(temperature(), compass.heading())

