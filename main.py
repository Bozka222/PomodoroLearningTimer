from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        #  If it's the 8th rep:
        count_down(long_break_sec)  # Start timer
        label_timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        #  If it's the 2nd/4th/6th rep:
        count_down(short_break_sec)  # Start timer
        label_timer.config(text="Break", fg=PINK)
    else:
        #  If it's the 1st/3rd/5th/7th rep:
        count_down(work_sec)  # Start timer
        label_timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:  # Start with  :00 sec
        count_sec = "00"
    if len(str(count_sec)) == 1:  # Adds 0 if there is just one number of seconds
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)  # Method which reacts to timer event
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
            label_check.config(text=marks)


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    label_timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    label_check.config(text="")
    global reps
    reps = 0


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer App")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # Method to read image
canvas.create_image(100, 112, image=tomato_img)  # Put image in canvas
canvas.grid(row=1, column=1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))  # Puts text on
# canvas

label_timer = Label(text="Timer", font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW)
label_timer.grid(row=0, column=1)

button_start = Button(text="Start", font=("Arial", 10, "bold"), bd=10, command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", font=("Arial", 10, "bold"), bd=10, command=reset_timer)
button_reset.grid(row=2, column=2)

label_check = Label(font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
label_check.grid(row=3, column=1)
window.mainloop()
