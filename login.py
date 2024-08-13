import tkinter as tk

window = tk.Tk()
window.title("login")
window.geometry('340x440')
window.configure(bg='#333333')

login_label = tk.Label(window, text="Login", bg='#333333', fg='white')
username_label = tk.Label(window, text="Username", bg='#333333', fg='white')
username_entry = tk.Entry(window)
password_entry = tk.Entry(window, show="*")
password_label = tk.Label(window, text="Password", bg='#333333', fg='white')
login_button = tk.Button(window, text="login")

login_label.grid(row=0, column=0, columnspan=2)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
login_button.grid(row=3, column=0, columnspan=2)

window.mainloop()