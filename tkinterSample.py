import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
window = tk.Tk()
agreement =tk.StringVar()

window.title("Main Window")
window.geometry("200x50")
heading = tk.Label(window, text="Welcome to this app")
heading.pack()
btnSample = tk.Button(window, text ='Press me')
btnSample.pack()
def agreementChanged():
  tk.messagebox.showinfo(title="Result", 
                         message = agreement.get())
chkTest = ttk.Checkbutton(window,
                          text="I agree",
                          command=agreementChanged,
                          variable=agreement,
                          onvalue='Agree',
                          offvalue='Disagree')

chkTest.pack()
chkTest.pack()
window.mainloop()