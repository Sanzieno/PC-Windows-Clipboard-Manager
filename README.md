# Clipboard Manager - BETA V1

The current prototype of this project uses a tkinter listbox that interfaces with the polling of the clipboard. Detects changes to system (Windows) clipboard, stores entries in a history, and allows entries to be recopied onto the clipboard.

## Current Features

- Detects changes to clipboard text via polling twice per second.
- Stores detected clipboard entries in a Python list.
- Displays previous history of clipboard entries in a listbox.
- Copy previously saved entries back to the system clipboard.

## Current Limitations

- Cannot delete clipboard entries.
- Cannot reorganise clipboard entries.
- Cannot edit clipboard entries.
- Clipboard history is not saved between sessions.
- Listbox is a temporary method of displaying saved clipboard entries.

## Next Iteration Plan
The next iteration, BETA V2, will rework some features, addressing some current limitations but also adding new features to the program.

## Planned Improvements

- Persistent storage of clipboard entries; saved between sessions.
- Robust deletion of clipboard entries.
- Editing clipboard entries.
- Change how GUI elements displaying the clipboard entries functions to lay foundations for advanced interactions and a more customisable interface (Subject to continual improvement in further prototype)

## Technologies

- Python
- Tkinter
- pywin32

## Project Status and Goal

Early development. Features still being developed and bugs are likely present. Current goal is to improve sustainability and ease of use. 
