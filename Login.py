import datetime
from tkinter import *
import tkinter as tk
from tkinter import messagebox
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
first_name_entry.place(x=410, y=280)
first_name_label = Label(window, text="First Name", bg="yellow", font=("Arial", 13))
first_name_label.place(x=250, y=280)
last_name_entry = Entry(window)
last_name_entry.place(x=410, y=320)
last_name_label = Label(window, text="Last Name", bg="yellow", font=("Arial", 13))
last_name_label.place(x=250, y=320)
id_entry = Entry(window)
id_entry.place(x=410, y=360)
id_label = Label(window, text="ID No.", bg="yellow", font=("Arial", 13))
id_label.place(x=250, y=360)


# Function to tells if user is older enough to play
def enter():
    with open("Login.txt", "a+") as f:
        f.write('Name: ' + first_name_entry.get() + '\n')
        f.write('Surname: ' + last_name_entry.get() + '\n')
        f.write('ID No.: ' + id_entry.get() + '\n')
    try:
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        id_no = id_entry.get()
        int(id_entry.get())
        d_o_b = rsaidnumber.parse(id_no).date_of_birth
        player_id = first_name[:3] + id_no[:6]
        print(player_id)
        if len(id_no) > 13 or len(id_no) < 13:
            raise ValueError
        elif relativedelta.relativedelta(datetime.datetime.today(), d_o_b).years >= 18:
            messagebox.showinfo(message='Congrats! You can play.')
            window.destroy()
            import Login_user
        else:
            messagebox.showerror(message='Sorry! You are underage.')
        if first_name == '':
            raise ValueError
        elif last_name == '':
            raise ValueError
    except ValueError:
        messagebox.showerror(message='Please ensure that all fields are entered correctly')


# Buttons
enter_button = tk.Button(window, text="Enter", command=enter, height=2, width=10, bg="green").place(x=280, y=500)
exit_button = tk.Button(window, text="Exit", command=exit, height=2, width=10, bg="red").place(x=490, y=500)


def lotto_prizes():
    window.destroy()
    import Lotto_prizes


prizes_button = tk.Button(window, text="Prizes", command=lotto_prizes, height=2, width=10, bg="#0696e0").place(x=780, y=30)

window.mainloop()
