from tkinter import *

window = Tk()
window.title("SDET-SOLOMAN's Miles to KM converter")
window.minsize(width=400, height=400)
window.config(padx=200, pady=200)

is_equal_to = Label(text="is equal to", font=("Arial", 28, 'italic'))
is_equal_to.grid(column=3, row=3)
is_equal_to.config(pady=10)

user_km = Label(text=f"{0}", font=("Arial", 28, 'italic'))
user_km.grid(column=4, row=3)
km = Label(text="KM", font=("Arial", 22, 'italic'))
km.grid(column=5, row=3)
km.config(padx=10)

user_miles = Entry(width=22)
user_miles.grid(column=4, row=2)
miles = Label(text="Miles", font=("Arial", 22, 'italic'))
miles.grid(column=5, row=2)
miles.config(padx=10)


def clicked():
    answer = user_miles.get()
    conv = round((int(answer) * 1.609344), 3)
    user_km = Label(text=f"{conv}", font=("Arial", 28, 'italic'))
    user_km.grid(column=4, row=3)


button = Button(text='Click Me', command=clicked)
button.grid(column=5, row=6)
button.config(padx=11, pady=11)

window.mainloop()

# pack, place, grid
# pack center, side
# place precise positioning, x=0 y=0
# grid tic tac toe # column = vniz, row = pryamo
