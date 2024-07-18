import tkinter as tk


def main():

    window = tk.Tk()
    window.title("Mile to Km Converter")
    window.minsize(width=200, height=75)
    window.config(padx=20, pady=20)

    entry_mile = tk.Entry()
    entry_mile.config(width=10)
    entry_mile.grid(column=1, row=0)

    label_miles = tk.Label(text="Miles")
    label_miles.grid(column=2, row=0)

    label_is_equal = tk.Label(text="is equal to")
    label_is_equal.grid(column=0, row=1)

    label_result_km = tk.Label(text=f"0")
    label_result_km.grid(column=1, row=1)

    label_km = tk.Label(text="Km")
    label_km.grid(column=2, row=1)

    button_converter = tk.Button(text="Calculate")
    button_converter.grid(column=1, row=2)

    def miles_to_km():
        km = float(entry_mile.get()) * 1.609344
        label_result_km.config(text=f"{km}")

    button_converter.config(command=miles_to_km)

    window.mainloop()

main()
