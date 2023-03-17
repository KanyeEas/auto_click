import pyautogui
import time

while True:
    buttonLocation = pyautogui.locateOnScreen('target.png', confidence=.7)
    if buttonLocation != None:
        pyautogui.click(pyautogui.center(buttonLocation))
        time.sleep(5)
    time.sleep(1)