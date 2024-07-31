import sqlite3
from tkinter import *
from tkinter import ttk

window = Tk()
frm = ttk.Frame(window)
frm.grid()
conn = sqlite3.connect('test.db')

print("opened database successfully")

# conn.execute("""CREATE TABLE COMPANY
#              (ID INT PRIMARY KEY NOT NULL,
#              NAME TEXT NOT NULL,
#              AGE INT NOT NULL,
#              ADRESS CHAR(50),
#              SALARY REAL);""")
id = int(input("Wat is het id-nummer?"))
name = input("Wat is je naam?")
age = int(input("wat is je leeftijd?"))
adres = input("wat is je adres?")

window.mainloop()
conn.close()
