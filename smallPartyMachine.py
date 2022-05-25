"""
Asks the user to input a float to serve as a timeout interval.
Moves the mouse one pixel diagonally back and fourth once per the timeout interval.
"""

import time
import pyautogui

try: 
    print()
    timeoutInterval = float(input('Enter the interval between movements in minutes (Ex: 5.5): ')) * 60
    print()
except ValueError:
    print()
    print('That wasn\'t a number you dongus. Please cooporate next time')
    print()
    exit()

print()
print('The party is officially on!')
print()
print('Command + C to quit')
print()

try: 
    while True:
        pyautogui.move(1, 1)
        pyautogui.move(-1, -1)
        time.sleep(timeoutInterval)
except KeyboardInterrupt:
    print()
    print('Small party coming to a close. Over and out. Have nice day!')
    print()
