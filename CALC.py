import re
import tkinter as tk
import math
from math import sin, tan, cos, sqrt, log, pi, acos, asin, atan, radians, degrees, log10

Trigo_mode=False
# Create main window
root = tk.Tk()
root.title("Tkinter Calculator")
root.geometry("300x460")
root.config(bg="#226C1C")
root.resizable(False, False)

# Entry widget to display input/output
display = tk.Entry(root, font=("Monotype Corsiva", 20), borderwidth=5, relief="ridge", justify="right",bg="#2CFAFF")
display.pack(fill="both", ipadx=8, ipady=9, padx=10, pady=10)

Par=True

# Function to add text to display
def button_click(value):
    display.insert(tk.END, value)

# Function to clear display
def clear_display():
    global Par
    Par=True
    display.delete(0, tk.END)
def trig_click(trig):
    global Par
    Par=False
    display.insert(tk.END,trig)
# Function to calculate result

point=None


Btn_digits=[]
def parenth(event):
    global Par
    if Par:
        display.insert(tk.END,"(")
        Par=False
    else:
        display.insert(tk.END, ")")
        Par=True
def calculate():

    try:

        expr=display.get()

        expr=display.get().replace("^","**").replace("Pi",str(pi))
        safe_env={"sin":lambda x:sin(radians(x)),"cos":lambda x:cos(radians(x)),"tan":lambda x:tan(radians(x)),"asin":lambda x:degrees(asin(x)),"acos":lambda x:degrees(acos(x)),"atan":lambda x:degrees(atan(x)),"sqrt":sqrt,"pi":pi,"log":log10}

        result = eval(expr,{"__builtins__":None},safe_env)
        clear_display()
        display.insert(0, f"{result:.6g}")
    except:
        clear_display()
        display.insert(0, "E")

# Frame for buttons
buttons_frame = tk.Frame(root,bg="#226C1C")
buttons_frame.pack()
# Button layout
buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("+", 3, 2), ("=", 3, 3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(buttons_frame, text=text, font=("Arial", 14),
                        command=calculate, width=5, height=2,bg="#FF8C00",relief="groove",activebackground="#FF8C00")
    else:
        btn = tk.Button(buttons_frame, text=text, font=("Monotype Corsiva", 14),
                        command=lambda t=text: button_click(t),
                        width=5, height=2,bg="#FF8C00",relief="ridge",activebackground="#FF8C00")
        if btn["text"] in ["0","1","2","3","4","5","6","7","8","9"]:
               Btn_digits.append(btn)
        elif btn["text"]==".":
            point=btn
            point.config(text=".\nRM-( )")

    btn.grid(row=row, column=col, padx=5, pady=5)
point.bind("<Button-3>",parenth)

# Clear button
clear_btn = tk.Button(root, text="Clear\n RM-Backspace", font=("Monotype Corsiva", 11),
                      command=clear_display,bg="#54FF45",activebackground="#226C1C")
clear_btn.pack()

def backspace(event):
    global Par
    display.delete(len(display.get())-1,tk.END)
    if display.get() and Par:
        Par=False
    elif display.get() and display.get()[-1]  in ["+","/","*","-"]:
        Par=True
    else:
        Par=True
clear_btn.bind("<Button-3>",backspace)

def switch_mode():
    global Trigo_mode,point,Par
    if Trigo_mode:
        lbs=["sin(","cos(","tan(","asin(","acos(","atan(","log(","sqrt(","^","Pi"]
        Trigo_mode=False
    else:
        Trigo_mode=True
        lbs=["7","8","9","4","5","6","1","2","3","0"]
    for i,j in enumerate(Btn_digits):
        lab=lbs[i]
        j.config(text=lab)
        j.config(command=lambda click=lab:button_click(click))
        if j["text"] in  ["sin(","cos(","tan(","asin(","acos(","atan(","log(","sqrt("]:
            j.config(command=lambda click=lab: trig_click(click))

switch_btn=tk.Button(root,text="Switch",font=("Monotype Corsiva",12),bg="#2900FF",activebackground="#2900FF",command=switch_mode)
switch_btn.pack(ipadx=14,pady=14)


root.mainloop()
