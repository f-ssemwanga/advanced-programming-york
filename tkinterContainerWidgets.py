from tkinter import *
window = Tk()
window.title = ("Main Frame")
''
window.geometry ("300x100")
''
left =Frame(borderwidth=5)
text = Label(left,text ="Some text in the left frame")
button1 = Button(left, text="Press Me")
left.pack(side='left')
button1.pack()
text.pack()
window.mainloop()

