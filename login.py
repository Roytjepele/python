import sqlite3
import tkinter as tk
from tkinter import ttk

def enter_data():
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    title = title_combobox.get()
    age = age_spinbox.get()
    registered = reg_status_var.get()
    # terms = terms_check.get()

    print("first name: ", firstname, "last name:", lastname)
    print("you are ", registered)


window = tk.Tk()
frame = tk.Frame(window)
frame.pack()

# conn = sqlite3.connect('test.db')

# print("opened database successfully")

user_info_frame = tk.LabelFrame(frame, text="User information")
user_info_frame.grid(column=0, row=0)

first_name_label= tk.Label(user_info_frame, text="first name")
first_name_label.grid(row=0, column=0)
last_name_label = tk.Label(user_info_frame, text="last name")
last_name_label.grid(row=1, column=0)

first_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=0, column=1)
last_name_entry = tk.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

title_label = tk.Label(user_info_frame, text="Title")
title_combobox= ttk.Combobox(user_info_frame, values=["Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=0, column=3)

age_label = tk.Label(user_info_frame, text="Age")
age_spinbox = tk.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=1, column=2)
age_spinbox.grid(row=1, column=3)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

courses_form = tk.LabelFrame(frame)
courses_form.grid(row=1, column=0, sticky="news")

registered_label = tk.Label(courses_form, text="registration status")
reg_status_var = tk.StringVar(value="not registered")
registered_check = tk.Checkbutton(courses_form, text="currently registered",
                                   variable=reg_status_var, onvalue="registered" , offvalue="not registered")
registered_label.grid(row=0, column=0)
registered_check.grid(row=0, column=1)

for widget in courses_form.winfo_children():
    widget.grid_configure(padx=10, pady=5)

terms_frame = tk.LabelFrame(frame, text="terms & conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)

terms_check = tk.Checkbutton(terms_frame, text="I accept the terms and conditions.")
terms_check.grid(row=0, column=0)

button = tk.Button(frame, text="Enter data", command=enter_data)
button.grid(row=3, column=0)

window.mainloop()

# conn.close()
# print("closed database successfully")

