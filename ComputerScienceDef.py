import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
# create the dictionary to extract terms
def jsonReader():
  '''Reads in Json files'''
  try:
    with open("computer_defs.json", 'r') as file:
      computer_defs = json.load(file)
      return computer_defs
  except FileNotFoundError:
    computer_defs ={}
    return computer_defs

  
def get_def():
  computer_defs = jsonReader()
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
window.geometry("760x600")

#text to output to the user
instruction = "Enter a term you would like to know the definition of : "
#adding a logo
logo = tk.PhotoImage(file="computerlogo.png")
logo = logo.subsample(4)
tk.Label(window, image=logo, bg='black').grid(row=0, column =0,columnspan=2,sticky='EW')

#adding instruction for the user
tk.Label(window,text=instruction, bg='black', fg='white', font = 'none 16 bold').grid(row =1, column =0, columnspan=2, sticky='w', padx=(100,80), pady=(0,10))

# create a text entry box
term_entry = tk.Entry(window, width=20, bg='white')
term_entry.grid(row=2, column=0, sticky='ew', padx=(100,30),pady=(0,10))
term_font =("Helvetica", 14)
term_entry.config(font=term_font) 
# add a button
ttk.Button(window, text='GET', width=20, command=get_def).grid(row=2, column=1, sticky='w', pady=(0,10))

# label for output
tk.Label(window, text='\nDefinition:', bg='black', fg='white', font='none 12 bold').grid(row=4,column=0, sticky='W')

# output for the definition (large text box)
output = tk.Text(window, width=75, height=3, wrap='word', background='white')
output.grid(row=4, column=0, columnspan=2, sticky='e', padx=(100,80), pady=(0,10))


#Saving a definition to the dictionary
def saveWords():
  '''takes entered words and saves them as a jason'''
  #read values from entry fields
  term = add_term_entry.get("1.0", "end-1c")
  defin = defin_entry.get("1.0", "end-1c")
  
  #check if both term and definition are non empty
  if term and defin:
    #load existing JSON data from the file if it exists
    computer_defs = jsonReader()
    #add the new term and definition to the dictionary
    computer_defs[term] = defin
    #write the updated data back to the JSON file
    with open ("computer_defs.json", 'w') as file:
      json.dump(computer_defs, file, indent=4)
    #clear entry fields after successful addition of data
    defin_entry.delete(0.0, tk.END)
    add_term_entry.delete(0.0, tk.END)
  else:
    #display error message if either term or defin is empty
    tk.messagebox.showerror("Error", "Both definition and Term must be present")
def handleClear():
  defin_entry.delete(0.0, tk.END)
  add_term_entry.delete(0.0, tk.END)
  
tk.Label(window,text="Add a new term to the dictionary", bg='black', fg='white', font = 'none 16 bold').grid(row =5, column =0, columnspan=2, sticky='w', padx=(100,80), pady=(0,10))
tk.Label(window, text='\nTerm to add:', bg='black', fg='white', font='none 12 bold').grid(row=6,column=0, sticky='W')
add_term_entry = tk.Text(window, width=40, height=2, wrap='word', background='white')
add_term_entry.grid(row=6, column=0, columnspan=2, sticky='e', padx=(10,230), pady=(0,10))
add_term_entry.config(font=term_font)

tk.Label(window, text='\nDefinition:', bg='black', fg='white', font='none 12 bold').grid(row=7,column=0, sticky='W')
defin_entry = tk.Text(window, width=40, height=2, wrap='word', background='white')
defin_entry.grid(row=7, column=0, columnspan=2, sticky='e', padx=(10,230), pady=(0,10))
defin_entry.config(font=term_font)
# add a button
ttk.Button(window, text='Clear', width=10, command=handleClear).grid(row=8, column=1,columnspan=2, sticky='w', pady=(0,10), padx=(0,350))
ttk.Button(window, text='Add', width=10, command=saveWords).grid(row=8, column=1,columnspan=2, sticky='e', pady=(0,10), padx=(10,230))
window.mainloop()
