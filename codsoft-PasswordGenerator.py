import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length <= 0:
        messagebox.showwarning("Warning", "Please enter a valid password length.")
        return

    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

root = tk.Tk()
root.title("Password Generator")

frame = tk.Frame(root)
frame.pack(pady=10)

length_label = tk.Label(frame, text="Password Length:")
length_label.pack(side=tk.LEFT, padx=5)

length_entry = tk.Entry(frame, width=5)
length_entry.pack(side=tk.LEFT)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(pady=10)

root.mainloop()
