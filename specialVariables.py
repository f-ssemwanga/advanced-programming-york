import tkinter as tk
from tkinter import ttk

def change(event):
  userOutput ['text'] = entryValue.get()
  

window = tk.Tk()
window.title("Special variables")
''
userInput = tk.Entry(window)
userInput.pack()
userOutput = tk.Label(window)
userOutput.pack()

entryValue = tk.StringVar()
entryValue.set ('A String')

userInput["textvariable"] = entryValue
userInput.bind('<Key-Return>', change)

'4571220168change'
window.mainloop()