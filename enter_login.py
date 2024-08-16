import tkinter as tk
import sqlite3
import random as rd

window = tk.Tk()
window.title("enter login")
window.geometry('800x600')
window.configure(bg='#333333')

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
    

frame = tk.Frame(bg='#333333')

login_label = tk.Label(frame, text="Enter Login", bg='#333333', fg='white', font=("Arial", 16))
username_label = tk.Label(frame, text="Username", bg='#333333', fg='white', font=("Arial", 16))
username_entry = tk.Entry(frame, font=("Arial", 16))
password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
password_label = tk.Label(frame, text="Password", bg='#333333', fg='white', font=("Arial", 16))
login_button = tk.Button(frame, text="login", command=login)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()