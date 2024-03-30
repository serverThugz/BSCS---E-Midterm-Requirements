from tkinter import *

#FUNCTION PART
def add_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation =str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"ERROR!")

def clear_field():
    global calculation
    calculation = " "
    text_result.delete(1.0,"end")

#GUI PART
calculator = Tk()
calculator.geometry('270x300')
calculator.title('CALCULATOR')
calculator.resizable(0,0)
text_result = Text(calculator,height=2,width=30,font=('Arial',12,'bold'),fg='black')
text_result.grid(columnspan=25)
#NUMBER BUTTON PART
number9_button = Button(calculator,text='9',font=('Arial',14,'bold'),fg='black',width=4,command=lambda:add_calculation(9))
number9_button.grid(row=1,column=0)
number8_button = Button(calculator,text='8',font=('Arial',14,'bold'),fg='black',width=4,command=lambda:add_calculation(8))
number8_button.grid(row=1,column=1)
number7_button = Button(calculator,text='7',font=('Arial',14,'bold'),fg='black',width=4,command=lambda:add_calculation(7))
number7_button.grid(row=1,column=2)
number6_button = Button(calculator,text='6',font=('Arial',14,'bold'),fg='black',width=4,command=lambda:add_calculation(6))
number6_button.grid(row=2,column=0)
number5_button = Button(calculator,text='5',font=('Arial',14,'bold'),fg='black',width=4,command=lambda:add_calculation(5))
number5_button.grid(row=2,column=1)
number4_button = Button(calculator,text='4',font=('Arial',14,'bold'),fg='black',width=4,command=lambda:add_calculation(4))
number4_button.grid(row=2,column=2)
number3_button = Button(calculator,text='3',font=('Arial',14,'bold'),fg='black',width=4,command=lambda:add_calculation(3))
number3_button.grid(row=3,column=0)
number2_button = Button(calculator,text='2',font=('Arial',14,'bold'),fg='black',width=4,command=lambda:add_calculation(2))
number2_button.grid(row=3,column=1)
number1_button = Button(calculator,text='1',font=('Arial',14,'bold'),fg='black',width=4,command=lambda:add_calculation(1))
number1_button.grid(row=3,column=2)
number0_button = Button(calculator,text='0',font=('Arial',14,'bold'),fg='black',width=4,command=lambda:add_calculation(0))
number0_button.grid(row=4,column=0)
#OPERATION BUTTON
addition_button = Button(calculator,text='+',font=('Arial',14,'bold'),fg='black',width=4,command=lambda:add_calculation("+"))
addition_button.grid(row=1,column=3)
subtraction_button = Button(calculator,text='-',font=('Arial',14,'bold'),fg='black',width=4,command=lambda:add_calculation("-"))
subtraction_button.grid(row=2,column=3)
multiplication_button = Button(calculator,text='x',font=('Arial',14,'bold'),fg='black',width=4,command=lambda:add_calculation("*"))
multiplication_button.grid(row=3,column=3)
division_button = Button(calculator,text='/',font=('Arial',14,'bold'),fg='black',width=4,command=lambda:add_calculation("/"))
division_button.grid(row=4,column=3)
equal_button = Button(calculator,text='=',font=('Arial',14,'bold'),fg='black',width=4,command=evaluate_calculation)
equal_button.grid(row=4,column=1)
clear_button = Button(calculator,text='C',font=('Arial',14,'bold'),fg='black',width=4,command=clear_field)
clear_button.grid(row=4,column=2)

calculator.mainloop()