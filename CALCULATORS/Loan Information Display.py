from tkinter import *

# Function part
vehicle_amount = 0

def calculate_loan():
    global vehicle_amount,monthly_payment
    vehicle_amount = float(vehicle_price_entry.get())
    loan_term = int(loan_terms_entry.get())
    interest_rate = 0.0215

    # Formula to get the percent of amount
    downPayment_20percent = vehicle_amount * 0.20
    downPayment_30percent = vehicle_amount * 0.30
    downPayment_40percent = vehicle_amount * 0.40

    # Formula to get the loan amount
    loanAmount_20percent = vehicle_amount - downPayment_20percent
    loanAmount_30percent = vehicle_amount - downPayment_30percent
    loanAmount_40percent = vehicle_amount - downPayment_40percent

    # Formula to get the monthly amortization
    monthly_amortization_20percent = loanAmount_20percent * (interest_rate / 12) * ((1 +(interest_rate / 12))**loan_term) / (((1 + (interest_rate / 12))**loan_term) -1)
    monthly_amortization_30percent = loanAmount_30percent * (interest_rate / 12) * ((1 +(interest_rate / 12))**loan_term) / (((1 + (interest_rate / 12))**loan_term) -1)
    monthly_amortization_40percent = loanAmount_40percent * (interest_rate / 12) * ((1 +(interest_rate / 12))**loan_term) / (((1 + (interest_rate / 12))**loan_term) -1)


    # Below is the  label for displaying the Loan Information of the user

    # This is the label of result
    result_lbl = Label(frame_LoanInformation_frm,text="RESULT",font=("Poppins", 8),bg="white")
    result_lbl.place(x=130,y=0)

    # For vehicle Price
    vehicle_price_lbl = Label(frame_LoanInformation_frm,text="Vehicle Price:",font=("Poppins", 8),bg="white")
    vehicle_price_lbl.place(x=0,y=20)
    display_vehicle_price_lbl = Label(frame_LoanInformation_frm, text=f"{vehicle_amount:,}", font=("Poppins", 8), bg="white")
    display_vehicle_price_lbl.place(x=100,y=20)

    # For down payment
    downPayment_lbl = Label(frame_LoanInformation_frm,text="DOWN PAYMENT:",font=("Poppins", 8),bg="white")
    downPayment_lbl.place(x=0,y=40)
    downPayment_20percent_lbl = Label(frame_LoanInformation_frm,text="20%",font=("Poppins", 8),bg="white")
    downPayment_20percent_lbl.place(x=10,y=60)
    downPayment_30percent_lbl = Label(frame_LoanInformation_frm,text="30%",font=("Poppins", 8),bg="white")
    downPayment_30percent_lbl.place(x=10,y=80)
    downPayment_40percent_lbl = Label(frame_LoanInformation_frm,text="40%",font=("Poppins", 8),bg="white")
    downPayment_40percent_lbl.place(x=10,y=100)
    display_downPayment_20percent_lbl = Label(frame_LoanInformation_frm, text=f"{downPayment_20percent:,.2f}",font=("Poppins", 8), bg="white")
    display_downPayment_20percent_lbl.place(x=100, y=60)
    display_downPayment_30percent_lbl = Label(frame_LoanInformation_frm, text=f"{downPayment_30percent:,.2f}",font=("Poppins", 8), bg="white")
    display_downPayment_30percent_lbl.place(x=100, y=80)
    display_downPayment_40percent_lbl = Label(frame_LoanInformation_frm, text=f"{downPayment_40percent:,.2f}",font=("Poppins", 8), bg="white")
    display_downPayment_40percent_lbl.place(x=100, y=100)

    # This is for Loan Term
    loan_term_lbl = Label(frame_LoanInformation_frm,text="LOAN TERM:",font=("Poppins", 8),bg="white")
    loan_term_lbl.place(x=0,y=130)
    display_loan_term_lbl = Label(frame_LoanInformation_frm,text=loan_term,font=("Poppins", 8),bg="white")
    display_loan_term_lbl.place(x=90,y=130)

    # This is for interest rate
    interest_rate_lbl = Label(frame_LoanInformation_frm,text="INTEREST RATE",font=("Poppins", 8),bg="white")
    interest_rate_lbl.place(x=0,y=150)
    display_interest_rate_lbl = Label(frame_LoanInformation_frm,text="25.80%",font=("Poppins", 8),bg="white")
    display_interest_rate_lbl.place(x=90,y=150)

    # This is for loan amount
    loan_amount_lbl = Label(frame_LoanInformation_frm,text="LOAN AMOUNT:",font=("Poppins", 8),bg="white")
    loan_amount_lbl.place(x=0,y=170)
    loanAmount_20percent_lbl = Label(frame_LoanInformation_frm,text="20%",font=("Poppins", 8),bg="white")
    loanAmount_20percent_lbl.place(x=10,y=190)
    loanAmount_30percent_lbl = Label(frame_LoanInformation_frm,text="30%",font=("Poppins", 8),bg="white")
    loanAmount_30percent_lbl.place(x=10,y=210)
    loanAmount_40percent_lbl = Label(frame_LoanInformation_frm,text="40%",font=("Poppins", 8),bg="white")
    loanAmount_40percent_lbl.place(x=10,y=230)
    display_loanAmount_20percent_lbl = Label(frame_LoanInformation_frm, text=f"{loanAmount_20percent:,.2f}",font=("Poppins", 8), bg="white")
    display_loanAmount_20percent_lbl.place(x=100, y=190)
    display_loanAmount_30percent_lbl = Label(frame_LoanInformation_frm, text=f"{loanAmount_30percent:,.2f}",font=("Poppins", 8), bg="white")
    display_loanAmount_30percent_lbl.place(x=100, y=210)
    display_loanAmount_40percent_lbl = Label(frame_LoanInformation_frm, text=f"{loanAmount_40percent:,.2f}",font=("Poppins", 8), bg="white")
    display_loanAmount_40percent_lbl.place(x=100, y=230)

    # This is for monthly amortization
    monthly_amortization_lbl = Label(frame_LoanInformation_frm,text="MONTHLY AMORTIZATION:",font=("Poppins", 8),bg="white")
    monthly_amortization_lbl.place(x=0,y=260)
    monthlyAmortization_20percent_lbl = Label(frame_LoanInformation_frm,text="20%",font=("Poppins", 8),bg="white")
    monthlyAmortization_20percent_lbl.place(x=10,y=280)
    monthlyAmortization_30percent_lbl = Label(frame_LoanInformation_frm,text="30%",font=("Poppins", 8),bg="white")
    monthlyAmortization_30percent_lbl.place(x=10,y=300)
    monthlyAmortization_40percent_lbl = Label(frame_LoanInformation_frm,text="40%",font=("Poppins", 8),bg="white")
    monthlyAmortization_40percent_lbl.place(x=10,y=320)
    display_monthlyAmortization_20percent_lbl = Label(frame_LoanInformation_frm,text=f"{monthly_amortization_20percent:,.2f}",font=("Poppins", 8), bg="white")
    display_monthlyAmortization_20percent_lbl.place(x=100, y=280)
    display_monthlyAmortization_30percent_lbl = Label(frame_LoanInformation_frm,text=f"{monthly_amortization_30percent:,.2f}",font=("Poppins", 8), bg="white")
    display_monthlyAmortization_30percent_lbl.place(x=100, y=300)
    display_monthlyAmortization_40percent_lbl = Label(frame_LoanInformation_frm,text=f"{monthly_amortization_40percent:,.2f}",font=("Poppins", 8), bg="white")
    display_monthlyAmortization_40percent_lbl.place(x=100, y=320)



def clear_textField():
    vehicle_price_entry.delete(0,END)
    loan_terms_entry.delete(0,END)


# GUI part
loan_Information_display = Tk()
loan_Information_display.geometry("350x550")
loan_Information_display.title("Loan Information Display")

# Main frame
main_frm = Frame(loan_Information_display, bg="sky blue", width=350, height=550)
main_frm.place(x=0, y=0)

# Frame for user input
userInput_frm = Frame(main_frm, bg="white", width=225, height=100)
userInput_frm.place(x=65, y=25)

# Frame for text field Loan Information
frame_LoanInformation_frm = Frame(main_frm, bg="white", width=300, height=400)
frame_LoanInformation_frm.place(x=25, y=135)

# Labels and Entries for user input
vehicle_price_lbl = Label(userInput_frm, text="Vehicle Price:", font=("Poppins", 8), bg="white")
vehicle_price_lbl.place(x=10, y=10)
loan_terms_lbl = Label(userInput_frm, text="Loan Terms:", font=("Poppins", 8), bg="white")
loan_terms_lbl.place(x=10, y=35)

vehicle_price_entry = Entry(userInput_frm, width=15, font=("Poppins", 8), bg="white")
vehicle_price_entry.place(x=95, y=10)
loan_terms_entry = Entry(userInput_frm, width=15, font=("Poppins", 8), bg="white")
loan_terms_entry.place(x=95, y=35)

# Clear and Calculate buttons
clear_btn = Button(userInput_frm, width=10, text="Clear", font=("Poppins", 8), bg="white", command=clear_textField)
clear_btn.place(x=20, y=65)
calculate_btn = Button(userInput_frm, width=10, text="Calculate", font=("Poppins", 10, "bold"), bg="white", command=calculate_loan)
calculate_btn.place(x=115, y=65)

loan_Information_display.mainloop()
