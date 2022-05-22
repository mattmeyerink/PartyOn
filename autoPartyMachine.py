import time
import pyautogui
from pynput.mouse import Listener

try: 
    print()
    timeoutInterval = float(input('Enter the interval between movements in minutes (Ex: 5.5): ')) * 60
    print()
except ValueError:
    print()
    print('That wasn\'t a number you dongus. Please cooporate next time')
    print()
    exit()

timeRemaining = timeoutInterval

def resetTimer():
    global timeRemaining
    timeRemaining = timeoutInterval

def on_move(x, y):
    resetTimer()

def on_click(x, y, button, pressed):
    resetTimer()

def on_scroll(x, y, dx, dy):
    resetTimer()

def printIntroMessage():
    print()
    print('Welcome to the auto party machine! We will generate a party any time the energy starts to dip!')
    print()
    print('Control + C to quit.')

def printExitMessage():
    print()
    print('Every party needs to end eventually. Thanks for partying with us!')
    print()

printIntroMessage()

listener = Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
listener.start()

try:
    while True:
        if (timeRemaining <= 0):
            pyautogui.move(200, 200, 1)
            pyautogui.move(-200, -200, 1)
        else:
            timeRemaining -= 1
        time.sleep(1)

except KeyboardInterrupt:
    printExitMessage()
