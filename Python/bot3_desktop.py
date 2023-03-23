import threading
import time
import keyboard
from ahk import AHK
from ahk.window import Window
import wmi
import win32con
import win32gui
import ctypes
import win32api

# Решение опубликованно в https://qna.habr.com/q/79336 участником  Perforator @Perforator
def PostKeyEx(hwnd, key, shift, specialkey):
    PBYTE256 = ctypes.c_ubyte * 256
    _user32 = ctypes.WinDLL("user32")
    GetKeyboardState = _user32.GetKeyboardState
    SetKeyboardState = _user32.SetKeyboardState
    PostMessage = win32api.PostMessage
    SendMessage = win32gui.SendMessage
    FindWindow = win32gui.FindWindow
    IsWindow = win32gui.IsWindow
    GetCurrentThreadId = win32api.GetCurrentThreadId
    GetWindowThreadProcessId = _user32.GetWindowThreadProcessId  # очень важно брать функцию из dll, т.к. питоновский враппер (win32process.GetWindowThreadProcessId) выдаёт неправильные значения
    AttachThreadInput = _user32.AttachThreadInput

    MapVirtualKeyA = _user32.MapVirtualKeyA
    MapVirtualKeyW = _user32.MapVirtualKeyW

    MakeLong = win32api.MAKELONG
    #w = win32con  # так короче запись

    if IsWindow(hwnd):

        ThreadId = GetWindowThreadProcessId(hwnd, None)

        lparam = MakeLong(0, MapVirtualKeyA(key, 0))
        msg_down = win32con.WM_KEYDOWN
        msg_up = win32con.WM_KEYUP

        if specialkey:
            lparam = lparam | 0x1000000

        if len(shift) > 0:  # Если есть модификаторы - используем PostMessage и AttachThreadInput
            pKeyBuffers = PBYTE256()
            pKeyBuffers_old = PBYTE256()

            SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
            AttachThreadInput(GetCurrentThreadId(), ThreadId, True)
            GetKeyboardState(ctypes.byref(pKeyBuffers_old))

            for modkey in shift:
                if modkey == win32con.VK_MENU:
                    lparam = lparam | 0x20000000
                    msg_down = win32con.WM_SYSKEYDOWN
                    msg_up = win32con.WM_SYSKEYUP
                pKeyBuffers[modkey] |= 128

            SetKeyboardState(ctypes.byref(pKeyBuffers))
            time.sleep(0.01)
            PostMessage(hwnd, msg_down, key, lparam)
            time.sleep(0.01)
            PostMessage(hwnd, msg_up, key, lparam | 0xC0000000)
            time.sleep(0.01)
            SetKeyboardState(ctypes.byref(pKeyBuffers_old))
            time.sleep(0.01)
            AttachThreadInput(GetCurrentThreadId(), ThreadId, False)

        else:  # Если нету модификаторов - используем SendMessage
            SendMessage(hwnd, msg_down, key, lparam)
            SendMessage(hwnd, msg_up, key, lparam | 0xC0000000)


#hwnd = 0x00730B48
#hwnd1 = 0x001F0336
#hwnd1 = 0x00160872



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
    if count > 2:
        (print('Error: pid 3 lineage'))
        return None


    return (handles)

def pers_work():
    counter = 0

    while True:
        counter += 1
        print(f"While sleep {115}s ....")

       # keyboard.press_and_release('f2')
        #keyboard.press_and_release('f2')
        print(counter)
        time.sleep(1)
        if len(pid_wins) == 1:


            if counter == 0:
                print(f'qqqq{counter}')
                time.sleep(3)




        if len(pid_wins) == 2:
            time.sleep(0)
            PostKeyEx(hwnd1, ord('1'), [win32con.VK_MENU], False)
            time.sleep(8)
            PostKeyEx(hwnd2, ord('1'), [win32con.VK_MENU], False)
            time.sleep(5)
            if counter == 1:
                PostKeyEx(hwnd2, ord('2'), [win32con.VK_MENU], False)


        time.sleep(103)
        print(f"stop {115}")


        if counter == 10:
            counter = 0

def vark_baf():
    counter = 0
    while True:
        counter += 1
        print(f"While sleep {285}s ....")

        # keyboard.press_and_release('f2')
        # keyboard.press_and_release('f2')
        print(counter)

        if len(pid_wins) == 1:

            if counter == 0:
                print(f'qqqq{counter}')
                time.sleep(3)

        if len(pid_wins) == 2:

            PostKeyEx(hwnd2, ord('1'), [win32con.VK_MENU], False)

            #if counter == 1:
                #PostKeyEx(hwnd2, ord('2'), [win32con.VK_MENU], False)

        time.sleep(285)
        print(f"stop {285}")

        if counter == 10:
            counter = 0


#def main():
ahk = AHK()
e = time.time()
pid_wins = handles_asterios()


if len(pid_wins) == 2:
    #global hwnd1, hwnd2

    s=int(Window.from_pid(ahk, pid=pid_wins[0]).id, 16)
    hwnd1 = int(Window.from_pid(ahk, pid=pid_wins[0]).id, 16)
    hwnd2 = int(Window.from_pid(ahk, pid=pid_wins[1]).id, 16)
    #win2 = Window(ahk, ahk_id=Window.from_pid(ahk, pid=pid_wins[1]).id)

    print(len(pid_wins))
    print(hwnd1)

elif len(pid_wins) == 1:

    hwnd1 = hex(int(Window.from_pid(ahk, pid=pid_wins[0]).id, 16))
    print(hwnd1.id)
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

        t = threading.Thread(target = vark_baf(), daemon=True)
        t.start()
        t.join(0.1)


    elif key == "p":
        print("You pressed p")
        break