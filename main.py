# Icon by Freepik from www.flaticon.com
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox

root = Tk()
root.geometry("900x450")
root.title("Tkinter Notes")
icon = PhotoImage(file = 'notes.png')
root.iconphoto(True, icon)

def newNote():
	text.delete(1.0, END)

def saveNote():
	f = fd.asksaveasfilename(filetypes = (("Text files", "*.txt"), ("All files", "*.*")))
	with open(f, "w") as file:
		file.write(text.get(1.0, "end-1c"))

def openNote():
	f = fd.askopenfilename(filetypes = (("Text files", "*.txt"), ("All files", "*.*")))
	text.delete(1.0, END)
	with open(f, "r") as file:
		text.insert(1.0, file.read())

def cut():
	text.event_generate(("<<Cut>>"))

def copy():
	text.event_generate(("<<Copy>>"))

def paste():
	text.event_generate(("<<Paste>>"))

def aboutApp():
	messagebox.showinfo("About", "Notepad Clone by Rishav Mitra using Tkinter")

menubar = Menu(root)
# File menu Starts
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "New", command = newNote)
filemenu.add_command(label = "Save", command = saveNote)
filemenu.add_command(label = "Open", command = openNote)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = root.destroy)
menubar.add_cascade(label = "File", menu = filemenu)
# File menu Ends

# Edit menu Starts
editmenu = Menu(menubar, tearoff = 0)
editmenu.add_command(label = "Cut", command = cut)
editmenu.add_command(label = "Copy", command = copy)
editmenu.add_command(label = "Paste", command = paste)
menubar.add_cascade(label = "Edit", menu = editmenu)
# Edit menu Ends

# Help menu Starts
helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "About", command = aboutApp)
menubar.add_cascade(label = "Help", menu = helpmenu)
# Help menu Ends

scroll = Scrollbar(root)
scroll.pack(side = RIGHT, fill = Y)

text = Text(root, yscrollcommand = scroll.set)
text.pack(fill = BOTH)
text.configure(font = ("Comic Sans MS", 20))

scroll.config(command = text.yview)

root.config(menu = menubar)
root.mainloop()
