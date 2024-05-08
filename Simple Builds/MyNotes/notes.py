from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('notes.db')

def populate_list():
    notes_list.delete(0, END)
    for row in db.fetch():
        notes_list.insert(END, row)

def add_item():
    if notes_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(notes_text.get())
    notes_list.delete(0, END)
    notes_list.insert(END, (notes_text.get()))

    clear_text()
    populate_list()

def select_item(event):
    try:
        global selected_item
        index = notes_list.curselection()[0]
        selected_item = notes_list.get(index)
        
        notes_entry.delete(0, END)
        notes_entry.insert(END, selected_item[1])
    except IndexError:
        pass

def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def update_item():
    db.update(selected_item[0], notes_text.get())
    populate_list()

def clear_text():
    notes_entry.delete(0, END)

# # Create window object
app = Tk()

# # Note
notes_text = StringVar()
notes_label = Label(app, text='Note Name', font=('bold', 10), pady=20, padx=20)
notes_label.grid(row=0, column=0, sticky=W)
notes_entry = Entry(app, textvariable=notes_text)
notes_entry.grid(row=0, column=1)

# # Notes List (ListBox)
notes_list = Listbox(app, height=8, width=50, border=0)
notes_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# Scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
# Set scroll to listbox
notes_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=notes_list.yview)
# Bind select
notes_list.bind('<<ListboxSelect>>', select_item)

# # Buttons
add_btn = Button(app, text='Add Note', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove Note', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update Note', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)

app.title('Note Manager')
app.geometry('700x350') # width x height

# # Populate data
populate_list()

# Start program 
app.mainloop()

