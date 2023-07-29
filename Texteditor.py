from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.title("Text Editor")

root.geometry('200x200')
text= Text(root, width=200, height=200)
text.pack()

root.mainloop()
