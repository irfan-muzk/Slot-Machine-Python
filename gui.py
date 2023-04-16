import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

window = tkinter.Tk()
window.geometry("500x250")
window.title("Mini Slot Machine")
window.resizable(height=False, width=False)

frame = tkinter.Frame(window)
frame.pack()

#frame one
spin_frame = tkinter.Frame(frame)
spin_frame.grid(row=1, column=0, padx=20, pady=10)

box1_label = tkinter.Label(spin_frame, text="?")
box1_label.grid(row=0, rowspan=2, column=0)

box2_label = tkinter.Label(spin_frame, text="?")
box2_label.grid(row=0, rowspan=2, column=1)

box3_label = tkinter.Label(spin_frame, text="?")
box3_label.grid(row=0, rowspan=2, column=2)

spin_button = tkinter.Button(spin_frame, text="Spin")
spin_button.grid(row=0, column=3)

display_label = tkinter.Label(spin_frame, text="Your Deposit is..")
display_label.grid(row=2, column=0, columnspan=4)

for widget in spin_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#frame two
deposit_frame = tkinter.LabelFrame(frame, text="Add Deposit")
deposit_frame.grid(row=2, column=0, padx=20, pady=10)

dollar_label = tkinter.Label(deposit_frame, text="$")
dollar_label.grid(row=0, column=0)

dollar_input = tkinter.Entry(deposit_frame)
dollar_input.grid(row=0, column=1, columnspan=2)

submit_button = tkinter.Button(deposit_frame, text="Submit")
submit_button.grid(row=0, column=4)

for widget in deposit_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#frame three
bet_spin_frame = tkinter.LabelFrame(frame)
bet_spin_frame.grid(row=0, column=0, padx=20, pady=10)

bet_label = tkinter.Label(bet_spin_frame, text="Bet: $")
bet_label.grid(row=0, column=0)
bet_box = ttk.Combobox(bet_spin_frame, values=[
    2, 5, 10, 20, 50, 100
])
bet_box.grid(row=1, column=0)

spin_label = tkinter.Label(bet_spin_frame, text="Spin")
spin_label.grid(row=0, column=1)
spin_box = ttk.Combobox(bet_spin_frame, values=[
        1, 2, 5, 10, 20, 50, 100, 200, 500, 1_000, 2_000, 10_000
])
spin_box.grid(row=1, column=1)

window.mainloop()