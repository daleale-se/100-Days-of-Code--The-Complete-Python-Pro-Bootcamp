import random
from tkinter import Tk, PhotoImage, Button, Canvas
from tkinter.ttk import Style
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")

flip_timer = None
current_word = None


def main():
    def right():
        global current_word
        to_learn.remove(current_word)
        df = pandas.DataFrame(to_learn)
        df.to_csv("./data/words_to_learn.csv", index=False)
        next_card()

    def show_translate():
        canvas.itemconfig(canvas_image, image=back_image)
        canvas.itemconfig(language_text, text="English", fill="white")
        canvas.itemconfig(word_text, text=f"{current_word['English']}", fill="white")

    def next_card():
        global flip_timer, current_word
        if flip_timer:
            window.after_cancel(flip_timer)
        current_word = random.choice(to_learn)
        canvas.itemconfig(canvas_image, image=front_image)
        canvas.itemconfig(language_text, text="French", fill="black")
        canvas.itemconfig(word_text, text=f"{current_word['French']}", fill="black")
        flip_timer = window.after(3000, show_translate)

    window = Tk()
    window.title("Flashiness")
    window.style = Style()
    window.style.theme_use("alt")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

    try:
        data = pandas.read_csv("./data/words_to_learn.csv")
    except FileNotFoundError:
        data = pandas.read_csv("./data/french_words.csv")
    to_learn = data.to_dict(orient="records")

    canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    back_image = PhotoImage(file="./images/card_back.png")
    front_image = PhotoImage(file="./images/card_front.png")
    canvas_image = canvas.create_image(400, 265, image=front_image)
    language_text = canvas.create_text(400, 150, text="Title", fill="black", font=FONT_LANGUAGE)
    word_text = canvas.create_text(400, 263, text="Word", fill="black", font=FONT_WORD)
    canvas.grid(column=0, row=0, columnspan=2)

    wrong_icon = PhotoImage(file="./images/wrong.png")
    wrong_button = Button(image=wrong_icon, highlightthickness=0, bd=0, command=next_card)
    wrong_button.grid(column=0, row=1)

    right_icon = PhotoImage(file="./images/right.png")
    right_button = Button(image=right_icon, highlightthickness=0, bd=0, command=right)
    right_button.grid(column=1, row=1)

    next_card()

    window.mainloop()


main()
