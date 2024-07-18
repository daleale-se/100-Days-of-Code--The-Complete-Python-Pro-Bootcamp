import tkinter as tk


def main():

    window = tk.Tk()
    window.title("GUI")
    window.minsize(width=500, height=500)
    window.config(padx=50, pady=50)

    # label
    my_label = tk.Label(text="I'm a label", font=("Sans", 14, "italic"))
    my_label["text"] = "..."
    # my_label.pack(side="top")
    # my_label.place(x=0, y=300)
    my_label.grid(column=0, row=0)
    my_label.config(padx=20)

    # entry
    my_entry = tk.Entry(width=10)
    # my_entry.pack()
    # my_entry.place(x=100, y=100)
    my_entry.grid(column=3, row=2)

    def button_clicked():
        user_input = my_entry.get()
        my_label.config(text=f"{user_input}", background="black")

    # button
    my_button = tk.Button(text="I'm a button", command=button_clicked)
    # my_button.pack(side="top")
    # my_button.place(x=400, y=300)
    my_button.grid(column=1, row=1)
    my_button.config(padx=30)

    other_button = tk.Button(text="New button")
    other_button.grid(column=2, row=0)

    window.mainloop()


main()