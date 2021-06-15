import datetime
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from playsound import playsound
import rsaidnumber
from dateutil import relativedelta

# initialise the root
window = Tk()
window.title("Lotto Machine: Jayden May")
window.geometry("900x600")
window.config(bg="yellow")

# Create a photo/image object of the image in the path
img = PhotoImage(file="image1.png")
Label(window, image=img, bg="yellow", width=370, height=125).place(x=265, y=10)

#  Heading
label = Label(window, text="Enter the following:", fg="black", bg="yellow", font=("Arial", 20)).place(x=340, y=200)

# Entries
first_name_entry = Entry(window)
first_name_label = Label(window, text="First Name", bg="yellow", font=("Arial", 13))
last_name_entry = Entry(window)
last_name_label = Label(window, text="Last Name", bg="yellow", font=("Arial", 13))
age_entry = Entry(window, width=10,)
age_label = Label(window, text="Age", bg="yellow", font=("Arial", 13))


# Function to tells if user is older enough to play
def enter():
    try:
        age = age_entry.get()
        int(age_entry.get())
        d_o_b = rsaidnumber.parse(age).date_of_birth
        if len(age) > 13 or len(age) < 13:
            raise ValueError
        elif relativedelta.relativedelta(datetime.datetime.today(), d_o_b).years > 18:
            messagebox.showinfo(message='Congrats! You can play.')
            window.destroy()
            import Login_user
        else:
            messagebox.showerror(message='Sorry! You are underage.')
    except ValueError:
        messagebox.showerror(message='ID number either too long or too short')

# Buttons
enter_button = tk.Button(window, text="Enter", command=enter, height=2, width=10).place(x=280, y=500)
exit_button = tk.Button(window, text="Exit", command=exit, height=2, width=10).place(x=490, y=500)


def lotto_prizes():
    window.destroy()
    import Lotto_prizes
prizes_button = tk.Button(window, text="Prizes", command=lotto_prizes, height=2, width=10).place(x=780, y=30)

first_name_entry.place(x=180, y=300)
last_name_entry.place(x=400, y=300)
age_entry.place(x=630, y=300)

first_name_label.place(x=200, y=340)
last_name_label.place(x=418, y=340)
age_label.place(x=655, y=340)

window.mainloop()
