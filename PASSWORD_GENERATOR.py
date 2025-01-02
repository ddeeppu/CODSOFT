import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4 characters.")
            return
 
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        special_characters = string.punctuation

        all_characters = lowercase + uppercase + digits + special_characters
        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(special_characters)
        ]

        password += random.choices(all_characters, k=length - 4)

        random.shuffle(password)

        password_entry.delete(0, tk.END)
        password_entry.insert(0, ''.join(password))

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the password length.")

#create  application interface
app = tk.Tk()
app.title("Password Generator")
app.geometry("400x200")

header_label = tk.Label(app, text="Password Generator", font=("Arial", 16, "bold"))
header_label.pack(pady=10)

#password length as input
length_label = tk.Label(app, text="Enter Password Length:", font=("Arial", 12))
length_label.pack()
length_entry = tk.Entry(app, font=("Arial", 12))
length_entry.pack()

#generate the button
generate_button = tk.Button(app, text="Generate Password", command=generate_password, font=("Arial", 12))
generate_button.pack(pady=10)

#displaying generated password
password_label = tk.Label(app, text="Generated Password:", font=("Arial", 12))
password_label.pack()
password_entry = tk.Entry(app, font=("Arial", 12), width=30)
password_entry.pack()

#call the main to run the application
app.mainloop()
