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

def test1():


    #win = ahk.win_get(title='')  # by title
    #win = list(ahk.windows())
    #print(win)# list of all windows
    #win = Window(ahk, ahk_id='0x00060324')

    print(f'1 {hwnd}')
    #win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x09, 0)
    print(f'2 {hwnd}')
    # win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_END, 0)
    # win32api.SendMessage(hwnd, win32coon.WM_CHAR, ord('x'), 0)

    win32api.PostMessage(hwnd, win32con.WM_SYSKEYDOWN, 0x31, 0xFD)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x70, 0)
    #win = Window.from_pid(ahk, pid=handles_asterios()[0])
    # by ahk_id
    #win = Window(ahk, ahk_id='0x000E05E4')  # 919012

    #win = Window.from_mouse_position(ahk)
    #time.sleep(1)
    #win.send('{F2}')
    print(win)
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x09, 0xFD)
    #time.sleep(1)
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x23, 0)
    time.sleep(2)
    win.send('{F2}')

ahk = AHK()
hwnd = win32gui.FindWindow(None, "Asterios")
#win = Window.from_pid(ahk, pid=handles_asterios()[0])
win = Window(ahk, ahk_id=(str(hex(hwnd))))
while True:

    key = keyboard.read_key()
    if key == "o":
        print("You pressed ")
        t = threading.Thread(target = test1(), daemon=True)
        t.start()
        t.join(0.1)
        

    elif key == "p":
        print("You pressed p")
        break