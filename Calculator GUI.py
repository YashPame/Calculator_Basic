import tkinter
from tkinter import *
from tkinter import messagebox

val = ""
A = 0
operator = ""


def btn1_clicked():
    global val
    val = val + "1"
    data.set(val)


def btn2_clicked():
    global val
    val = val + "2"
    data.set(val)


def btn3_clicked():
    global val
    val = val + "3"
    data.set(val)


def btn4_clicked():
    global val
    val = val + "4"
    data.set(val)


def btn5_clicked():
    global val
    val = val + "5"
    data.set(val)


def btn6_clicked():
    global val
    val = val + "6"
    data.set(val)


def btn7_clicked():
    global val
    val = val + "7"
    data.set(val)


def btn8_clicked():
    global val
    val = val + "8"
    data.set(val)


def btn9_clicked():
    global val
    val = val + "9"
    data.set(val)


def btn0_clicked():
    global val
    val = val + "0"
    data.set(val)

def btn_plus():
    global A
    global operator
    global val
    A=int(val)
    operator="+"
    val=val + "+"
    data.set(val)

def btn_min():
    global A
    global operator
    global val
    A=int(val)
    operator="-"
    val=val + "-"
    data.set(val)

def btn_multiply():
    global A
    global operator
    global val
    A=int(val)
    operator="*"
    val=val + "*"
    data.set(val)

def btn_divide():
    global A
    global operator
    global val
    A=int(val)
    operator="/"
    val=val + "/"
    data.set(val)

def c():
    global A
    global operator
    global val
    val=""
    A=0
    operator=""
    data.set(val)

def result():
    global A
    global operator
    global val
    val2=val
    if operator=="+":
        x=int((val2.split("+")[1]))
        c=A+x
        data.set(c)
        val=str(c)
    elif operator=="-":
        x=int((val2.split("-")[1]))
        c=A-x
        data.set(c)
        val=str(c)
    elif operator=="*":
        x=int((val2.split("*")[1]))
        c=A*x
        data.set(c)
        val=str(c)
    elif operator=="/":
        x=int((val2.split("/")[1]))
        if x==0:
            messagebox.showerror("Error", "Error")
            A=""
            val=""
            data.set(val)
        else:
            c=float(A/x)
            data.set(c)
            val=str(c)

root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0, 0)
root.title("Calculator")

data = StringVar()
lbl = Label(
    root,
    text="Label",
    anchor=SE,
    font=("Verdana", 20),
    textvariable=data,
    bg="#ffffff",
    fg='#000000'
)
lbl.pack(expand=True, fill="both")

btnrow1 = Frame(root, bg='#000000')
btnrow1.pack(expand=True, fill="both")

btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill="both")

btnrow3 = Frame(root)
btnrow3.pack(expand=True, fill="both")

btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill="both")

btn1 = Button(
    btnrow1,
    text=1,
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn1_clicked
)
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(
    btnrow1,
    text=2,
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn2_clicked
)
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(
    btnrow1,
    text=3,
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn3_clicked
)
btn3.pack(side=LEFT, expand=True, fill="both")

btn4 = Button(
    btnrow1,
    text='+',
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_plus
)
btn4.pack(side=LEFT, expand=True, fill="both")

btn1 = Button(
    btnrow2,
    text=4,
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn4_clicked
)
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(
    btnrow2,
    text=5,
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn5_clicked
)
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(
    btnrow2,
    text=6,
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn6_clicked
)
btn3.pack(side=LEFT, expand=True, fill="both")

btn4 = Button(
    btnrow2,
    text='-',
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_min
)
btn4.pack(side=LEFT, expand=True, fill="both")

btn1 = Button(
    btnrow3,
    text=7,
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn7_clicked
)
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(
    btnrow3,
    text=8,
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn8_clicked
)
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(
    btnrow3,
    text=9,
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn9_clicked
)
btn3.pack(side=LEFT, expand=True, fill="both")

btn4 = Button(
    btnrow3,
    text='*',
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_multiply
)
btn4.pack(side=LEFT, expand=True, fill="both")

btn1 = Button(
    btnrow4,
    text='C',
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command= c
)
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(
    btnrow4,
    text=0,
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn0_clicked
)
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(
    btnrow4,
    text='=',
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=result
)
btn3.pack(side=LEFT, expand=True, fill="both")

btn4 = Button(
    btnrow4,
    text='/',
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_divide
)
btn4.pack(side=LEFT, expand=True, fill="both")

root.mainloop()
