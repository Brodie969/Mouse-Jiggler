import random
import pyautogui
import time

pyautogui.FAILSAFE = False

for i in range(1200):
    x = random.randint(1, 1920)
    y = random.randint(1, 1080)
    pyautogui.moveTo(x, y)
    time.sleep(0.1)
