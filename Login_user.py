import uuid
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random
from playsound import playsound

# initialise the root
window = Tk()
window.title("Lotto Machine: Jayden May")
window.geometry("900x600")
window.config(bg="yellow")
#playsound('sound1.mp3')

# Create a photo/image object of the image in the path
img = PhotoImage(file="image1.png")
Label(window, image=img, bg="yellow", width=370, height=125).place(x=265, y=10)
player_id = str(uuid.uuid1())
player_id = player_id[0:5]
# DOB Heading
label = Label(window, text="Welcome "+player_id, fg="black", bg="yellow", font=("Arial", 25, 'bold')).place(x=330, y=170)


# Entries
number_label = Label(window, text="Enter a set of numbers ranging from 1-49:", bg="yellow", font=("Arial", 16)).place(x=240, y=240)

# Entries for user to enter numbers
first_number_entry = Entry(window, width=6)
first_number_entry.place(x=160, y=310)
second_number_entry = Entry(window, width=6)
second_number_entry.place(x=260, y=310)
third_number_entry = Entry(window, width=6)
third_number_entry.place(x=360, y=310)
fourth_number_entry = Entry(window, width=6)
fourth_number_entry.place(x=460, y=310)
fifth_number_entry = Entry(window, width=6)
fifth_number_entry.place(x=560, y=310)
sixth_number_entry = Entry(window, width=6)
sixth_number_entry.place(x=660, y=310)
seventh_number_entry = Entry(window, width=3, state='readonly')
seventh_number_entry.place(x=300, y=375)
eighth_number_entry = Entry(window, width=3, state='readonly')
eighth_number_entry.place(x=350, y=375)
ninth_number_entry = Entry(window, width=3, state='readonly')
ninth_number_entry.place(x=400, y=375)
tenth_number_entry = Entry(window, width=3, state='readonly')
tenth_number_entry.place(x=450, y=375)
eleventh_number_entry = Entry(window, width=3, state='readonly')
eleventh_number_entry.place(x=500, y=375)
twelfth_number_entry = Entry(window, width=3, state='readonly')
twelfth_number_entry.place(x=550, y=375)

# Entries that display the Lotto draw and matching numbers
lotto_draw_numbers = Label(window, text="Lotto Draw is:", bg="yellow", font=("Arial", 13))
lotto_draw_numbers.place(x=160, y=375)
matching_numbers = Label(window, text="Your matching numbers:", bg="yellow", font=("Arial", 13))
matching_numbers.place(x=160, y=420)

# List of the users numbers
new_list = []
# List of the the random lotto numbers
lotto_numbers = random.sample(range(1, 50), 6)
print(lotto_numbers)


# Lotto draw function
# Reason for not using this is because it did not want to generate a new set of numbers so the player could take the
# old set of number, enter them and win. Then i created a new function.
# def lotto():
#     # Getting each number that the user enters
#     try:
#         new_list = [int(first_number_entry.get()), int(second_number_entry.get()), int(third_number_entry.get()),
#                      int(fourth_number_entry.get()),
#                      int(fifth_number_entry.get()), int(sixth_number_entry.get())]
#         # Takes the users numbers and puts it in a list, if the numbers are not between 1-49 it returns an error
#         for i in range(6):
#             if 0 <= int(new_list[i]) <= 49:
#                 new_list.append(new_list[i])
#             elif 49 < int(new_list[i]):
#                 messagebox.showerror("Something went wrong", "Enter numbers from range 0 - 49")
#             lotto_draw_label = Label(window, text=lotto_numbers, bg="yellow", font=("Arial", 13))
#             lotto_draw_label.place(x=300, y=375)
#
#         # Stores the lists using set and compares the two
#         matching_numbers = set(new_list) & set(lotto_numbers)
#
#         # if statement that displays if there are any matching numbers and will be displayed in a list
#         if new_list == new_list:
#             matching_numbers_entry = Entry(window, text=matching_numbers, bg="white", font=("Arial", 13))
#             matching_numbers_entry.place(x=400, y=420)
#             print(sorted(matching_numbers))
#         else:
#             if new_list == 0:
#                 with open("Login_use.txt", 'a') as file:
#                     file.write('Prize: R0' + '\n' + '\n')
#                 messagebox.showerror("Try again", "You have no matching numbers:(")
#
#         if len(matching_numbers) == 0:
#             with open("Login_use.txt", 'a') as file:
#                 file.write('Prize: R0' + '\n' + '\n')
#             matched_label = Label(window, text="0", bg='yellow', width='10', font=("Arial", 13))
#             matched_label.place(x=450, y=420)
#             messagebox.showerror("Try again", "You have no matching numbers:(")
#
#         elif len(matching_numbers) == 1:
#             with open("Login_use.txt", 'a') as file:
#                 file.write('Prize: R0' + '\n' + '\n')
#             messagebox.showerror("Too bad", "You only have one matching number, better luck next time")
#
#         elif len(matching_numbers) == 2:
#             with open("Login_use.txt", 'a') as file:
#                 file.write('Prize: R20.00' + '\n' + '\n')
#             messagebox.showinfo("Well Done!", "You won R20.00")
#
#             def claims():
#                 window.destroy()
#                 import Claim
#
#             claims_button = tk.Button(window, text="Claim Prize", command=claims, height=2, width=10,
#                                       bg="#f649a2").place(x=400, y=500)
#
#         elif len(matching_numbers) == 3:
#             with open("Login_use.txt", 'a') as file:
#                 file.write('Prize: R100.50' + '\n' + '\n')
#             messagebox.showinfo("Well Done!!", "You won R100.50")
#
#             def claims():
#                 window.destroy()
#                 import Claim
#
#             claims_button = tk.Button(window, text="Claim Prize", command=claims, height=2, width=10,
#                                       bg="#f649a2").place(x=400, y=500)
#
#         elif len(matching_numbers) == 4:
#             with open("Login_use.txt", 'a') as file:
#                 file.write('Prize: R2 384.00' + '\n' + '\n')
#             messagebox.showinfo("WOW!", "You won R2 384.00")
#
#             def claims():
#                 window.destroy()
#                 import Claim
#
#             claims_button = tk.Button(window, text="Claim Prize", command=claims, height=2, width=10,
#                                       bg="#f649a2").place(x=400, y=500)
#
#         elif len(matching_numbers) == 5:
#             with open("Login_use.txt", 'a') as file:
#                 file.write('Prize: R8584.00' + '\n' + '\n')
#             messagebox.showinfo("OMG!!!", "You won R8584.00")
#
#             def claims():
#                 window.destroy()
#                 import Claim
#
#             claims_button = tk.Button(window, text="Claim Prize", command=claims, height=2, width=10,
#                                       bg="#f649a2").place(x=400, y=500)
#
#         elif len(matching_numbers) == 6:
#             with open("Login_use.txt", 'a') as file:
#                 file.write('Prize: R10 000 000.00' + '\n' + '\n')
#             messagebox.showinfo("Congratulations Champ!!!!", "You won R10 000 000.00")
#
#             def claims():
#                 window.destroy()
#                 import Claim
#
#             claims_button = tk.Button(window, text="Claim Prize", command=claims, height=2, width=10,
#                                       bg="#f649a2").place(x=400, y=500)
#     except ValueError:
#         messagebox.showerror("Do you want to win??", "Then enter number!!")


def lotto():
    try:
        new_list = []
        while len(new_list) < 6:
            lotto_numbers = random.randint(1, 49)
            print(lotto_numbers)
            if lotto_numbers not in new_list:
                new_list.append(lotto_numbers)
        seventh_number_entry.config(state='normal')
        eighth_number_entry.config(state='normal')
        ninth_number_entry.config(state='normal')
        tenth_number_entry.config(state='normal')
        eleventh_number_entry.config(state='normal')
        twelfth_number_entry.config(state='normal')
        seventh_number_entry.delete(0, END)
        eighth_number_entry.delete(0, END)
        ninth_number_entry.delete(0, END)
        tenth_number_entry.delete(0, END)
        eleventh_number_entry.delete(0, END)
        twelfth_number_entry.delete(0, END)
        seventh_number_entry.config(state='normal')
        seventh_number_entry.insert(0, new_list[0])
        eighth_number_entry.config(state='normal')
        eighth_number_entry.insert(0, new_list[1])
        ninth_number_entry.config(state='normal')
        ninth_number_entry.insert(0, new_list[2])
        tenth_number_entry.config(state='normal')
        tenth_number_entry.insert(0, new_list[3])
        eleventh_number_entry.config(state='normal')
        eleventh_number_entry.insert(0, new_list[4])
        twelfth_number_entry.config(state='normal')
        twelfth_number_entry.insert(0, new_list[5])

        if first_number_entry.get() == "" or second_number_entry.get() == "" or third_number_entry == "" or fourth_number_entry == "" or fifth_number_entry == "" or sixth_number_entry == "":
            raise ValueError
        else:
            new_list = set(new_list)
            user_list = [int(first_number_entry.get()), int(second_number_entry.get()), int(third_number_entry.get()),
                         int(fourth_number_entry.get()),
                         int(fifth_number_entry.get()), int(sixth_number_entry.get())]
            matching_numbers = new_list.intersection(user_list)
            winnings = len(matching_numbers)
            if user_list == 0:
                with open("Login_use.txt", 'a') as file:
                    file.write('Prize: R0' + '\n' + '\n')
                playsound("Sad Trombone - Gaming Sound Effect (HD).mp3")
                messagebox.showerror("Try again", "You have no matching numbers:(")

            if winnings == 0:
                with open("Login_use.txt", 'a') as file:
                    file.write('Prize: R0' + '\n' + '\n')
                matched_label = Label(window, text="0", bg='yellow', width='10', font=("Arial", 13))
                matched_label.place(x=450, y=420)
                playsound("Sad Trombone - Gaming Sound Effect (HD).mp3")
                messagebox.showerror("Try again", "You have no matching numbers:(")

            elif winnings == 1:
                with open("Login_use.txt", 'a') as file:
                    file.write('Prize: R0' + '\n' + '\n')
                playsound("Sad Trombone - Gaming Sound Effect (HD).mp3")
                messagebox.showerror("Too bad", "You only have one matching number, better luck next time")

            elif winnings == 2:
                with open("Login_use.txt", 'a') as file:
                    file.write('Prize: R20.00' + '\n' + '\n')
                playsoud("ka-ching sound effect.mp3")
                messagebox.showinfo("Well Done!", "You won R20.00")

                def claims():
                    window.destroy()
                    import Claim

                claims_button = tk.Button(window, text="Claim Prize", command=claims, height=2, width=10,
                                          bg="#f649a2").place(x=400, y=500)

            elif winnings == 3:
                with open("Login_use.txt", 'a') as file:
                    file.write('Prize: R100.50' + '\n' + '\n')
                playsoud("ka-ching sound effect.mp3")
                messagebox.showinfo("Well Done!!", "You won R100.50")

                def claims():
                    window.destroy()
                    import Claim

                claims_button = tk.Button(window, text="Claim Prize", command=claims, height=2, width=10,
                                          bg="#f649a2").place(x=400, y=500)

            elif winnings == 4:
                with open("Login_use.txt", 'a') as file:
                    file.write('Prize: R2 384.00' + '\n' + '\n')
                playsoud("ka-ching sound effect.mp3")
                messagebox.showinfo("WOW!", "You won R2 384.00")

                def claims():
                    window.destroy()
                    import Claim

                claims_button = tk.Button(window, text="Claim Prize", command=claims, height=2, width=10,
                                          bg="#f649a2").place(x=400, y=500)

            elif winnings == 5:
                with open("Login_use.txt", 'a') as file:
                    file.write('Prize: R8584.00' + '\n' + '\n')
                playsoud("ka-ching sound effect.mp3")
                messagebox.showinfo("OMG!!!", "You won R8584.00")

                def claims():
                    window.destroy()
                    import Claim

                claims_button = tk.Button(window, text="Claim Prize", command=claims, height=2, width=10,
                                          bg="#f649a2").place(x=400, y=500)

            elif winnings == 6:
                with open("Login_use.txt", 'a') as file:
                    file.write('Prize: R10 000 000.00' + '\n' + '\n')
                playsoud("ka-ching sound effect.mp3")
                messagebox.showinfo("Congratulations Champ!!!!", "You won R10 000 000.00")

                def claims():
                    window.destroy()
                    import Claim

                claims_button = tk.Button(window, text="Claim Prize", command=claims, height=2, width=10,
                                          bg="#f649a2").place(x=400, y=500)
    except:
        messagebox.showerror("Do you want to win??", "Then enter number!!")


def try_again():
    first_number_entry.delete(0, END)
    second_number_entry.delete(0, END)
    third_number_entry.delete(0, END)
    fourth_number_entry.delete(0, END)
    fifth_number_entry.delete(0, END)
    sixth_number_entry.delete(0, END)
    seventh_number_entry.delete(0, END)
    eighth_number_entry.delete(0, END)
    ninth_number_entry.delete(0, END)
    tenth_number_entry.delete(0, END)
    eleventh_number_entry.delete(0, END)
    twelfth_number_entry.delete(0, END)


# Buttons
enter_button = tk.Button(window, text="Enter", command=lotto, height=2, width=10, bg="Green").place(x=260, y=500)
try_again_button = tk.Button(window, text="Try Again", command=try_again, height=2, width=10,
                             bg="#cb2eba").place(x=540, y=500)

# def clear():
# clear_button = tk.Button(window, text="Clear", command=clear, height=2, width=10, bg="#0696e0").place(x=540, y=500)
exit_button = tk.Button(window, text="Exit", command=exit, height=2, width=10, bg="Red").place(x=780, y=30)



window.mainloop()
