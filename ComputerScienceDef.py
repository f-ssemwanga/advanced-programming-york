import tkinter as tk
from tkinter import ttk
# create the dictionary to extract terms
computer_defs = {'CPU':'Central Processing Unit', 'RAM':'Random Access Memory'}

def get_def():
  term = term_entry.get()
  #print("Term entered:", term)
  #clear the text box from previous entries
  output.delete(0.0, tk.END)
  if term in  computer_defs:
    definition = computer_defs[term]
  else:
    definition = "sorry that term is not in the dictionary" 
  #print("Definition:", definition)  
  output.insert(tk.END, definition)
window = tk.Tk()
window.title("Computer Science Definitions")
window.configure(background='black')

#text to output to the user
instruction = "Enter a term you would like to know the definition of : "
#adding a logo
logo = tk.PhotoImage(file="computerlogo.png")
logo = logo.subsample(4)
tk.Label(window, image=logo, bg='black').grid(row=0, column =0,sticky='EW')

#adding instruction for the user
tk.Label(window,text=instruction, bg='black', fg='white', font = 'none 12 bold').grid(row =1, column =0, sticky='Ew')

# create a text entry box
term_entry = tk.Entry(window, width=20, bg='white')
term_entry.grid(row=2, column=0)

# add a button
ttk.Button(window, text='GET', width=6, command=get_def).grid(row=3, column=0)

# label for output
tk.Label(window, text='\nDefinition:', bg='black', fg='white', font='none 12 bold').grid(row=4,column=0, sticky='EW')

# output for the definition (large text box)
output = tk.Text(window, width=75, height=6, wrap='word', background='white')
output.grid(row=5, column=0, columnspan=2)



window.mainloop()
