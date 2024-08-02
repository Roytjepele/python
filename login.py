import sqlite3
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

conn = sqlite3.connect('test.db')

print("opened database successfully")

idlabel = tk.Label(text="What is the id-nummer?")
id = tk.Entry(window)
namelabel = tk.Label(text="What is your name?")
name = tk.Entry(window)
agelabel = tk.Label(text="What is your age?")
age = tk.Entry(window)
adresslabel = tk.Label(text="What is your adress?")
adress = tk.Entry(window)
salarylabel = tk.Label(text="What is your salary?")
salary = tk.Entry(window)

def message():
    messagebox.showinfo("title", f"id number is {id.get()}, name is {name.get()}, age is {age.get()}, adress is {adress.get()}, salary is {salary.get()}")

entrybutton = tk.Button(text="save", command=message)

idlabel.grid(row=0, column=0, padx=5, pady=5)
id.grid(row=0, column=1, padx=5, pady=5)
namelabel.grid(row=1, column=0, padx=5, pady=5)
name.grid(row=1, column=1, padx=5, pady=5)
agelabel.grid(row=2, column=0, padx=5, pady=5)
age.grid(row=2, column=1, padx=5, pady=5)
adresslabel.grid(row=3, column=0, padx=5, pady=5)
adress.grid(row=3, column=1, padx=5, pady=5)
salarylabel.grid(row=4, column=0, padx=5, pady=5)
salary.grid(row=4, column=1, padx=5, pady=5)
entrybutton.grid(row=5, column=1, padx=5, pady=5)



window.mainloop()
conn.close()
print("closed database successfully")
