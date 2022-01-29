from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(text_item, text=f"00:00")
    timer_label.config(text='Timer')
    check_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text='Short Break', fg=PINK)
    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text='Long Break', fg=RED)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text='Work', fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count >= 0:
        canvas.itemconfig(text_item, text=f"{count_min}:{count_sec}")
        global timer
        timer = window.after(1000, count_down, (count-1))
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50,bg=YELLOW)

canvas = Canvas(height=200, width=230, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 97, image=photo)
text_item = canvas.create_text(100, 124, text="00:00", font=(FONT_NAME, 35, 'bold'), fill='white')
canvas.grid(column=1, row=1)

timer_label = Label(text='Timer', font=(FONT_NAME, 25, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()
