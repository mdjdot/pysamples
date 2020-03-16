#!/usr/bin/env python3
import tkinter
import tkinter.messagebox
import tkinter.font

"""
pyinstaller pytkinter.py -F -i app.ico -w
pack single executable file with icon and without console window
"""

appTitle = "tkinter app 1.0"


def startApp():
    app = tkinter.Tk()
    app.title(appTitle)
    app.geometry("400x400")
    label = tkinter.Label(
        app,
        text="a label control",
        foreground="blue",
        font=tkinter.font.Font(
            slant=tkinter.font.ITALIC,
            size=32
        )
    )
    label.pack(expand=1)
    panel = tkinter.Frame(app, class_="app.frame")

    button = tkinter.Button(
        panel, text="Quit", command=lambda: confirm_to_quit(app),)
    button.pack(side="left")
    panel.pack(side="bottom")
    app.mainloop()


def confirm_to_quit(app):
    if tkinter.messagebox.askokcancel(appTitle, "Quit or not?"):
        app.quit()


if __name__ == "__main__":
    startApp()
