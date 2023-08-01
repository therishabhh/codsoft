import tkinter as tk

def on_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, button_text)

def clear_entry():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for button_text, row, col in buttons:
    tk.Button(root, text=button_text, width=5, height=2, font=("Arial", 15),
              command=lambda text=button_text: on_click(text)).grid(row=row, column=col, padx=5, pady=5)

tk.Button(root, text="C", width=10, height=2, font=("Arial", 15), bg="red", fg="white",
          command=clear_entry).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
