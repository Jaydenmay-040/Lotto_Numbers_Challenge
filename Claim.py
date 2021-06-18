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
account_holder_name_entry.place(x=400, y=300)
account_holder_name_label = Label(window, text="Account Holder Name", bg="yellow", font=("Arial", 13))
account_holder_name_label.place(x=170, y=300)
account_number_entry = Entry(window)
account_number_entry.place(x=400, y=340)
account_number_label = Label(window, text="Account Number", bg="yellow", font=("Arial", 13))
account_number_label.place(x=170, y=340)
variable = StringVar()
variable.set('Select Bank')
bank_opt = OptionMenu(window, variable, 'FNB', 'Capitec', 'Netbank', 'Standard Bank')
bank_opt.place(x=630, y=300)
currency_entry = Entry(window)
currency_entry.place(x=400, y=380)
currency_label = Label(window, text="Enter currency code", bg="yellow", font=("Arial", 13))
currency_label.place(x=170, y=380)



# Function to tells if user is older enough to play
def enter():
    # try:
    #     list1 = ["1", "2", "3", "4", '5', "6", "7", "8", '9', "0"]
    #     name_ent = account_holder_name_entry.get()
    #     if name_ent == "":
    #         raise ValueError
    #     for x in name_ent:
    #         if x in list1:
    #             raise ValueError
    #     messagebox.showinfo(message='Details have been entered correctly.')
    # except ValueError:
    #     messagebox.showerror(message='Something went wrong! Ensure that account holder name is entered correctly')
    #
    #     try:
    #         number_ent = account_number_entry.get()
    #         if number_ent == "":
    #             raise ValueError
    #         else:
    #             int(account_number_entry.get())
    #             messagebox.showinfo(message='Details have been entered correctly:)')
    #     except ValueError:
    #         messagebox.showerror(message='Something went wrong! Ensure that your account number is entered correctly')

            try:
                list1 = ["1", "2", "3", "4", '5', "6", "7", "8", '9', "0"]
                name_ent = account_holder_name_entry.get()
                number_ent = account_number_entry.get()
                if name_ent == '':
                    raise ValueError
                elif name_ent in list1:
                    raise ValueError
                if number_ent == '':
                    raise ValueError
                else:
                    int(account_number_entry.get())
                    messagebox.showinfo(message='Details have been entered correctly:)')
                if variable.get() == 'Select Bank':
                    raise ValueError
                elif variable.get() == 'FNB':
                    messagebox.showinfo(message='Details have been entered correctly:)')
                elif variable.get() == 'Capitec':
                    messagebox.showinfo(message='Details have been entered correctly:)')
                elif variable.get() == 'Netbank':
                    messagebox.showinfo(message='Details have been entered correctly:)')
                elif variable.get() == 'Standard Bank':
                    messagebox.showinfo(message='Details have been entered correctly:)')
            except ValueError:
                messagebox.showerror(message='Something went wrong! Please ensure that fields are entered correctly')

# Buttons
enter_button = tk.Button(window, text="Enter", command=enter, height=2, width=10, bg="Green").place(x=280, y=500)
exit_button = tk.Button(window, text="Exit", command=exit, height=2, width=10, bg="red").place(x=490, y=500)

window.mainloop()
