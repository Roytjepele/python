from tkinter import *
import tkinter as tk
import random as rd
from gui.software.register_account import enter_login
import sqlite3



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

        inicio_btn = tk.Button(menu_frame, text="Create account", font=("Bold", 18), fg="white", bd=0, bg="grey", padx=30, activebackground='#6a6a6a', command=lambda: enter_login(main_frame))
        inicio_btn.place(x=10, y=100)

        page1_indicate = tk.Label(menu_frame, text="", bg="#6a6a6a")
        page1_indicate.place(x=3, y=100, width=5, height=43)

        # setting up the working frame on the right

        main_frame = tk.Frame(self, highlightbackground="#6a6a6a", highlightthickness=1)
        background_mainframe= Label(main_frame, background="#6a6a6a")
        background_mainframe.place(x=0, y=0, relwidth=1, relheight=1)
        main_frame.pack(side=tk.LEFT)
        main_frame.pack_propagate(False)
        main_frame.configure(height=1020, width=1750)


if __name__ == "__main__":
    app = App()
    app.mainloop()