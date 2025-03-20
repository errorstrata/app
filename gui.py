from tkinter import * 
import tkinter.font as font

def enroll():
    output["text"] = "Enrolled Successfully"
    
    
def add():
    x = int(enterOne.get())
    y = int(enterTwo.get())
    result["text"] = x+y


def sub():
    x = int(enterOne.get())
    y = int(enterTwo.get())
    result["text"] = x-y


def div():
    x = int(enterOne.get())
    y = int(enterTwo.get())
    result["text"] = x/y


def mul():
    x = int(enterOne.get())
    y = int(enterTwo.get())
    result["text"] = x*y

root = Tk()
root.title("my programms GUI")


course = Label(root, text="MINE " ,fg = "red",bg ="blue")
button =Button(root,text="continue" ,bd = 2, fg="blue")
course.place(x="200",y="700")
button.place(x="200", y="750")


python = Button(root, text="Python", width=8)
java = Button(root, text="Java", width=8)
cpp = Button(root, text="C++", width=8)
javascript = Button(root, text="JavaScript", width=8)

python.grid(row=0, column=0)
java.grid(row=0, column=1)
cpp.grid(row=1, column=0)
javascript.grid(row=1, column=1)


lbl = Label(root, text="Name")
data = Entry(root)
lbl.grid(row=0, column=0)
data.grid(row=0, column=1)


lbl = Label(root, text="Python Course")
btn = Button(root, text="Enroll Now", command=enroll)
output = Label( root, text="" ,fg="#00bb00")
lbl.grid(row=0 ,column= 3)
btn.grid(row=1,column=3)
output.grid(row=2 , column=3)


numOne = Label(root, text="Enter First Number:", font=("Serif", 12))
enterOne = Entry(root)
numTwo = Label(root, text="Enter Second Number:", font=("Serif", 12))
enterTwo = Entry(root)

add = Button(root, text="Add", width=10, command=add)
sub = Button(root, text="Sub", width=10, command=sub)
div = Button(root, text="Div", width=10, command=div)
mul = Button(root, text="Mul", width=10, command=mul)

result = Label(root)

numOne.grid(row=3, column=0)
enterOne.grid(row=3, column=1)
numTwo.grid(row=4, column=0)
enterTwo.grid(row=4, column=1)


add.grid(row=5, column=0)
sub.grid(row=5, column=1)
div.grid(row=6, column=0)
mul.grid(row=6, column=1)
result.grid(row=7, column=2)

root.mainloop()