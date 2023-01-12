# Windows Resize Using TKinter
from tkinter import *

def Function():
 root.geometry(f"{height.get()}x{width.get()}")

#This is the By defult window
root=Tk()
root.title("Resize Your Window ")
root.geometry("400x400")
root.configure(bg="Yellow")


h=Label(text="Height").grid(row=0,column=1)
w=Label(text="Width").grid(row=1,column=1)

height=StringVar()
width=StringVar()
h_value=Entry(root,textvariable=height).grid(row=0,column=2)
w_value=Entry(root,textvariable=width).grid(row=1,column=2)

widget=Button(root,text="Apply",bg="red",command=Function)
widget.grid(row=2,column=6)
root.mainloop()
