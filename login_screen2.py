import tkinter as tk
from tkinter import *
import sqlite3

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

def window1():
        frame2.destroy()
        
        other_window()

def other_window():
        Username = username_entry.get()
        # password = password_entry.get()  
        sql = 'SELECT EXISTS (SELECT 1 FROM user_login WHERE username = ?)'
        c.execute(sql, (Username, ))
        if c.fetchone()[0]:
                frame1.destroy()
                frame2.pack()
                username_label = Label(frame2, text=f"Username: {Username} already exists.")
                username_label.pack()
                conn.close()
        else:
                frame1.destroy()
                frame2.pack()
                error_Label = Label(frame2, text=f"Username: {Username} doesn't exist.")
                error_Label.pack()
                error_button = tk.Button(frame2, text="Go back!", command=window1)
                error_button.pack()
        
        
#Saving User information in frame 1
user_info_frame = tk.LabelFrame(frame1, text="User information")
user_info_frame.grid(column=0, row=0)

username_label= tk.Label(user_info_frame, text="username")
username_label.grid(row=0, column=0)
# password_label = tk.Label(user_info_frame, text="password")
# password_label.grid(row=1, column=0)

username_entry = Entry(user_info_frame)
username_entry.grid(row=0, column=1)

# password_entry = tk.Entry(user_info_frame, show="*", font=("Arial", 16))
# password_entry.grid(row=1, column=1)

Button1 = tk.Button(user_info_frame, text="click me!", command=other_window)
Button1.grid(row=2, column=0)


window.mainloop()