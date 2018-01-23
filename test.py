import tkinter
import sys

import STATE as STATE

root = tkinter.Tk()
root.geometry("200x200")
root.title("His Button Increaser")

counter = tkinter.IntVar()

def onClick(event=None):
    counter.set(counter.get() + 1)

def offClick(event=None):
    counter.set(counter.get() - 1)
    # if counter == 0:

a = tkinter.Label(root, textvariable=counter).pack()
b = tkinter.Button(root, text="decrease", command=offClick, fg="dark red", bg = "white").pack()
c = tkinter.Button(root, text="Increase", command=onClick, fg="dark green", bg = "white").pack()

root.mainloop()