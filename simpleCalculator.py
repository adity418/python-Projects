from tkinter import *
import ast
from math import factorial


i = 0
def get_variable(num):
    global i
    display.insert(END,num)
    i += 1

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(END, operator)
    i += length

def clear_all():
    display.delete(0, END)

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0,"Error")

def calculate():
    entire_string = display.get()
    try:
        expr_ast = ast.parse(entire_string, mode='eval')
        result = eval(compile(expr_ast, filename="<string>", mode="eval"))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

def fact():
    entire_string = display.get()
    try:
        result= factorial(int(entire_string))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")
root = Tk()
root.title("Aditya-Calculator")

display = Entry(root)
display.grid(row=1, columnspan=6,sticky=N+E+W+S)

Button(root,text="1",command=lambda: get_variable(1)).grid(row=2,column=0,sticky=N+S+E+W)
Button(root,text="2",command=lambda: get_variable(2)).grid(row=2,column=1,sticky=N+S+E+W)
Button(root,text="3",command=lambda: get_variable(3)).grid(row=2,column=2,sticky=N+S+E+W)
Button(root,text="4",command=lambda: get_variable(4)).grid(row=3,column=0,sticky=N+S+E+W)
Button(root,text="5",command=lambda: get_variable(5)).grid(row=3,column=1,sticky=N+S+E+W)
Button(root,text="6",command=lambda: get_variable(6)).grid(row=3,column=2,sticky=N+S+E+W)
Button(root,text="7",command=lambda: get_variable(7)).grid(row=4,column=0,sticky=N+S+E+W)
Button(root,text="8",command=lambda: get_variable(8)).grid(row=4,column=1,sticky=N+S+E+W)
Button(root,text="9",command=lambda: get_variable(9)).grid(row=4,column=2,sticky=N+S+E+W)
Button(root,text="AC",command=lambda: clear_all()).grid(row=5,column=0,sticky=N+S+E+W)
Button(root,text="0",command=lambda: get_variable(0)).grid(row=5,column=1,sticky=N+S+E+W)
Button(root,text=".",command=lambda: get_variable(".")).grid(row=5,column=2,sticky=N+S+E+W)
Button(root,text="+",command=lambda: get_operation("+")).grid(row=2,column=3,sticky=N+S+E+W)
Button(root,text="-",command=lambda: get_operation("-")).grid(row=3,column=3,sticky=N+S+E+W)
Button(root,text="*",command=lambda: get_operation("*")).grid(row=4,column=3,sticky=N+S+E+W)
Button(root,text="/",command=lambda: get_operation("/")).grid(row=5,column=3,sticky=N+S+E+W)
Button(root,text="pi",command=lambda: get_operation("3.14")).grid(row=2,column=4,sticky=N+S+E+W)
Button(root,text="%",command=lambda: get_operation("%")).grid(row=3,column=4,sticky=N+S+E+W)
Button(root,text="(",command=lambda: get_operation("(")).grid(row=4,column=4,sticky=N+S+E+W)
Button(root,text="exp",command=lambda: get_operation("**")).grid(row=5,column=4,sticky=N+S+E+W)
Button(root,text="<-",command=lambda: undo()).grid(row=2,column=5,sticky=N+S+E+W)
Button(root,text="x!",command=lambda: fact()).grid(row=3,column=5,sticky=N+S+E+W)
Button(root,text=")",command=lambda: get_operation(")")).grid(row=4,column=5,sticky=N+S+E+W)
Button(root,text="^2",command=lambda: get_operation("**2")).grid(row=5,column=5,sticky=N+S+E+W)
Button(root,text="=",command=lambda: calculate()).grid(columnspan=6,sticky=N+S+E+W)







root.mainloop()
