import math
from tkinter import Tk, Canvas, PhotoImage, Label, Button

# ---------------------------- CONSTANTS ------------------------------- #

LIGHT_PINK = "#FFCBCB"
PINK = "#FFB1B1"
BLUE = "#1679AB"
DARK_BLUE = "#102C57"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"

reps = 0
timer = None


def main():

    # ---------------------------- TIMER RESET ------------------------------- #

    def reset_timer():
        window.after_cancel(timer)
        canvas.itemconfig(timer_text, text=f"00:00")
        title_label.config(text="Timer")
        check_label.config(text="")
        start_button.config(state="normal")
        global reps
        reps = 0

    # ---------------------------- TIMER MECHANISM ------------------------------- #

    def start_timer():
        global reps
        reps += 1
        print(reps)
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        start_button.config(state="disabled")

        if reps in [1, 3, 5, 7]:
            count_down(work_sec)
            title_label.config(text="Work Time")
        elif reps in [2, 4, 6]:
            count_down(short_break_sec)
            title_label.config(text="Break Time")
        elif reps == 8:
            count_down(long_break_sec)
            title_label.config(text="Long\nBreak Time")

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

    def count_down(count):
        minutes = math.floor(count / 60)
        seconds = count % 60

        if seconds < 10:
            seconds = f"0{seconds}"

        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        if count > 0:
            global timer
            timer = window.after(1000, count_down, count - 1)
        elif count == 0:
            start_timer()
            if reps % 2 == 0:
                text = f"{CHECK_MARK*int(reps/2)}"
                check_label.config(text=text)

    # ---------------------------- UI SETUP ------------------------------- #

    window = Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50, bg=LIGHT_PINK)

    canvas = Canvas(width=200, height=224, bg=LIGHT_PINK, highlightthickness=0)
    tomato_png = PhotoImage(file="tomato.png")
    canvas.create_image(100, 112, image=tomato_png)
    timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.grid(column=1, row=1)

    title_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"))
    title_label.config(fg=BLUE, bg=LIGHT_PINK)
    title_label.grid(column=1, row=0)

    start_button = Button(text="start", bg=PINK, fg=DARK_BLUE, font=(FONT_NAME, 10, "bold"), highlightthickness=0,
                          command=start_timer)
    start_button.grid(column=0, row=2)

    reset_button = Button(text="reset", bg=PINK, fg=DARK_BLUE, font=(FONT_NAME, 10, "bold"), highlightthickness=0,
                          command=reset_timer)
    reset_button.grid(column=2, row=2)

    check_label = Label(fg=BLUE, bg=LIGHT_PINK, font=(FONT_NAME, 20, "normal"))
    check_label.grid(column=1, row=3)

    window.mainloop()


main()
