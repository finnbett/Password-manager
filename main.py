from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password_function():
    password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    new_password = ""
    for char in password_list:
        new_password += char

    password.insert(0, new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    # will write the data to a file,
    f = open("data.txt", "a")
    website_txt = website.get()
    password_txt = password.get()
    user_name_txt = user_name.get()
    data_check = True
    if len(website_txt) == 0 or len(password_txt) == 0 or len(user_name_txt) == 0:
        messagebox.showerror(title="Woops!", message="fill in all fields")
        data_check = False
    if data_check:
        is_ok = messagebox.askokcancel(title=website_txt, message=f"These are the details entered: \n User name: "
                                                                  f"{user_name_txt}\n "
                                                                  f"Website: {website_txt} \n Password: {password_txt}")
        if is_ok:
            f.write(f"{website_txt} | {password_txt} | {user_name_txt}\n")
            f.close()
            clear_entries()


def clear_entries():
    website.delete(0, END)
    password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# image
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
w = Canvas(window, width=200, height=200)
logo = PhotoImage(file="logo.png")
image = w.create_image(100, 100, image=logo)

# inputs
website = Entry(width=35)
website.grid(column=2, row=2, columnspan=2)
website_label = Label(text="Website:")
website_label.grid(column=1, row=2)
user_name = Entry(width=35)
user_name.grid(column=2, row=3, columnspan=2)
user_name.insert(0, "example@gmail.com")
user_name_label = Label(text="Username/email:")
user_name_label.grid(column=1, row=3)
password = Entry(width=21)
password.grid(column=2, row=4)
password_label = Label(text="Password:")
password_label.grid(column=1, row=4)

# buttons
generate_password = Button(text="Generate Password", command=generate_password_function)
generate_password.grid(row=4, column=3)
add = Button(text="Add", width=36, command=add_password)
add.grid(row=5, column=2, columnspan=2)

w.grid(row=1, column=2)
window.mainloop()
