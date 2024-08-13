'''m=int(input("Enter rows for  ma:"))
n=int(input("Enter columns for ma:"))
p=int(input("Enter rows for  mb:"))
q=int(input("Enter columns for mb:"))
if m!=p and n!=q:
    print("addition is not possible")
else:
    a=[]
    b=[]
    c=[]
    print("enter values for ma:")
    for i in range(m):
        row=[]
        for j in range(n):
            x=int(input(f"Entry in row: {i+1} column: {j+1}\n"))
            row.append(x)
        a.append(row)
    print("enter vallues for matrix-B")
    for i in range(p):
        row=[]
        for j in range(q):
            x=int(input(f"Entry in row: {i+1} column: {j+1}\n"))
            row.append(x)
        b.append(row)
    for i in range(len(a)):
        matrix=[]
        for j in range(len(b[0])):
            matrix.append(0)
        c.append(matrix)
    for i in range(len(a)):
        matrix=[]
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j]+=a[i][k]*b[k][j]
    print(c)
    for i in range(m):
        row=[]
        for j in range(n):
            row.append(a[i][j]+b[i][j])
        c.append(row)
    print(a)
    print(b)
    print(c)
import turtle
turtle.setup(800,600)
window=turtle.Screen()
tr=turtle.getturtle()
tr.hideturtle()
tr.setposition(100,0)
tr.setposition(100,100)
tr.setposition(0,100)
tr.setposition(0,0)
turtle.exitonclick()
import turtle
turtle.setup(800,600)
window=turtle.Screen()
tr=turtle.getturtle()
tr.hideturtle()
tr.forward(100)
tr.left(120)
tr.forward(100)
tr.left(120)
tr.forward(100)
turtle.exitonclick()
import turtle
turtle.setup(800,600)
window=turtle.Screen()
t=turtle.getturtle()
t.hideturtle()
t.resizemode('user')
t.turtlesize(3,3)
turtle.colormode(255)
t.pensize(5)
t.pencolor(238,130,238)
t.penup()
t.goto(-150, 0)
t.left(60)
t.forward(100)
t.pendown()
t.right(120)
t.forward(100)
t.left(120)
t.forward(100)
t.right(120)
t.forward(100)
t.left(120)
t.forward(100)
turtle.exitonclick()
from tkinter import Toplevel,Button,Tk,Menu
top=Tk()
menubar=Menu(top)
file=Menu(menubar,tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as..")
file.add_command(label="another")
file.add_command(label="Close")
file.add_separator()
file.add_command(label="Exit",command=top.quit)
menubar.add_cascade(label="File",menu=file)
edit=Menu(menubar,tearoff=0)
edit.add_command(label="Undo")
edit.add_separator()
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="paste")
edit.add_command(label="Delete")
edit.add_command(label="Select all")
menubar.add_cascade(label='Edit',menu=edit)
help_menu=Menu(menubar,tearoff=0)
help_menu.add_command(label="About")
menubar.add_cascade(label="Help",menu=help_menu)
top.config(menu=menubar)
top.mainloop()
import tkinter as tk
def cl():
    l=lee.get()
    la=tk.Label(root,text=l)
    la.pack()
root=tk.Tk()
root.title("Text Label creator")
le=tk.Label(root,text="Enter the text:")
le.pack()
lee=tk.Entry(root)
lee.pack()
cb=tk.Button(root,text="Create Label",command=cl)
cb.pack()
root.mainloop()
import tkinter as tk
def cl():
    l=lee.get()
    la=tk.Label(root,text=l)
    la.pack()
root=tk.Tk()
root.title("Text label creator")
le=tk.Label(root,text="enter text:")
le.pack()
lee=tk.Entry(root)
lee.pack()
cb=tk.Button(root,text="create label",command=cl)
cb.pack()
cb.mainloop()
import tkinter as tk
def cm():
    ml.config(text="Good bye")
root=tk.Tk()
root.title("message changer")
ml=tk.Label(root,text="Hello")
ml.pack()
cb=tk.Button(root,text="change message",command=cm)
cb.pack()
cb.mainloop()
import tkinter as tk
def m(event):
    mpl.config(text=f"Mouse pressed at:({event.x},{event.y})")
def k(event):
    kpl.config(text=f"key pressed:{event.char}")
root=tk.Tk()
root.title("event handling")
root.geometry("500x400")
mpl=tk.Label(root,text="Key pressed will appear here")
mpl.pack()
kpl=tk.Label(root,text="Key pressed will appear here")
kpl.pack()
root.bind("<Button-1>",m)
root.bind("<KeyPress>",k)
root.mainloop()

import tkinter as tk
def m(event):
    mpl.config(text=f"Mouse pressed at:({event.x,event.y})")
def k(event):
    kpl.config(text=f"Key pressed at:{event.char}")
root=tk.Tk()
root.title("event handling")
root.geometry("500x400")
mpl=tk.Label(root,text="mouse pressed appear here")
mpl.pack()
kpl=tk.Label(root,text="Key pressed appear here")
kpl.pack()
root.bind("<Button-1>",m)
root.bind("<KeyPress>",k)
root.mainloop()
el=[1,2,3,4,5]
n=10
d=0
try:
    r=n/d
    print(r)
except ZeroDivisionError:
    print("Error:not allowed")
index=10
try:
    e=el[index]
    print(index,":",e)
except IndexError:
    print(f"Error: Index {index} is out of bounds for the list.")
index=2
try:
    e=el[index]
    print(index,":",e)
except IndexError:
    print(f"Error: Index {index} is out of bounds for the list.")
import math
a=int(input("enter"))
b=int(input("enter"))
g=math.gcd(a,b)
if(a>0 and b>0):
    print(g)
else:
    print(-g)
data=input("data:")
l1=data.split(",")
l1=map(int,l1)
l1=list(l1)
print(l1)
num=int(input("num:"))
ind=l1.index(num)
if(l1[ind]==l1[ind+1]):
    print("True")
else:
    print("False")
a=[]
n=int(input('enter {}'))
for i in range(n):
    e=int(input('num {}'.format(i)))
    a.append(e)
print("ele are:")
for i in a:
    print(i,end=' ')'''






















































'''import turtle
turtle.setup(800,600)
window=turtle.Screen()
tr=turtle.getturtle()
tr.hideturtle()
tr.setposition(100,0)
tr.setposition(100,100)
tr.setposition(0,100)
tr.setposition(0,0)
turtle.exitonclick()
import turtle
turtle.setup(800,600)
window=turtle.Screen()
tr=turtle.getturtle()
tr.hideturtle()
tr.forward(100)
tr.left(120)
tr.forward(100)
tr.left(120)
tr.forward(100)
turtle.exitonclick()'''
import turtle
turtle.setup(800,600)
window=turtle.Screen()
t=turtle.getturtle()
t.hideturtle()
t.resizemode('user')
t.turtlesize(3,3)
turtle.colormode(255)
t.pensize(5)
t.pencolor(238,130,238)
t.penup()
t.goto(-150, 0)
t.left(60)
t.forward(100)
t.pendown()
t.right(120)
t.forward(100)
t.left(120)
t.forward(100)
t.right(120)
t.forward(100)
t.left(120)
t.forward(100)
turtle.exitonclick()
      
    
        































































































































































































