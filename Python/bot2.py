from ahk import AHK
from ahk.window import Window

ahk = AHK()

#win = ahk.active_window                        # Get the active window
#win = ahk.win_get(title='Untitled - Notepad')  # by title
#win = list(ahk.windows())                      # list of all windows
win = Window(ahk, ahk_id='0x000e05e4')  # 919012   0xabc123')           # by ahk_id
#win = Window.from_mouse_position(ahk)          # the window under the mouse cursor
#win = Window.from_pid(ahk, pid='20366')                 # by process ID
win.send('{F2}')