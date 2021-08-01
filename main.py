from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#50C878"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=NONE

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="TIMER",fg=GREEN)
    checkmark.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_time=WORK_MIN*60
    break_time=SHORT_BREAK_MIN*60
    long_break=LONG_BREAK_MIN*60
    if reps%8==0:
        say(long_break)
        title_label.config(title_label,text="Long break",fg=GREEN)
    elif reps%2==0:
        say(break_time)    
        title_label.config(text="Short Break",fg=PINK)
    else:
        title_label.config(text="Work time",fg=RED)
        say(work_time)    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time
def say(count):
    count_min=floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,say,count-1)
    else:
        start_timer()    
        marks=""
        work_session=floor(reps/2)
        for _ in range(work_session):
            marks+="✓"
        checkmark.config(text=marks)   
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
title_label=Label(text="TIMER",fg=GREEN,font=(FONT_NAME,50),bg=YELLOW)
title_label.grid(row=1,column=2)
tomato=PhotoImage(file="tomato.png")
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image=tomato)
timer_text=canvas.create_text(100,138,text="00:00",fill="white",font=(FONT_NAME,32,"bold"))
canvas.grid(row=2,column=2)
start_button=Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(row=3,column=1)
reset_button=Button(text="Reset",highlightthickness=0,command=reset)
reset_button.grid(row=3,column=3)
checkmark=Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME,35,"bold"))
checkmark.grid(row=4,column=2)  
window.mainloop()