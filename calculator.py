from tkinter import *



def button_pressed(num):
    global equation_text

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text

    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError as e:
        equation_label.set(str(e) + "Error")
        equation_text = ""
    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""


def clear():
    global equation_text

    equation_text = ""

    equation_label.set(equation_text)


window = Tk()
window.title("Calculator App")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=("consolas", 20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, font=35, height=4, width=9, command=lambda: button_pressed(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, font=35, height=4, width=9, command=lambda: button_pressed(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, font=35, height=4, width=9, command=lambda: button_pressed(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, font=35, height=4, width=9, command=lambda: button_pressed(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, font=35, height=4, width=9, command=lambda: button_pressed(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, font=35, height=4, width=9, command=lambda: button_pressed(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, font=35, height=4, width=9, command=lambda: button_pressed(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, font=35, height=4, width=9, command=lambda: button_pressed(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, font=35, height=4, width=9, command=lambda: button_pressed(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, font=35, height=4, width=9, command=lambda: button_pressed(0))
button0.grid(row=3, column=0)

plus = Button(frame, text="+", font=35, height=4, width=9, command=lambda: button_pressed("+"))
plus.grid(row=0, column=3)

minus = Button(frame, text="-", font=35, height=4, width=9, command=lambda: button_pressed("-"))
minus.grid(row=1, column=3)

multiply = Button(frame, text="*", font=35, height=4, width=9, command=lambda: button_pressed("*"))
multiply.grid(row=2, column=3)

divide = Button(frame, text="/", font=35, height=4, width=9, command=lambda: button_pressed("/"))
divide.grid(row=3, column=3)

equal = Button(frame, text="=", font=35, height=4, width=9, command=equals)
equal.grid(row=3, column=2)

decimal = Button(frame, text=".", font=35, height=4, width=9, command=lambda: button_pressed("."))
decimal.grid(row=3, column=1)

clear = Button(window, text="clear", font=35, height=4, width=12, command=clear)
clear.pack()

window.mainloop()