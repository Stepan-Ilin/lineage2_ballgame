import threading
import time
import keyboard
from ahk import AHK
from ahk.window import Window
import wmi
import win32con
import win32gui
import win32api



def handles_asterios():
    f = wmi.WMI()

    # Printing the header for the later columns
    # print("pid Process name")
    e = f.Win32_Process()
    # Iterating through all the running processes
    count = 0
    l_process = []
    for process in e:
        if process.Name == 'AsteriosGame.exe':
            l_process.append([process.UserModeTime, process.ProcessId])
            # print(f'{count} index {process.Name} {process.UserModeTime} {process.ProcessId} ')
            # print(l_process)
            count += 1

    handles = []

    if count == 1:
        handles.append(l_process[0][1])

    if count == 2:
        q1 = int(l_process[0][0])
        q2 = int(l_process[1][0])
        if q1 > q2:
            handles.append(l_process[0][1])
            handles.append(l_process[1][1])
        else:
            handles.append(l_process[1][1])
            handles.append(l_process[0][1])

    return (handles)

def pers_work():
    counter = 0

    while True:
        print(f"While sleep {115}s ....")

       # keyboard.press_and_release('f2')
        #keyboard.press_and_release('f2')
        print(counter)
        time.sleep(5)
        if len(pid_wins) == 1:
            print(win1.send('{f2}'), 'dgd')
            win2.send('{F2}', press_duration=2)
            print(win1.id,'1111')
            win1.send('{f2}')

            if counter == 0:
                print(f'qqqq{counter}')
                time.sleep(3)
                win2.send('{F4}')

        time.sleep(5)

        if len(pid_wins) == 2:
            time.sleep(5)

            win1.send('{f5}')
            print(win1)
            time.sleep(10)
            win2.send('{f2}')
            time.sleep(10)
            win2.send('{F4}')

            if counter == 0:
                print(f'qqqq{counter}')
                time.sleep(7)
                win2.send('{F4}')


        time.sleep(105)
        print(f"stop {115}")
        counter += 1

        if counter == 7:
            counter = 0

#def main():
ahk = AHK()
e = time.time()
pid_wins = handles_asterios()
if len(pid_wins) == 2:                                                                             
    global win1, win2
    win1 = Window(ahk, ahk_id=Window.from_pid(ahk, pid=pid_wins[0]).id)
    win2 = Window(ahk, ahk_id=Window.from_pid(ahk, pid=pid_wins[1]).id)

    print(len(pid_wins))
    print(win1.id)

elif len(pid_wins) == 1:

    win1 = Window(ahk, ahk_id=Window.from_pid(ahk, pid=pid_wins[0]).id)
    print(win1.id)
    print(len(pid_wins)) 
we = time.time()

print(f'Узнали {we-e} ')
print(pid_wins)

#hwnd = win32gui.FindWindow(None, "Asterios")    593446
# win = Window(ahk, ahk_id=(str(hex(hwnd))))
#if 'a_variable' in locals(): return True

while True:

    key = keyboard.read_key()
    if key == "o":
        print("You pressed o")

        t = threading.Thread(target = pers_work(), daemon=True)
        t.start()
        t.join(0.1)


    elif key == "p":
        print("You pressed p")
        break
