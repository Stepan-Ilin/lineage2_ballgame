#from ahk import AHK
#from ahk.window import Window
import time
import threading

import keyboard
#ahk = AHK()
a = 0
def test():
    while True:
        global a
        print(f'a = {a}')
        time.sleep(0.1)
        if a == 1:
            print(f"a = {a} ")
            time.sleep(4)
            a = 0
            break


t = threading.Thread(target= test, daemon=True)
t.start()
t.join(0.1)


def pers_work():
    while True:
        print(f"While sleep {115}s ....")
        time.sleep(7)
        keyboard.press_and_release('f1')
        time.sleep(105)
        print(f"stop {115}")

while True:
    print('gffgsgsoopoppooooooo')
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
        a = 1



print("Конец циклa")