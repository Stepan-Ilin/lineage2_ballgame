import wmi


def handles_asterios():
    f = wmi.WMI()

    # Printing the header for the later columns
    #print("pid Process name")
    e = f.Win32_Process()
    # Iterating through all the running processes
    count = 0
    l_process = []
    for process in e:
        if process.Name == 'AsteriosGame.exe':

            l_process.append([process.UserModeTime, process.ProcessId])
            #print(f'{count} index {process.Name} {process.UserModeTime} {process.ProcessId} ')
            #print(l_process)
            count += 1
    handles=[]
    q1 = int(l_process[0][0])
    q2 = int(l_process[1][0])

    if  q1 > q2:
        handles.append(l_process[0][1])
        handles.append(l_process[1][1])
    else:
        handles.append(l_process[1][1])
        handles.append(l_process[0][1])
    return (handles)

print(handles_asterios())


