from ahk import AHK
#from ahk.window import Window
import time
import threading

import keyboard
import pygame
from pynput.mouse import Controller


ahk = AHK()

def test():
    mouse = Controller().position

    print()
    while True:
        print(mouse)
        cur = Controller().position
        ahk.click(mouse)
        ahk.click()
        #ahk.mouse_move(cur)
        time.sleep(120)


def pers_work():
    while True:
        print(f"While sleep {115}s ....")
        time.sleep(7)
        keyboard.press_and_release('f1')
        time.sleep(105)
        print(f"stop {115}")

while True:
    print('Начало')
    key = keyboard.read_key()
    if key == "o":

        print("You pressed ")
        t = threading.Thread(target = pers_work, daemon=True)
        t.start()
        t.join(0.1)


    elif key == "p":
        print("You pressed p")
        break

    elif key == "[":
        t = threading.Thread(target=test, daemon=True)
        t.start()
        t.join(0.1)






print("Конец циклa")