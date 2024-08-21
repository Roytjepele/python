import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def enter_data():
    accepted = accept_var.get()
    
    if accepted =="Accepted":
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()

            conn = sqlite3.connect('data.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS user_data
            (user_id INT NOT NULL, 
            firstname VARCHAR(255) NOT NULL, 
            lastname VARCHAR(255) NOT NULL, 
            title VARCHAR(255), 
            age INT,
            PRIMARY KEY (user_id)
            FOREIGN KEY (user_id) REFERENCES user_login (user_id)
            )
            
            '''
            conn.execute(table_create_query)
            data_insert_query = '''INSERT INTO user_data (firstname, lastname, title,
            age) VALUES (?, ?, ?, ?)'''
            data_insert_tuple = (firstname, lastname, title, age)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()
        else:
            messagebox.showwarning(title="error", message="First name and last name are required")
    else:
        messagebox.showwarning(title="Error", message="You have not accepted the terms & conditions")

window = tk.Tk()
frame = tk.Frame(window)
frame.configure(bg='#333333')
frame.pack()

user_info_frame = tk.LabelFrame(frame, text="User information",bg="#333333", fg="white")
user_info_frame.configure(bg='#333333')
user_info_frame.grid(column=0, row=0)

first_name_label= tk.Label(user_info_frame, text="first name", bg="#333333", fg="white")
first_name_label.grid(row=0, column=0)
last_name_label = tk.Label(user_info_frame, text="last name", bg="#333333", fg="white")
last_name_label.grid(row=1, column=0)

first_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=0, column=1)
last_name_entry = tk.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

title_label = tk.Label(user_info_frame, text="Title", bg="#333333", fg="white")
title_combobox= ttk.Combobox(user_info_frame, values=["Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=0, column=3)

age_label = tk.Label(user_info_frame, text="Age", bg="#333333", fg="white")
age_spinbox = tk.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=1, column=2)
age_spinbox.grid(row=1, column=3)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

courses_form = tk.LabelFrame(frame)
courses_form.grid(row=1, column=0, sticky="news")

for widget in courses_form.winfo_children():
    widget.grid_configure(padx=10, pady=5)

terms_frame = tk.LabelFrame(frame, text="terms & conditions", fg="white")
terms_frame.configure(bg='#333333')
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)

accept_var = tk.StringVar(value="not accepted")
terms_check = tk.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                             variable=accept_var, onvalue="Accepted", offvalue="Not registered",
                             bg="#333333", fg="white")
terms_check.grid(row=0, column=0)

button = tk.Button(frame, text="Enter data", command=enter_data)
button.grid(row=3, column=0)

window.mainloop()
