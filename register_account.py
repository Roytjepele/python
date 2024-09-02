import tkinter as tk
import sqlite3
from tkinter import *
import random as rd


class enter_login:

    def __init__(self, main_frame):
        self.frame = tk.Frame(main_frame)
        background_mainframe = Label(main_frame)
        background_mainframe.place(x=0, y=0, relwidth=1, relheight=1)
        background_mainframe.configure(background='#6a6a6a')
        frame = tk.Frame(main_frame)
        frame.pack()
        
        login_label = tk.Label(main_frame, text="Create Account", bg='#6a6a6a', fg='black', font=("Arial", 16))
        username_label = tk.Label(main_frame, text="Username", bg='#6a6a6a', fg='black', font=("Arial", 16))
        global username_entry
        global password_entry 
        username_entry = tk.Entry(main_frame, font=("Arial", 16))
        password_entry = tk.Entry(main_frame, show="*", font=("Arial", 16))


        password_label = tk.Label(main_frame, text="Password", bg='#6a6a6a', fg='black', font=("Arial", 16))
        login_button = tk.Button(main_frame, text="Create account", command=enter_login.login)

        login_label.grid(row=0, column=5, columnspan=2, sticky="news", pady=40)
        username_label.grid(row=1, column=5)
        username_entry.grid(row=1, column=6, pady=10)
        password_label.grid(row=2, column=5)
        password_entry.grid(row=2, column=6, pady=10)
        login_button.grid(row=3, column=5, columnspan=2)

        

    
    def login():
            user_id = rd.randint(1,99999999999999)
            username = username_entry.get()
            password = password_entry.get()
            conn = sqlite3.connect('data.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS user_login(
                user_id INT NOT NULL,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                PRIMARY KEY (user_id)
                )
                
                '''
            conn.execute(table_create_query)
            data_insert_query = '''INSERT INTO user_login (user_id, username, password) VALUES (?, ?, ?)'''
            data_insert_tuple = (user_id, username, password)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()