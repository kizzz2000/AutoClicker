import time
import pyautogui


def action_set_1(interval):
    time.sleep(1)
    while True:
        pyautogui.click(button="left", clicks=1000000, interval=interval)

def action_set_2():
    pyautogui.hotkey("ctrl", "c")

def action_set_3():
    print("hello")

def action_set_4():
    print("hello")