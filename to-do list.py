import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def add_task():
    task = entry_task.get()
    due_date = entry_due_date.get()
    if task and due_date and due_date != "DD-MM-YYYY":
        current_date = datetime.now().strftime("%d-%m-%Y")
        full_task = f"{current_date} | {task} (Due: {due_date})"
        listbox_tasks.insert(tk.END, full_task)
        entry_task.delete(0, tk.END)
        entry_due_date.delete(0, tk.END)
        entry_due_date.insert(0, "DD-MM-YYYY")
        entry_due_date.config(fg='grey')
    else:
        messagebox.showwarning("Warning", "You must enter both a task and a due date.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def clear_tasks():
    listbox_tasks.delete(0, tk.END)

def complete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        task = f"[Completed] {task}"
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(selected_task_index, task)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as complete.")

def on_entry_click(event):
    if entry_due_date.get() == "DD-MM-YYYY":
        entry_due_date.delete(0, "end")
        entry_due_date.config(fg='black')

def on_focusout(event):
    if entry_due_date.get() == "":
        entry_due_date.insert(0, "DD-MM-YYYY")
        entry_due_date.config(fg='grey')

# Set up the main window
window = tk.Tk()
window.title("To-Do List")
window.geometry('600x400')

# Create a frame to contain the widgets
frame = tk.Frame(window)
frame.pack(pady=10)

# Create a listbox to display the tasks
listbox_tasks = tk.Listbox(frame, width=70, height=10, font=('Calibri', 14))
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

# Add a scrollbar to the listbox
scrollbar_tasks = tk.Scrollbar(frame)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Create an entry widget to accept user input for tasks
entry_task = tk.Entry(window, width=50, font=('Calibri', 14))
entry_task.pack(pady=5)

# Create an entry widget to accept due date for tasks
entry_due_date = tk.Entry(window, width=50, font=('Calibri', 14), fg='grey')
entry_due_date.insert(0, "DD-MM-YYYY")
entry_due_date.bind('<FocusIn>', on_entry_click)
entry_due_date.bind('<FocusOut>', on_focusout)
entry_due_date.pack(pady=5)

# Create a frame to contain the buttons
frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=10)

# Create buttons for adding, deleting, clearing, and completing tasks
button_add_task = tk.Button(frame_buttons, text="Add Task", width=15, font=('Calibri', 14), command=add_task)
button_add_task.grid(row=0, column=0, padx=5)

button_delete_task = tk.Button(frame_buttons, text="Delete Task", width=15, font=('Calibri', 14), command=delete_task)
button_delete_task.grid(row=0, column=1, padx=5)

button_clear_tasks = tk.Button(frame_buttons, text="Clear All Tasks", width=15, font=('Calibri', 14), command=clear_tasks)
button_clear_tasks.grid(row=0, column=2, padx=5)

button_complete_task = tk.Button(frame_buttons, text="Complete Task", width=15, font=('Calibri', 14), command=complete_task)
button_complete_task.grid(row=0, column=3, padx=5)

# Start the main event loop
window.mainloop()
