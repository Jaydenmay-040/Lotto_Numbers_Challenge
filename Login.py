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
        if int(age_entry.get()) >= 18:
            messagebox.showerror("You qualify", "Let's play" "\n" + first_name_entry.get() + "\n" + last_name_entry.get())

            window.destroy()
            import Login_user
        elif int(age_entry.get()) < 18:
            messagebox.showerror("You do not qualify", "Try again in a few years" "\n" + first_name_entry.get() + last_name_entry.get()
                                 )
    except ValueError:
        messagebox.showerror("Invalid", "Please enter your age")

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
