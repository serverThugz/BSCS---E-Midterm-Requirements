from tkinter import *
# This is the function part
calculation = " "
def add_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_field.delete(1.0, END)
    text_field.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_field.delete(1.0, "end")
        text_field.insert(1.0, calculation)
    except:
        clear_field()
        text_field.insert(1.0, "ERROR!")

def clear_field():
    global calculation
    calculation = " "
    text_field.delete(1.0, "end")


# This is GUI PART
calculator = Tk()
calculator.geometry("430x580")
calculator.title("CALCULATOR")
img = PhotoImage(file="/Calculator Icon.png")
calculator.iconphoto(False, img)
calculator.config(bg="black")

# This is Text Part
text_field = Text(calculator, font=("Poppins", 24, "bold"), height=2, width=24)
text_field.grid(columnspan=4)

# This is Button Part
btn9 = Button(calculator, text="9", font=("Poppins", 24), fg="white", bg="black", width=5, height=2, command=lambda: add_calculation(9))
btn9.grid(row=2, column=0)
btn8 = Button(calculator, text="8", font=("Poppins", 24), fg="white", bg="black", width=5, height=2, command=lambda: add_calculation(8))
btn8.grid(row=2, column=1)
btn7 = Button(calculator, text="7", font=("Poppins", 24), fg="white", bg="black", width=5, height=2, command=lambda: add_calculation(7))
btn7.grid(row=2, column=2)
btn6 = Button(calculator, text="6", font=("Poppins", 24), fg="white", bg="black", width=5, height=2, command= lambda: add_calculation(6))
btn6.grid(row=3, column=0)
btn5 = Button(calculator, text="5", font=("Poppins", 24), fg="white", bg="black", width=5, height=2, command=lambda: add_calculation(5))
btn5.grid(row=3, column=1)
btn4 = Button(calculator, text="4", font=("Poppins", 24), fg="white", bg="black", width=5, height=2, command=lambda: add_calculation(4))
btn4.grid(row=3, column=2)
btn3 = Button(calculator, text="3", font=("Poppins", 24), fg="white", bg="black", width=5, height=2, command=lambda: add_calculation(3))
btn3.grid(row=4, column=0)
btn2 = Button(calculator, text="2", font=("Poppins", 24), fg="white", bg="black", width=5, height=2, command=lambda: add_calculation(2))
btn2.grid(row=4, column=1)
btn1 = Button(calculator, text="1", font=("Poppins", 24), fg="white", bg="black", width=5, height=2, command=lambda: add_calculation(1))
btn1.grid(row=4, column=2)
btn0 = Button(calculator, text="0", font=("Poppins", 24), fg="white", bg="black", width=11, height=2, command=lambda: add_calculation(0))
btn0.grid(row=5, column=0,columnspan=2)

# This is operation part
clear_btn = Button(calculator,text="C", font=("Poppins", 24), fg="white", bg="navy blue", width=5, height=2, command=clear_field)
clear_btn.grid(row=1, column=0)
division_btn = Button(calculator, text="/", font=("Poppins", 24), fg="white", bg="black", width=5, height=2, command=lambda:add_calculation("/"))
division_btn.grid(row=1, column=1)
modulos_btn = Button(calculator, text="%", font=("Poppins", 24), fg="white", bg="black", width=5, height=2, command=lambda: add_calculation("%"))
modulos_btn.grid(row=1, column=2)
multiplication_btn = Button(calculator,text="x", font=("Poppins", 24), fg="white", bg="black", width=5,height=2, command=lambda:add_calculation("*"))
multiplication_btn.grid(row=1, column=3)
additional_btn = Button(calculator, text="+", font=("Poppins", 24), fg="white", bg="black", width=5, height=2, command=lambda:add_calculation("+"))
additional_btn.grid(row=2, column=3)
subtraction_btn = Button(calculator,text="-", font=("Poppins", 24), fg="white", bg="black", width=5, height=2, command=lambda:add_calculation("-"))
subtraction_btn.grid(row=3, column=3)
equal_btn = Button(calculator, text="=", font=("Poppins", 24), fg="white", bg="orange", width=5, height=5, command=evaluate_calculation)
equal_btn.grid(row=4, column=3,rowspan=3)
dot_btn = Button(calculator, text=".", font=("Poppins", 24), fg="white", bg="black", width=5, height=2, command=evaluate_calculation)
dot_btn.grid(row=5, column=2)
calculator.mainloop()