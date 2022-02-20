from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
#image
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
w = Canvas(window, width=200, height=200)
logo = PhotoImage(file="logo.png")
image = w.create_image(100, 100, image=logo)

#inputs
website = Entry(width=35)
website.grid(column=2, row=2, columnspan=2)
website_label = Label(text="Website:")
website_label.grid(column=1, row=2)
user_name = Entry(width=35)
user_name.grid(column=2, row=3, columnspan=2)
user_name_label = Label(text="Username/email:")
user_name_label.grid(column=1, row=3)
password = Entry(width=21)
password.grid(column=2, row=4)
password_label = Label(text="Password:")
password_label.grid(column=1, row=4)

#buttons
generate_password = Button(text="Generate Password")
generate_password.grid(row=4, column=3)
add = Button(text="Add", width=36)
add.grid(row=5, column=2, columnspan=2)


w.grid(row=1, column=2)
window.mainloop()