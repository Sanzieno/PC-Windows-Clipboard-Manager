# Clipboard Manager

A local Windows clipboard manager built with Python and Tkinter.

## About

This project is aiming to make it easy to keep track of the text a user copies, creating a log of the clipboard.

## Current Features

- Detects changes to clipboard text via polling twice per second.
- Stores detected clipboard entries in a Python list.
- Returns clipboard contents as text upon clipboard update.

## Planned Features

- Display clipboard history in a graphical user interface with customisation options
- Copy previously saved entries back to the system clipboard.
- Delete and organise clipboard entries.
- Reorder entries using drag and drop.
- Save clipboard history between sessions.

## Technologies

- Python
- Tkinter
- pywin32

## Project Status

Early development. The current implementation is a prototype for testing clipboard detection and storage.
