import random
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from functools import partial

bet = 0
deposit = 0
roll = 0
paying = 0

letter = ["A", "B", "C", "D", "E"]

winner = {
    "AAA": 100, "BBB": 15, "CCC": 10, "DDD": 5, "EEE": 5
}

window = tkinter.Tk()
window.geometry("500x250")
window.title("Mini Slot Machine")
window.resizable(height=False, width=False)

frame = tkinter.Frame(window)
frame.pack()

#Deposit Frame
def submit_deposit(label_result, n1):
    global deposit
    try:
        num1 = int(n1.get())
        deposit += num1 
        label_result.config(text="You Have Added $%d Deposit" % num1)  
    except ValueError:
        label_result.config(text="Please enter a number!")

number1 = tkinter.StringVar()

#frame two
deposit_frame = tkinter.LabelFrame(frame, text="Add Deposit")
deposit_frame.grid(row=2, column=0, padx=20, pady=10)

dollar_label = tkinter.Label(deposit_frame, text="$")
dollar_label.grid(row=0, column=0)

dollar_input = tkinter.Entry(deposit_frame, textvariable=number1)
dollar_input.grid(row=0, column=1, columnspan=2)

labelResult = tkinter.Label(deposit_frame)  
labelResult.grid(row=1, column=1)

call_result = partial(submit_deposit, labelResult, number1)  

submit_button = tkinter.Button(deposit_frame, text="Submit",
                               command=call_result)
submit_button.grid(row=0, column=4)

for widget in deposit_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Play Frame

window.mainloop()