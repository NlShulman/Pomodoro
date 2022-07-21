from tkinter import *
import math
from playsound import playsound

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None


def play_break_sound():
    playsound("Break.wav")


def reset_timer():
    global rep
    window.after_cancel(timer)
    rep = 0
    timer_label.configure(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_canvas, text="00:00")
    check_mark.configure(text="")


def start_timer():
    global rep
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if rep % 2 == 0:
        count_down(work_sec)
        timer_label.configure(text="WORK", fg=GREEN)
    elif rep % 7 == 0:
        play_break_sound()
        count_down(long_break_sec)
        timer_label.configure(text="BREAK", fg=RED)
    elif rep % 2 != 0:
        play_break_sound()
        count_down(short_break_sec)
        timer_label.configure(text="BREAK", fg=PINK)
    rep += 1


def count_down(count):
    global timer
    minute = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(timer_canvas, text=f"{minute}:{sec}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    # elif rep < 8:
    #     start_timer()
    #     if rep == 3:
    #         check_mark.configure(text="🗸")
    #     elif rep == 5:
    #         check_mark.configure(text="🗸🗸")
    #     elif rep == 7:
    #         check_mark.configure(text="🗸🗸🗸")
    elif rep < 8:
        start_timer()
        mark = ""
        for i in range(math.floor(rep/2)):
            mark += "🗸"
        check_mark.configure(text=mark)


window = Tk()
window.title("Pomodoro")
window.configure(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_canvas = canvas.create_text(110, 120, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", fg=GREEN, background=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(row=0, column=1)
check_mark = Label(fg=GREEN, background=YELLOW, font=(FONT_NAME, 20, "bold"))
check_mark.grid(row=3, column=1)

reset_button = Button()
reset_button.configure(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

start_button = Button()
start_button.configure(text="Start", command=start_timer)
start_button.grid(row=2, column=0)


window.mainloop()