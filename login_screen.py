import tkinter as tk
import sqlite3

window = tk.Tk()
window.title("enter login")
window.geometry('800x600')
window.configure(bg='#333333')

def login():
    username = username_entry.get()
    password = password_entry.get()
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    checkUsername = cursor.execute('SELECT username FROM user_login WHERE username=(?)', (username))
    checkPassword = cursor.execute('SELECT username FROM user_login WHERE password=(?)', (password))
    cursor.execute(checkUsername)
    cursor.execute(checkPassword)
    print(checkUsername)
    conn.commit()
    conn.close()
    

frame = tk.Frame(bg='#333333')

login_label = tk.Label(frame, text="Login", bg='#333333', fg='white', font=("Arial", 16))
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