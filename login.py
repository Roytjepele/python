import sqlite3
import tkinter as tk

window = tk.Tk()

conn = sqlite3.connect('test.db')

print("opened database successfully")

idlabel = tk.Label(text="Wat is het id-nummer?")
id = tk.Entry(window)
namelabel = tk.Label(text="Wat is je naam?")
name = tk.Entry(window)
agelabel = tk.Label(text="wat is je leeftijd?")
age = tk.Entry(window)
adreslabel = tk.Label(text="wat is je adres?")
adres = tk.Entry(window)
salarylabel = tk.Label(text="wat is je salaris?")
salary = tk.Entry(window)
entrybutton = tk.Button(text="save")

idlabel.grid(row=0, column=0, padx=5, pady=5)
id.grid(row=0, column=1, padx=5, pady=5)
namelabel.grid(row=1, column=0, padx=5, pady=5)
name.grid(row=1, column=1, padx=5, pady=5)
agelabel.grid(row=2, column=0, padx=5, pady=5)
age.grid(row=2, column=1, padx=5, pady=5)
adreslabel.grid(row=3, column=0, padx=5, pady=5)
adres.grid(row=3, column=1, padx=5, pady=5)
salarylabel.grid(row=4, column=0, padx=5, pady=5)
salary.grid(row=4, column=1, padx=5, pady=5)
entrybutton.grid(row=5, column=1, padx=5, pady=5)

window.mainloop()
conn.close()
print("closed database successfully")
