#Clipboard Manager - Iterations
#Beta V1 - Setting up the window interactivity, and simplifying workflow

import win32clipboard as pc
import tkinter as tk

currentclip = ""
clipboard_history = []

def read_clipboard():
    """Return clipboard text or None if its unavailable or not text."""
    try:
        pc.OpenClipboard()
        return pc.GetClipboardData(pc.CF_UNICODETEXT)
    except Exception:
        return None
    finally:
        try:
            pc.CloseClipboard()
        except Exception:
            pass

def write_clipboard(text):
    try:
        pc.OpenClipboard()
        pc.EmptyClipboard()
        pc.SetClipboardText(text, pc.CF_UNICODETEXT)
    except Exception:
        pass
    finally:
        try:
            pc.CloseClipboard()
        except Exception:
            pass


def detect_change(): 
    global currentclip
    newclip = read_clipboard()
    if newclip is not None and newclip != currentclip:
        currentclip = newclip
        clipboard_history.append(currentclip)
        #Listbox puts most recent clip at the too

        listbox.insert(0, currentclip.replace("\n", " ")[:100])


    root.after(500, detect_change)

def copy_selected(event):
    global currentclip
    #When the row is selected in the list
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        text = clipboard_history[len(clipboard_history) - 1 - index]
        currentclip = text
        write_clipboard(text)

#Mode 1 includes whats already copied. Mode 2 waits for the next copy after launch
mode = ""
while mode != "1" and mode != "2":
    mode = str(input("Choose mode 1 or mode 2 (Enter 1 or 2): "))

if mode == "2":
    copyclip = read_clipboard()
    currentclip = copyclip if copyclip is not None else ""

root = tk.Tk()
root.title("Clipboard History")
root.geometry("400x500")

listbox = tk.Listbox(root, font = ("Sans serif", 10))
listbox.pack(fill = "both", expand = True, padx = 10, pady = 10)
listbox.bind("<Double-Button-1>", copy_selected)
        

root.after(500,detect_change)
root.mainloop()

#CLIPBOARD TEXT TEST


