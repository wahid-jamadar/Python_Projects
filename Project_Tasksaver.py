import tkinter as tk
from tkinter import messagebox
import os

# Define the file name for storing tasks
FILE_NAME = "tasks.txt"

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a selected task from the list
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to load tasks from the file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                tasks_listbox.insert(tk.END, task.strip())

# Function to save tasks to the file
def save_tasks():
    tasks = tasks_listbox.get(0, tk.END)
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Info", "Tasks saved successfully!")

# Create the main window
root = tk.Tk()
root.title("To-Do List Application")

# Create a frame for task entry
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

# Create a text entry widget for entering tasks
task_entry = tk.Entry(entry_frame, width=50)
task_entry.pack(side=tk.LEFT, padx=5)

# Create a button to add tasks
add_button = tk.Button(entry_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

# Create a listbox to display tasks
tasks_listbox = tk.Listbox(root, width=60, height=15)
tasks_listbox.pack(pady=10)

# Create buttons to save and delete tasks
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

save_button = tk.Button(button_frame, text="Save Tasks", command=save_tasks)
save_button.pack(side=tk.LEFT, padx=5)

# Load tasks from the file when the application starts
load_tasks()

# Start the Tkinter event loop
root.mainloop()