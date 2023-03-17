import pyautogui
import time

count = 0
while True:
    buttonLocation = pyautogui.locateOnScreen('target.png', confidence=.7)
    if buttonLocation != None:
        pyautogui.click(pyautogui.center(buttonLocation))
        time.sleep(5)
        count += 1
        print("Click times: " + count)
    time.sleep(1)