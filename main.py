import pyautogui
import pyperclip
import pandas as pd
import time


pyautogui.hotkey('ctrl','t')
time.sleep(1)
pyperclip.copy('https://drive.google.com/drive/u/0/folders/1WZq1TFohlNwgrfEzn46ucscBovPQfuA-')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')

pyautogui.click(522,534)
pyautogui.click(1661,206)
pyautogui.click(1541,665)


