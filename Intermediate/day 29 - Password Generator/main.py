from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, messagebox, END
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


def main():

    def generate_password():
        # Password Generator Project
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_list = [random.choice(letters) for _ in range(random.randint(4, 6))]
        password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
        password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

        random.shuffle(password_list)

        password = "".join(password_list)

        password_entry.insert(0, password)
        pyperclip.copy(password)

    def save_password():
        website_data = website_entry.get()
        email_data = email_entry.get()
        password_data = password_entry.get()

        if website_data == "" or email_data == "" or password_data == "":
            messagebox.showerror(title="Error", message="There are empty fields")
        else:
            is_ok = messagebox.askokcancel(title=website_data, message=f"These are the details entered: \nEmail: "
                                                                       f"{email_data} Password: {password_data} \nIs "
                                                                       f"it ok to save?")
            if is_ok:
                with open("./data.txt", "a") as file:
                    file.write(f"{website_data} | {email_data} | {password_data}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

    window = Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50, bg="gray")

    canvas = Canvas(width=200, height=200, bg="gray", highlightthickness=0)
    lock_png = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=lock_png)
    canvas.grid(column=1, row=0)

    website_label = Label(text="Website:")
    website_label.grid(column=0, row=1)
    website_label.focus()
    email_label = Label(text="Email/Username:")
    email_label.grid(column=0, row=2)
    password_label = Label(text="Password:")
    password_label.grid(column=0, row=3)

    website_entry = Entry(width=36)
    website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
    email_entry = Entry(width=36)
    email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
    email_entry.insert(0, "daleale.se@gmail.com")
    password_entry = Entry(width=21)
    password_entry.grid(column=1, row=3, sticky="EW")

    generate_button = Button(text="Generate Password", command=generate_password)
    generate_button.grid(column=2, row=3, sticky="EW")
    add_button = Button(text="Add", width=36, command=save_password)
    add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

    window.mainloop()


main()
