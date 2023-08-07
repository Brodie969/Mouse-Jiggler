import random
import pyautogui
import time
import tkinter as tk

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
pyautogui.FAILSAFE = False

for i in range(1200):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    pyautogui.moveTo(x, y)
    time.sleep(0.1)
