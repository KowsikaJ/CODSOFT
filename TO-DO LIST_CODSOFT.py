#!/usr/bin/env python
# coding: utf-8

# In[63]:


import tkinter as tk
from tkinter import messagebox,simpledialog

class ToDolist:
    def __init__(self, root):
        self.root=root
        self.root.title("To-Do List")
        self.root.geometry("500x600") 
        
        # Initialize task list
        self.tasks=[]
        self.create_widgets()
        
    def create_widgets(self):
        # Title Label
        self.title_label=tk.Label(self.root,text="To-Do List",font=("Helvetica",18))
        self.title_label.pack(pady=10)
        
        # Task List
        self.task_listbox=tk.Listbox(self.root,selectmode=tk.SINGLE,width=50,height=12,font=("Helvetica",12))
        self.task_listbox.pack(pady=20)
        
        # Entry Box
        self.task_entry=tk.Entry(self.root,width=40,font=("Helvetica",14)) 
        self.task_entry.pack(pady=10)
        
        button_width=20 
        button_font=("Helvetica", 12) 
        
        # Buttons
        self.add_button=tk.Button(self.root,text="Add Task",width=button_width,font=button_font,command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.update_button=tk.Button(self.root,text="Update Task",width=button_width,font=button_font,command=self.update_task)
        self.update_button.pack(pady=5)
        
        self.delete_button=tk.Button(self.root,text="Delete Task",width=button_width,font=button_font,command=self.delete_task)
        self.delete_button.pack(pady=5)
        
        self.complete_button=tk.Button(self.root,text="Mark as Complete",width=button_width,font=button_font,command=self.complete_task)
        self.complete_button.pack(pady=5)
        
    def add_task(self):
        task=self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0,tk.END)
        else:
            messagebox.showwarning("Input Error","Please enter a task.")
        
    def update_task(self):
        selected_task_index=self.task_listbox.curselection()
        if selected_task_index:
            new_task=simpledialog.askstring("Update Task","Enter new task:")
            if new_task:
                self.tasks[selected_task_index[0]]=new_task
                self.update_listbox()
        else:
            messagebox.showwarning("Selection Error","Please select a task to update.")
        
    def delete_task(self):
        selected_task_index=self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_listbox()
        else:
            messagebox.showwarning("Selection Error","Please select a task to delete.")
        
    def complete_task(self):
        selected_task_index=self.task_listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]]=self.tasks[selected_task_index[0]]+" - Completed"
            self.update_listbox()
        else:
            messagebox.showwarning("Selection Error","Please select a task to mark it as complete.")
        
    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__=="__main__":
    root=tk.Tk()
    app=ToDolist(root)
    root.mainloop()

