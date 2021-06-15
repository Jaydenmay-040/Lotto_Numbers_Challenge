from tkinter import *
import tkinter as tk

# initialise the root
window = Tk()
window.title("Lotto Machine: Jayden May")
window.geometry("900x600")
window.config(bg="yellow")

# Create a photo/image object of the image in the path
img = PhotoImage(file="image1.png")
Label(window, image=img, bg="yellow", width=370, height=125).place(x=265, y=10)

#  Heading
label = Label(window, text="Prizes to be won", fg="black", bg="yellow", font=("Arial", 20, 'bold')).place(x=340, y=200)

# Prizes
prediction_six = Label(window, text="6 correct numbers", width=20, font=("Arial", 15, 'bold')).place(x=220, y=270)
prize_six = Label(window, text="R10, 000 000.00", width=20, font=("Arial", 15, 'bold')).place(x=450, y=270)
prediction_five = Label(window, text="5 correct numbers", width=20, font=("Arial", 15, 'bold')).place(x=220, y=310)
prize_five = Label(window, text="R8,584.00", width=20, font=("Arial", 15, 'bold')).place(x=450, y=310)
prediction_four = Label(window, text="4 correct numbers", width=20, font=("Arial", 15, 'bold')).place(x=220, y=350)
prize_four = Label(window, text="R2,384.00", width=20, font=("Arial", 15, 'bold')).place(x=450, y=350)
prediction_three = Label(window, text="3 correct numbers", width=20, font=("Arial", 15, 'bold')).place(x=220, y=390)
prize_three = Label(window, text="R100.50", width=20, font=("Arial", 15, 'bold')).place(x=450, y=390)
prediction_two = Label(window, text="2 correct numbers", width=20, font=("Arial", 15, 'bold')).place(x=220, y=430)
prize_two = Label(window, text="R20.00", width=20, font=("Arial", 15, 'bold')).place(x=450, y=430)
prediction_one = Label(window, text="1 correct numbers", width=20, font=("Arial", 15, 'bold')).place(x=220, y=470)
prize_one = Label(window, text="R0", width=20, font=("Arial", 15, 'bold')).place(x=450, y=470)
prediction_zero = Label(window, text="0 correct numbers", width=20, font=("Arial", 15, 'bold')).place(x=220, y=510)
prize_zero = Label(window, text="R0", width=20, font=("Arial", 15, 'bold')).place(x=450, y=510)


def back():
    window.destroy()
    import Login
prizes_button = tk.Button(window, text="Back", command=back, height=2, width=10).place(x=80, y=530)

window.mainloop()

