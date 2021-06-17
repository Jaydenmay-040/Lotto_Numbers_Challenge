import datetime
from tkinter import *
import tkinter as tk
from tkinter import messagebox

# initialise the root
window = Tk()
window.title("Lotto Machine: Jayden May")
window.geometry("900x600")
window.config(bg="yellow")

# Create a photo/image object of the image in the path
img = PhotoImage(file="image1.png")
Label(window, image=img, bg="yellow", width=370, height=125).place(x=265, y=10)

#  Heading
label = Label(window, text="Enter your banking details", fg="black", bg="yellow", font=("Arial", 20)).place(x=300, y=200)

# Entries
account_holder_name_entry = Entry(window)
account_holder_name_entry.place(x=180, y=300)
account_holder_name_label = Label(window, text="Account Holder Name", bg="yellow", font=("Arial", 13))
account_holder_name_label.place(x=170, y=340)
account_number_entry = Entry(window)
account_number_entry.place(x=400, y=300)
account_number_label = Label(window, text="Account Number", bg="yellow", font=("Arial", 13))
account_number_label.place(x=415, y=340)
variable = StringVar()
variable.set('Select Bank')
bank_opt = OptionMenu(window, variable, 'FNB', 'Capitec', 'Netbank', 'Standard Bank')
bank_opt.place(x=630, y=300)
# bank_label = Label(window, text="Select your Bank", bg="yellow", font=("Arial", 13))
# bank_label.place(x=655, y=340)


# Function to tells if user is older enough to play
def enter():
    try:
        name_ent = account_holder_name_entry.get()
        str(account_holder_name_entry.get())
        if type(name_ent) is str:
            messagebox.showinfo(message='Details have been entered correctly.')
        elif type(name_ent) is int:
            raise ValueError
    except ValueError:
        messagebox.showerror(message='Something went wrong! Ensure that field is entered correctly')

# Buttons
enter_button = tk.Button(window, text="Enter", command=enter, height=2, width=10).place(x=280, y=500)
exit_button = tk.Button(window, text="Exit", command=exit, height=2, width=10).place(x=490, y=500)

window.mainloop()
