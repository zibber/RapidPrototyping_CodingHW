# Write your code here :-)
from microbit import *
import random
# roll instruction
display.scroll("Welcome to even or odd")
display.scroll("press a and b to start")  # welcome to odd and even
# press A to generate a ramdom number from 1-999,
# press button A as odd, press press button B as even, then press A to restart
# select difficulty(easy more time, hard less time)
# press A to show a ramdom number

while True:
    random_number = random.randint(0, 99)
    stage = 0
    # generate a ramdom number
    if button_a.is_pressed() and button_b.is_pressed():
        # timer begin
        # display the random number
        display.scroll(random_number)
        display.scroll("even press a and odd press b")
# knowing if odd or even (%),if odd number = 1, even number = 2
        while random_number % 2 == 0 and stage == 0:
            if button_a.is_pressed():
                display.show("V")
                stage = 1
            elif button_b.is_pressed():
                display.show("X")
                stage = 1
        while random_number % 2 == 1 and stage == 0:
            if button_a.is_pressed():
                display.show("X")
                stage = 1
            elif button_b.is_pressed():
                display.show("V")
                stage = 1


# buton_a = 1, buton_b = 2
# if number = button_ show check mark else show cross mark
# press button_a to restart(new odd or even)