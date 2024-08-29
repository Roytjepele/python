import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import messagebox as mb

import oracledb

window = tk.Tk()
window.title("data entry form")
# window.configure(bg='#333333')

frame1 = tk.Frame(window)
frame1.pack()

frame2 = tk.Frame(window)

conn = sqlite3.connect("data.db")
c= conn.cursor()
c.fetchall()
conn.commit()

def check_user_data():
        Username = username_entry.get()
        password = password_entry.get()  
        sql = "SELECT * FROM user_login WHERE username = '%s' AND password = '%s'" % (Username, password)
        data = c.execute(sql)
        if data.fetchone():
                frame1.destroy()
                frame2.pack()
                username_label = Label(frame2, text=f"Username: {Username} is logged in.")
                username_label.pack()
                conn.close()
        else:
                mb.showerror(title="Error", message=f"Username: {Username} doesn't exist.")
                
        
        
#Saving User information in frame 1
user_info_frame = tk.LabelFrame(frame1, text="User information")
user_info_frame.grid(column=0, row=0)

username_label= tk.Label(user_info_frame, text="username")
username_label.grid(row=0, column=0)
password_label = tk.Label(user_info_frame, text="password")
password_label.grid(row=1, column=0)

username_entry = Entry(user_info_frame)
username_entry.grid(row=0, column=1)

password_entry = tk.Entry(user_info_frame, show="*", font=("Arial", 16))
password_entry.grid(row=1, column=1)

Button1 = tk.Button(user_info_frame, text="click me!", command=check_user_data)
Button1.grid(row=2, column=0)


window.mainloop()