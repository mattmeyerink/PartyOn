"""
Move the mouse in a clockwise square continuously in 1 second movements every 30 seconds.
"""

import pyautogui
import time

def keepThePartyRolling():
    printIntroMessage()

    try:
        while True:
            pyautogui.move(200, 0, 1)
            time.sleep(30)
            pyautogui.move(0, 200, 1)
            time.sleep(30)
            pyautogui.move(-200, 0, 1)
            time.sleep(30)
            pyautogui.move(0, -200, 1)
            time.sleep(30)

    except KeyboardInterrupt:
        printExitMessage()

def printIntroMessage():
    print()
    print('Lets keep the party rolling!')
    print()
    print('Control + C to quit.')
    print()

def printExitMessage():
    print()
    print('Stopping now! Take it from here!')
    print()

keepThePartyRolling()
