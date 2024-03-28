import tkinter as tk
import random
import string

def generate_password():
    password_length=int(length_entry.get())
    password_characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(password_characters) for i in range(password_length))
    password_var.set(password)
    password_label.config(fg="#333333",bg="#66CD00")

def reset_fields():
    username_entry.delete(0,tk.END)
    length_entry.delete(0,tk.END)
    password_var.set("")
    username_entry.config(fg="#000000",font=("Arial",12),bg="white")
    length_entry.config(fg="#000000",font=("Arial",12),bg="white")
    password_label.config(fg="#333333",bg="#FFFFFF",font=("Arial",16))
    result_label.config(text="",fg="#333333")

def accept_credentials():
    username=username_entry.get()
    password=password_var.get()
    result_label.config(text=f"Username: {username}\nPassword: {password}",font=("Arial",12),fg="#006400")

root=tk.Tk()
root.title("Password Generator")
root.geometry("400x400")

username_label=tk.Label(root,text="Username:",font=("Arial",14),fg="#333333")
username_label.pack()

username_entry=tk.Entry(root,width=30,font=("Arial",12),bd=2,relief=tk.SOLID,bg="lightyellow")
username_entry.pack(pady=5,ipady=5)

length_label=tk.Label(root,text="Password Length:",font=("Arial",14),fg="#333333")
length_label.pack()

length_entry=tk.Entry(root,width=30,font=("Arial",12),bd=2,relief=tk.SOLID,bg="lightyellow")
length_entry.pack(pady=5,ipady=5)

generate_button=tk.Button(root,text="Generate Password",font=("Arial",12),command=generate_password,bg="#FFD700",fg="#333333")
generate_button.pack(pady=5)

password_var=tk.StringVar()
password_label=tk.Label(root,textvariable=password_var,font=("Arial",16),wraplength=300,padx=10,pady=10,fg="#333333",bg="#FFFFFF")
password_label.pack()

reset_button=tk.Button(root,text="Reset",font=("Arial",12),command=reset_fields,bg="#FFD700",fg="#333333")
reset_button.pack(pady=5)

accept_button=tk.Button(root,text="Accept",font=("Arial",12),command=accept_credentials,bg="#FFD700",fg="#333333")
accept_button.pack(pady=5)

result_label=tk.Label(root,text="",font=("Arial",12),wraplength=300,padx=10,pady=10)
result_label.pack()

root.mainloop()
