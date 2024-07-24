from tkinter import Tk, Label, PhotoImage, Button

BACKGROUND_COLOR = "#B1DDC6"


def main():

    window = Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

    language_label = Label(text="french")
    language_label.grid(column=0, row=0, columnspan=2)

    language_word = Label(text="word")
    language_word.grid(column=0, row=1, columnspan=2)

    wrong_image = PhotoImage(file="./images/wrong.png")
    wrong_button = Button(image=wrong_image, highlightthickness=0)
    wrong_button.grid(column=0, row=2)

    right_image = PhotoImage(file="./images/right.png")
    right_button = Button(image=right_image, highlightthickness=0)
    right_button.grid(column=1, row=2)

    window.mainloop()

main()