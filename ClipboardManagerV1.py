#Clipboard Manager - Test Window
#Test 1 - Polling logic

import win32clipboard as pc
import tkinter as tk

root = tk.Tk()
currentclip = ""
clipboard_history = []

def detect_change(): 
    global currentclip
    #Check current contents
    try:
        pc.OpenClipboard()
        newclip = pc.GetClipboardData(pc.CF_UNICODETEXT)
        
    #Case clipboard inaccessible
    except Exception:
        newclip = currentclip
    finally:
        try:
            pc.CloseClipboard()
        except Exception:
            pass
    #Replace new clip
    if currentclip != newclip:
        currentclip = newclip
        print(currentclip)
        clipboard_history.append(currentclip)

    root.after(500, detect_change)

#Practice setting for storing current clip or waiting until it changes, mode 2 may not work all the time due to other program interference
mode = ""
while mode != "1" and mode != "2":
    mode = str(input("Choose mode 1 or mode 2 (Enter 1 or 2): "))

if mode == "2":
    try:
        pc.OpenClipboard()
        currentclip = pc.GetClipboardData(pc.CF_UNICODETEXT)
        pc.CloseClipboard()
    except Exception:
        pass
        

root.after(500,detect_change)
root.mainloop()

#CLIPBOARD TEXT TEST


