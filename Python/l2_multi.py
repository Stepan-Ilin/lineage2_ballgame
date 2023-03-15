#from ahk import AHK
#from ahk.window import Window
import time
import threading
import multiprocessing

import keyboard
#ahk = AHK()

def pers_work():
    print(f"sleep {10}s ....")
    time.sleep(10)
    print(f"stop {10}")
while True:
    print('gffgsgsoopoppooooooo')
    key = keyboard.read_key()
    if key == "o":
        print("You pressed o")

        n_proc = multiprocessing.cpu_count()
        print(n_proc)
        p = multiprocessing.Process(target = pers_work)
        p.start()
        p.join()


    elif key == "p":
        print("You pressed p")

        break


print("Конец циклаo")