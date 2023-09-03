import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def random_pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = 8
    nr_symbols = 2
    nr_numbers = 2

    # Eazy Level - Order not randomised:

    password = []

    [password.append(letters[random.randint(0, len(letters) - 1)]) for x in range(0, nr_letters + 1)]
    [password.append(numbers[random.randint(0, len(numbers) - 1)]) for x in range(0, nr_numbers + 1)]
    [password.append(symbols[random.randint(0, len(symbols) - 1)]) for x in range(0, nr_symbols + 1)]
    random.shuffle(password)

    rand_pass = ''.join(password)
    pyperclip.copy(rand_pass)
    password_field.delete(0, END)
    password_field.insert(0, rand_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():

    website_ = website_field.get()
    email_ = email_field.get()
    password_ = password_field.get()
    new_data = {
        website_: {
            'email': email_,
            'password': password_,
        }
    }

    if len(password_) > 7 and len(website_) > 7:
        is_save = messagebox.askyesno(title='Attention', message=f"You have entered:\n"
                                                                 f"Website: {website_}\n"
                                                                 f"Email: {email_}\n"
                                                                 f"Password: {password_}\n"
                                                                 f"Do you want to save it?")
        if is_save:

            try:
                with open("my_passwords.json", mode='r') as my_passwords:

                    # to create and write:
                    # with open("my_passwords.json", mode='w') as my_passwords:
                    # json.dump(new_data, my_passwords, indent=5)

                    # to reade a jason:
                    # data = json.load(my_passwords)
                    # print(data)

                    # to append a json file:

                    data = json.load(my_passwords)
                    data.update(new_data)

            except FileNotFoundError:
                with open("my_passwords.json", mode='w') as my_passwords:
                    json.dump(new_data, my_passwords, indent=5)

            else:
                with open("my_passwords.json", mode='w') as my_passwords:
                    json.dump(data, my_passwords, indent=5)
                my_passwords.close()

            finally:
                website_field.delete(0, END)
                email_field.delete(0, END)
                password_field.delete(0, END)

    else:
        messagebox.showerror(message="Password and Website fields must be longer than 8 chars")


# ---------------------------- Search Button --------------------------#

def search_btn():
    website_ = website_field.get()
    try:
        with open("my_passwords.json", mode='r') as my_passwords:
            data = json.load(my_passwords)
            messagebox.showinfo(title=website_, message=f""
                                         f"Email: {data[website_]['email']}\n"
                                         f"Password: {data[website_]['password']}")
    except KeyError or FileNotFoundError:
        messagebox.showerror(message=f'No Data for {website_}')
    finally:
        my_passwords.close()




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("SDET-SOLOMAN's PASSWORD MANAGER")
window.config(padx=55, pady=55, bg='white')

canvas = Canvas(width=300, height=300, bg='white', highlightthickness=0)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(150, 150, image=lock_image)
canvas.grid(row=0, column=1)

website_name = Label(text="Website: ", fg='black', bg='white')
website_name.grid(column=0, row=1)
website_field = Entry(width=32, fg='black', bg='white')
website_field.grid(column=1, row=1)
website_field.focus()
search_button = Button(text='Search', width=19, command=search_btn, highlightthickness=0)
search_button.grid(column=2, row=1)

email_name = Label(text="Email/Username: ", fg='black', bg='white')
email_name.grid(column=0, row=2)
email_field = Entry(width=55, fg='black', bg='white')
email_field.insert(0, 'example@gmail.com')
email_field.grid(column=1, row=2, columnspan=2)

password_name = Label(text="Password: ", fg='black', bg='white')
password_name.grid(column=0, row=3)
password_field = Entry(width=55, fg='black', bg='white')
password_field.grid(column=1, row=3, columnspan=2)

generate_password_btn = Button(text='New Password', width=10, command=random_pass_generator, padx=40,
                               highlightthickness=0)
generate_password_btn.grid(column=2, row=4, columnspan=2, rowspan=2)
add_btn = Button(text='Add', width=13, command=save_data, padx=20, highlightthickness=0)
add_btn.grid(column=0, row=4, columnspan=2, rowspan=2)

window.mainloop()
