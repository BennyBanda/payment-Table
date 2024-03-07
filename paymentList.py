from tkinter import ttk
import tkinter as tk
from tkinter import *
from random import choice #It allows us to get values in a list

# Main Window
win = Tk()
win.title("Payment list")
win.geometry("550x390+400+200")

# Data
firstName = ["Albert", "Luka", "Philip", "Joseph", "Jackson", "Josephat"]
lastName = ["Mubanga", "Siwale", "Chola", "Malunga", "Sichangwa", " .N. Zulu"]

# Treeview
table = ttk.Treeview(win, columns = ("first", "last", "email"), show="headings")
table.heading("first", text = "First Name")
table.heading("last", text = "Last Name")
table.heading("email", text = "Email")
table.pack(fill="both", expand=True)

# How to insert values in a list
for i in range(40):
    first = choice(firstName)
    last = choice(lastName)
    email = f'{first}{last}@gmail.com'
    data = (first, last, email)
    table.insert(parent = "", index=0, values=data)

# How to print out values of the table
def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)["values"])

table.bind("<<TreeviewSelection>>", item_select) #Bind function

# Run Fuction
win.mainloop()