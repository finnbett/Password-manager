# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
window = Tk()
window.config(padx=20, pady=20)
w = Canvas(window, width=200, height=200)
logo = PhotoImage(file="logo.png")
image = w.create_image(100, 100, image=logo)

w.pack()
window.mainloop()