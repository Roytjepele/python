import tkinter as tk

window = tk.Tk()
window.title("login")

frame = tk.Frame(window)
frame.pack()

user_info_frame = tk.LabelFrame(frame, text="Login")
user_info_frame.grid(column=0, row=0)

login_label= tk.Label(user_info_frame, text="name")
login_label.grid(row=0, column=0)
password_label = tk.Label(user_info_frame, text="password")
password_label.grid(row=1, column=0)

login_entry = tk.Entry(user_info_frame)
login_entry.grid(row=0, column=1)
password_entry = tk.Entry(user_info_frame)
password_entry.grid(row=1, column=1)

window.mainloop()