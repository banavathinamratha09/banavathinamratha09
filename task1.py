import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Define the function to be called when the submit button is pressed
def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()

    if not name or not email or not age:
        messagebox.showwarning("Input Error", "Please fill out all fields")
        return

    messagebox.showinfo("Registration Successful", f"Name: {name}\nEmail: {email}\nAge: {age}")

# Create and place the labels and entry widgets
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=10)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Age:").grid(row=2, column=0, padx=10, pady=10)
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1, padx=10, pady=10)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, column=0, columnspan=2, pady=20)

# Start the Tkinter event loop
root.mainloop()
