import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import messagebox as mb
from data_entry import member_entry

class login_screen:

        def __init__(self,main_frame):
                for widget in main_frame.winfo_children():
                        widget.destroy()

                self.frame = tk.Frame(main_frame)
                background_mainframe = Label(main_frame)
                background_mainframe.place(x=0, y=0, relwidth=1, relheight=1)
                background_mainframe.configure(background='#6a6a6a')
                frame = tk.Frame(main_frame)
                frame.pack()

                conn = sqlite3.connect("data.db")
                c= conn.cursor()
                c.fetchall()
                conn.commit()

                # check if user is in database
                def check_user_data():
                        Username = username_entry.get()
                        password = password_entry.get()  
                        sql = "SELECT * FROM user_login WHERE username = '%s' AND password = '%s'" % (Username, password)
                        data = c.execute(sql)
                        if data.fetchone():
                                user_info_frame.destroy()
                                member_entry()
                        else:
                                mb.showerror(title="Error", message="Your credentials are wrong. Please try again.")

                #Saving User information in frame 1
                user_info_frame = LabelFrame(self.frame, text="User information")
                user_info_frame.grid(column=2, row=4)

                username_label= Label(user_info_frame, text="username")
                username_label.grid(row=0, column=0)
                password_label = Label(user_info_frame, text="password")
                password_label.grid(row=1, column=0)

                username_entry = Entry(user_info_frame)
                username_entry.grid(row=0, column=1)

                password_entry = tk.Entry(user_info_frame, show="*", font=("Arial", 16))
                password_entry.grid(row=1, column=1)

                Button1 = tk.Button(user_info_frame, text="click me!", command=check_user_data)
                Button1.grid(row=2, column=0)
