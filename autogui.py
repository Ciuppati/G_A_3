import pyautogui
import time

def ask_days():
    days = int(pyautogui.prompt('Giorni nel mese'))

    return days

def ask_name():
    name = pyautogui.prompt('Nome del lavoratore')
    return name

def scrivi(input):
    pyautogui.write(input)

#giorni = ask_days()
#print(giorni)

def tab():
    pyautogui.press("tab")

def enter():
    pyautogui.press("enter")

def up():
    pyautogui.press("up")

def down():
    pyautogui.press("down")

def left():
    pyautogui.press("left")

def big_left():
    tab()
    for i in range(9):
        pyautogui.press("left")