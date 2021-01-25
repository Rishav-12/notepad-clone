from tkinter import *
from tkinter import filedialog as fd
import os

root = Tk()
root.geometry("900x450")
root.title("Tkinter Notes")

def saveNote():
    saveFileName = fd.asksaveasfilename(filetypes = (("Text files", "*.txt"), ("All files", "*.*")))
    with open(saveFileName, "w") as file:
        file.write(text.get("1.0", "end-1c"))

def openNote():
    openFileName = fd.askopenfilename(filetypes = (("Text files", "*.txt"), ("All files", "*.*")))
    with open(openFileName, "r") as file:
        text.delete("1.0", "end")
        text.insert(END, file.read())

menubar = Menu(root)
menubar.add_command(label = "Save", command = saveNote)
menubar.add_command(label = "Open", command = openNote)

scroll = Scrollbar(root)
scroll.pack(side = RIGHT, fill = Y)

text = Text(root, yscrollcommand = scroll.set)
text.pack(fill = BOTH)
text.configure(font = ("comicsansms", 20))

scroll.config(command = text.yview)

root.config(menu = menubar)
root.mainloop()
