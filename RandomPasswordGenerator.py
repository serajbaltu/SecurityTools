import tkinter as tk
import string
import random

def generate_password():
    length = int(password_length.get())
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    password_var.set(password)

root = tk.Tk()
root.title("Random Password Generator")

tk.Label(root, text="Password Length:").pack(pady=5)
password_length = tk.Entry(root)
password_length.pack(pady=5)

password_var = tk.StringVar()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

password_entry = tk.Entry(root, textvariable=password_var, state='readonly', width=50)
password_entry.pack(pady=10)


root.mainloop()
