from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox as mb

from register_account import enter_login
from data_entry import member_entry
from present_value import Present_value
from datatable import Show_Historical_Data



class App(tk.Tk):
    def __init__(self):
        super().__init__()

        conn = sqlite3.connect("data.db")
        c= conn.cursor()
        c.fetchall()
        conn.commit()

        self.title("Test")
        app_width = 1300
        app_height = 720

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 3) - (app_height / 3)

        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.configure(background='#6a6a6a')
        self.minsize(width=1300, height=720)
        self.maxsize(width=1920, height=1080)


        # setting up the menu on the left side
        menu_frame = tk.Frame(self, bg="#6a6a6a", highlightbackground="#6a6a6a", highlightthickness=1)
        menu_frame.pack(side=tk.LEFT)
        menu_frame.pack_propagate(False)
        menu_frame.configure(width=195, height=1020)

        background_menuframe= Label(menu_frame, background="black")
        background_menuframe.place(x=0, y=0, relwidth=1, relheight=1)

        create_account_btn = tk.Button(menu_frame, text="Create account", font=("Bold", 18), fg="white", bd=0, bg="grey", padx=30, activebackground='#6a6a6a', command=lambda: enter_login(main_frame))
        create_account_btn.place(x=10, y=100)

        page1_indicate = tk.Label(menu_frame, text="", bg="#6a6a6a")
        page1_indicate.place(x=3, y=100, width=5, height=43)

        # setting up the working frame on the right
        main_frame = tk.Frame(self, highlightbackground="#6a6a6a", highlightthickness=1)
        background_mainframe= Label(main_frame, background="#6a6a6a")
        background_mainframe.place(x=0, y=0, relwidth=1, relheight=1)
        main_frame.pack(side=tk.LEFT)
        main_frame.pack_propagate(False)
        main_frame.configure(height=1020, width=1750)

        # check if user is in database
        def check_user_data():
                Username = username_entry.get()
                password = password_entry.get()  
                sql = "SELECT * FROM user_login WHERE username = '%s' AND password = '%s'" % (Username, password)
                data = c.execute(sql)
                if data.fetchone():
                        create_account_btn.destroy()
                        Create_member_info = tk.Button(menu_frame, text="Create member", font=("Bold", 18), fg="white", bd=0, bg="grey", padx=30, activebackground='#6a6a6a', command=lambda: member_entry(main_frame))
                        Create_member_info.place(x=10, y=100)
                        Present_value_btn = tk.Button(menu_frame, text="Calculate Present Value", font=("Bold", 18), fg="white", bd=0, bg="grey", padx=30, activebackground='#6a6a6a', command=lambda: Present_value(main_frame))
                        Present_value_btn.place(x=10, y=150)
                        Present_value_btn = tk.Button(menu_frame, text="Show historical data", font=("Bold", 18), fg="white", bd=0, bg="grey", padx=30, activebackground='#6a6a6a', command=lambda: Show_Historical_Data(main_frame))
                        Present_value_btn.place(x=10, y=200)

                else:
                        mb.showerror(title="Error", message="Your credentials are wrong. Please try again.")
        
        username_label= Label(main_frame, text="username")
        username_label.grid(row=0, column=0)
        password_label = Label(main_frame, text="password")
        password_label.grid(row=1, column=0)

        username_entry = Entry(main_frame)
        username_entry.grid(row=0, column=1)

        password_entry = tk.Entry(main_frame, show="*", font=("Arial", 16))
        password_entry.grid(row=1, column=1)

        Button1 = tk.Button(main_frame, text="click me!", command=check_user_data)
        Button1.grid(row=2, column=0)
        
        


if __name__ == "__main__":
    app = App()
    app.mainloop()