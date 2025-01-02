import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("To-Do List")
app.geometry("400x400")
#list to store the tasks
tasks = []
#adding a task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)  # Clear the entry field
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")
# removeing a task
def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        del tasks[selected_task_index]  # Remove from the list
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

#completed task
def complete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = tasks[selected_task_index]
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, f"{task} (Completed)")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

#  clearing all tasks
def clear_all():
    task_listbox.delete(0, tk.END)
    tasks.clear()

#create the input field for the task
task_entry = tk.Entry(app, font=("Arial", 14), width=30)
task_entry.pack(pady=10)

# Buttons for task actions
add_button = tk.Button(app, text="Add Task", font=("Arial", 12), command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(app, text="Remove Task", font=("Arial", 12), command=remove_task)
remove_button.pack(pady=5)

complete_button = tk.Button(app, text="Complete Task", font=("Arial", 12), command=complete_task)
complete_button.pack(pady=5)

clear_button = tk.Button(app, text="Clear All Tasks", font=("Arial", 12), command=clear_all)
clear_button.pack(pady=5)

task_listbox = tk.Listbox(app, font=("Arial", 12), width=40, height=10, selectmode=tk.SINGLE)
task_listbox.pack(pady=10)
app.mainloop()
