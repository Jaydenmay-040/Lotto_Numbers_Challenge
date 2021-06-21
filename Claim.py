import datetime
from validate_email import validate_email
import smtplib
# from email.mine.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import requests


window = Tk()
window.title("Lotto Machine: Jayden May")
window.geometry("900x600")
window.config(bg="yellow")

# Create a photo/image object of the image in the path
img = PhotoImage(file="image1.png")
Label(window, image=img, bg="yellow", width=370, height=125).place(x=265, y=10)

#  Heading
label = Label(window, text="Enter your banking details", fg="black", bg="yellow", font=("Arial", 20)).place(x=300,
                                                                                                            y=170)

# Entries
account_holder_name_entry = Entry(window)
account_holder_name_entry.place(x=400, y=255)
account_holder_name_label = Label(window, text="Account Holder Name", bg="yellow", font=("Arial", 13))
account_holder_name_label.place(x=170, y=255)
account_number_entry = Entry(window)
account_number_entry.place(x=400, y=295)
account_number_label = Label(window, text="Account Number", bg="yellow", font=("Arial", 13))
account_number_label.place(x=170, y=295)
variable = StringVar()
variable.set('Select Bank')
bank_opt = OptionMenu(window, variable, 'FNB', 'Capitec', 'Netbank', 'Standard Bank')
bank_opt.place(x=630, y=255)
currency_entry = Entry(window)
currency_entry.place(x=400, y=335)
currency_label = Label(window, text="Enter currency code", bg="yellow", font=("Arial", 13))
currency_label.place(x=170, y=335)
with open("Login_use.txt", "r") as file:
    for line in file:
        if "Prize" in line:
            prize = line[8:-1]
amount_entry = Entry(window, state="normal")
amount_entry.insert(0, prize)
amount_entry.config(state='readonly')
amount_entry.place(x=400, y=375)
amount_label = Label(window, text="Amount won", bg='yellow', font=("Arial", 13))
amount_label.place(x=170, y=375)
answer_label = Label(window, bg="white", width=20)
answer_label.place(x=400, y=415)
email_entry = Entry(window)
email_entry.place(x=400, y=455)
email_label = Label(window, text="Email", bg="yellow", font=("Arial", 13))
email_label.place(x=170, y=455)


def currency_convert():
    api = "https://v6.exchangerate-api.com/v6/4a704b6911da3fab9b1df53d/latest/ZAR"
    data = requests.get(api).json()
    result = round(float(amount_entry.get()), 2) * data['conversion_rates'][currency_entry.get()]
    print(result)
    answer_label.config(text=result)


answer_button = Button(window, text="Convert", command=currency_convert)
answer_button.place(x=170, y=415)


# Function to tells if user is older enough to play
def enter():
    try:
        list1 = ["1", "2", "3", "4", '5', "6", "7", "8", '9', "0"]
        name_ent = account_holder_name_entry.get()
        number_ent = account_number_entry.get()
        email_ent = email_entry.get()
        with open("Login.txt", "a+") as f:
            f.write('Account Holder Name: ' + account_holder_name_entry.get() + '\n')
            f.write('Account Number: ' + account_number_entry.get() + '\n')
            f.write('Currency Code: ' + currency_entry.get() + '\n')
            f.write('Email: ' + email_entry.get() + '\n'+ '\n')
        if name_ent == '':
            raise ValueError
        elif name_ent in list1:
            raise ValueError
        if number_ent == '':
            raise ValueError
        elif len(number_ent) < 10 or len(number_ent) > 10:
            messagebox.showerror(message="Hello it's wrong")
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
        if email_ent == '':
            raise ValueError
        else:
            if not validate_email(email_ent):
                messagebox.showerror(message='Please enter correct email')
        s = smtplib.SMTP('smtp.gmail.com', 587)
        sender_email = 'jaydenmay040@gmail.com'
        receiver_email = email_entry.get()
        password = 'elatedcream040'
        subject = 'Congratulations Champ, you won!!!'
        s.starttls()
        s.login(sender_email, password)
        message = 'Your details reads as the following:\n'
        message = message + '\nBank: ' + variable.get() + '\nAccount holder name: ' + account_holder_name_entry.get() +\
                      '\nAccount number: ' + account_number_entry.get() + '\nCurrency: ' + currency_entry.get() + \
                      '\nAccount number: ' + account_number_entry.get() + '\nCurrency: ' + currency_entry.get() + \
                      '\nYour prize will be transferred into your account within 3-6 business days  \n' \
                      'If any of your personal info was not entered incorrectly or you would like to know more ' \
                      'information, contact out services line on 021 675 4132.' \
                      'Thank you for playing the Lotto:), \n' \
                      '~ Lotto Generator Ltd.'
        s.sendmail(sender_email, receiver_email, message)
        s.quit()
    except ValueError:
        messagebox.showerror(message='Something went wrong! Please ensure that fields are entered correctly')


# Buttons
enter_button = tk.Button(window, text="Enter", command=enter, height=2, width=10, bg="Green").place(x=280, y=500)


def exit():
    messagebox.showinfo(message="Thank you for playing, enjoy you prize:)")
    window.destroy()


exit_button = tk.Button(window, text="Exit", command=exit, height=2, width=10, bg="red").place(x=490, y=500)

window.mainloop()
