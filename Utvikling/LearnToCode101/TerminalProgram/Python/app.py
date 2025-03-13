import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        
        # Task list
        self.tasks = []
        
        # Create GUI elements
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.task_listbox = tk.Listbox(root, width=40, height=15)
        self.task_listbox.pack(pady=10)
        
        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(pady=5)
        
        self.clear_button = tk.Button(root, text="Clear All", command=self.clear_tasks)
        self.clear_button.pack(pady=5)
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")
    
    def complete_task(self):
        try:
            selected = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected)
            self.tasks.pop(selected)
            messagebox.showinfo("Success", "Task completed!")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task!")
    
    def clear_tasks(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
            self.task_listbox.delete(0, tk.END)
            self.tasks.clear()

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()