import tkinter as tk
from tkinter import font

def on_click(event):
    text=event.widget.cget("text")
    if text=="=":
        try:
            result=eval(entry.get())
            entry.delete(0,tk.END)
            entry.insert(tk.END,str(result))
        except Exception as e:
            entry.delete(0,tk.END)
            entry.insert(tk.END,"Error")
    elif text=="C":
        entry.delete(0,tk.END)
    else:
        entry.insert(tk.END,text)

root = tk.Tk()
root.title("Calculator")
root.configure(bg="#333333")

entry=tk.Entry(root,width=10,font=("Arial",24),bg="#444444",fg="white",borderwidth=0,justify=tk.RIGHT)
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

buttons=[
    ("7","#666666"),("8","#666666"),("9","#666666"),("/","#FF9500"),
    ("4","#666666"),("5","#666666"),("6","#666666"),("*","#FF9500"),
    ("1","#666666"),("2","#666666"),("3","#666666"),("-","#FF9500"),
    ("C","#FF3B30"),("0","#666666"),("=","#4CD964"),("+","#FF9500")
]

for i,(button_text,color) in enumerate(buttons):
    btn=tk.Button(root,text=button_text,width=5,height=2,font=("Arial",12,"bold"),bg=color,fg="white",borderwidth=0)
    btn.grid(row=1+i//4,column=i%4,padx=5,pady=5)
    btn.bind("<Button-1>",on_click)

root.mainloop()
