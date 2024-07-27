import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    
    if name and email and age:
        messagebox.showinfo("Registration", f"Name: {name}\nEmail: {email}\nAge: {age}")
    else:
        messagebox.showwarning("Input Error", "All fields are required.")

app = tk.Tk()
app.title("Registration Form")

tk.Label(app, text="Name:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(app, text="Email:").grid(row=1, column=0, padx=10, pady=10)
tk.Label(app, text="Age:").grid(row=2, column=0, padx=10, pady=10)

name_entry = tk.Entry(app)
email_entry = tk.Entry(app)
age_entry = tk.Entry(app)

name_entry.grid(row=0, column=1, padx=10, pady=10)
email_entry.grid(row=1, column=1, padx=10, pady=10)
age_entry.grid(row=2, column=1, padx=10, pady=10)

submit_button = tk.Button(app, text="Submit", command=submit_form)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

app.mainloop()
