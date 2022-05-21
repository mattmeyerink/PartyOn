import pyautogui
import time

while True:
    pyautogui.move(200, 0, 1)
    time.sleep(30)
    pyautogui.move(0, -200, 1)
    time.sleep(30)
    pyautogui.move(-200, 1)
    time.sleep(30)
    pyautogui.move(0, 200, 1)
    time.sleep(30)
