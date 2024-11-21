from tkinter import *

window = Tk()
window.title("Hello World!")
window.geometry("400x400")

menubar = Menu(window)
window.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Window")
file_menu.add_command(label="New Window with Profile")

menus: dict = {
    "File": ["New Text File",
             "New File...",
             "New Window",
             "New Window with Profile",
             None,
             "Open File...",
             "Open Folder...",
             "Open Workspace form File...",
             "Open Recent",
             None,
             "Add Folder to Workspace...",
             "Save Workspace As...",
             "Duplicate Workspace",
             None,
             "Save",
             "Save As...",
             "Save All",
             None,
             "Share",
             None,
             "Auto Save",
             "Preferences",
             None,
             "Revert File",
             "Close Editor",
             "Close Folder",
             "Close Window",
             None,
             "Exit"],
    "Edit": ["Undo",
             "Redo",
             None,
             "Cut",
             "Copy",
             "Paste",
             None,
             "Find",
             "Replace",
             None,
             "Find in Files",
             "Replace in Files",
             None,
             "Toggle Line Comment",
             "Toggle Block Comment",
             "Emmet: Expand Abbreviation"]}

def menu_setup(root: object = ..., menus: dict = ...):
    menubar = Menu(root)
    root.config(menu=menubar)
    for key in menus:
        menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label=key, menu=menu)
        for options in menus[key]:
            match options:
                case None:
                    menu.add_separator()
                case _:
                    menu.add_command(label=options)
menu_setup(root=window,menus=menus)
window.mainloop()