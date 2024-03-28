import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self,master):
        self.master=master
        self.master.title("To-Do List App")
        self.tasks=[]
        self.task_var=tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.task_entry=tk.Entry(self.master,textvariable=self.task_var,width=40,font=("Arial",12))
        self.task_entry.grid(row=0,column=0,padx=10,pady=10)
        self.task_entry.bind("<Return>",self.add_task_from_entry)

        self.add_button=tk.Button(self.master,text="Add Task",command=self.add_task,bg="#4CAF50",fg="white",font=("Arial",12))
        self.add_button.grid(row=0,column=1,padx=10,pady=10)

        self.task_listbox=tk.Listbox(self.master,width=50,height=10,font=("Arial",12))
        self.task_listbox.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
        self.task_listbox.bind("<Delete>",self.remove_task)

        self.mark_complete_button=tk.Button(self.master,text="Mark as Complete",command=self.mark_complete,bg="#008CBA",fg="white",font=("Arial",12))
        self.mark_complete_button.grid(row=2,column=0,padx=10,pady=10,sticky="W")

        self.remove_button=tk.Button(self.master,text="Remove Task",command=self.remove_task,bg="#f44336",fg="white",font=("Arial",12))
        self.remove_button.grid(row=2,column=1,padx=10,pady=10,sticky="E")

        self.edit_button=tk.Button(self.master,text="Edit Task",command=self.edit_task,bg="#FFC107",fg="black",font=("Arial",12))
        self.edit_button.grid(row=3,column=0,padx=10,pady=10,sticky="W")

        self.edit_var=tk.StringVar()
        self.edit_entry=tk.Entry(self.master,textvariable=self.edit_var,width=40,font=("Arial",12))
        self.edit_entry.grid(row=3,column=1,padx=10,pady=10)
        self.edit_entry.grid_remove()
        self.edit_entry.bind("<Return>",self.save_edit_task)

    def add_task(self):
        task=self.task_var.get().capitalize()
        if task and task not in self.tasks:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END,task)
            self.task_var.set("")
        elif task in self.tasks:
            messagebox.showinfo("Duplicate Task","Task already exists!")

    def mark_complete(self):
        selected_index=self.task_listbox.curselection()
        if selected_index:
            index=selected_index[0]
            if not self.tasks[index].startswith("✓"):
                self.tasks[index]=f"✓ {self.tasks[index]}"
                self.task_listbox.delete(index)
                self.task_listbox.insert(index,self.tasks[index])

    def remove_task(self,event=None):
        selected_index=self.task_listbox.curselection()
        if selected_index:
            index=selected_index[0]
            confirmation=messagebox.askyesno("Confirmation", "Are you sure you want to remove this task?")
            if confirmation:
                self.task_listbox.delete(index)
                del self.tasks[index]

    def edit_task(self):
        selected_index=self.task_listbox.curselection()
        if selected_index:
            index=selected_index[0]
            self.edit_var.set(self.tasks[index])
            self.task_entry.grid_remove()
            self.add_button.grid_remove()  # Hide the Add Task button
            self.edit_entry.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
            self.edit_entry.focus()

    def save_edit_task(self,event=None):
        edited_task=self.edit_var.get()
        selected_index=self.task_listbox.curselection()
        if selected_index and edited_task and edited_task not in self.tasks:
            index=selected_index[0]
            self.tasks[index]=edited_task
            self.task_listbox.delete(index)
            self.task_listbox.insert(index,edited_task)
            self.edit_var.set("")
            self.edit_entry.grid_remove()
            self.task_entry.grid()
            self.add_button.grid()  
        elif edited_task in self.tasks:
            messagebox.showinfo("Duplicate Task", "Task already exists!")

    def add_task_from_entry(self,event=None):
        self.add_task()
        return "break" 

def main():
    root=tk.Tk()
    app=ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()