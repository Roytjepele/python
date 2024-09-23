import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class Present_value:

    def __init__(self,main_frame):
        for widget in main_frame.winfo_children():
            widget.destroy()

        self.frame = Frame(main_frame)
        background_mainframe = Label(main_frame)
        background_mainframe.place(x=0, y=0, relwidth=1, relheight=1)
        background_mainframe.configure(background='#6a6a6a')
        frame = Frame(main_frame)
        frame.pack()

        global principal_entry
        principal_label = Label(main_frame, text="Principal", bg='#6a6a6a', fg='black', font=("Arial", 16))
        principal_label.grid(row=1, column=1)
        principal_entry = Entry(main_frame, font=("arial", 16))
        principal_entry.grid(row=1, column=2)

        global term_entry
        term_label = Label(main_frame, text="Term", bg='#6a6a6a', fg='black', font=("Arial", 16))
        term_label.grid(row=2, column=1)
        term_entry = Entry(main_frame, font=("arial", 16))
        term_entry.grid(row=2, column=2)

        global interest_entry
        interest_label = Label(main_frame, text="Interest", bg='#6a6a6a', fg='black', font=("Arial", 16))
        interest_label.grid(row=3, column=1)
        interest_entry = Entry(main_frame, font=("arial", 16))
        interest_entry.grid(row=3, column=2)

        calculate_button = Button(main_frame, text="calculate", command=calculate_fv)
        calculate_button.grid(row=4, column=3)


        def calculate_fv():
            Principal = principal_entry.get()
            Interest = interest_entry.get()
            Term = term_entry.get()

            fv_compound_interest = pow((Principal * (1+(Interest/100))), Term)
            return(fv_compound_interest)