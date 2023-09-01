from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global REPS
    REPS = 0
    window.after_cancel(timer)
    canvas.itemconfig(clock_on_screen, text=f"00:00")
    timer_text.config(text="TIMER")
    checkmark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def clicked():
    global REPS

    REPS += 1

    work_secs = WORK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60

    if REPS % 2 == 8:
        timer_text.config(text="LONG BREAK", fg=RED)
        my_timer(long_break)

    elif REPS % 2 == 0:
        timer_text.config(text="SHORT BREAK", fg=PINK)
        my_timer(short_break)

    else:
        timer_text.config(text="TIME TO WORK", fg=GREEN)
        my_timer(work_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def my_timer(number):
    global REPS

    mins = number // 60
    secs = number % 60

    if mins < 10:
        mins = f"0{mins}"
    if secs < 10:
        secs = f"0{secs}"

    canvas.itemconfig(clock_on_screen, text=f"{mins}:{secs}")

    if number > 0:
        global timer
        timer = window.after(1000, my_timer, number - 1)
    else:
        checkmark.config(text="✅︎" * (REPS // 2))
        clicked()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("SDET-SOLOMANS POMODORO APP")
window.config(pady=60, padx=105, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
clock_on_screen = canvas.create_text(100, 130, text="00:00", fill="White", font=('Arial', 24, 'bold'))
canvas.grid(column=3, row=3)

start = Button(text="START", fg=PINK, bg=YELLOW, highlightthickness=0, command=clicked)
start.grid(column=0, row=7)
start.config(padx=2, pady=2)

timer_text = Label(text="TIMER", underline=33, fg=GREEN, font=("Arial", 66, 'italic'))
timer_text.grid(column=3, row=0)
timer_text.config(pady=20, padx=20, bg=YELLOW)

checkmark = Label(fg=GREEN, font=("Arial", 28, 'italic'))
checkmark.grid(column=3, row=7)
checkmark.config(pady=20, padx=20, bg=YELLOW)

finish = Button(text="RESTART", fg=PINK, bg=YELLOW, highlightthickness=0, command=reset)
finish.grid(column=5, row=7)
finish.config(padx=2, pady=2)

window.mainloop()
