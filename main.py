from tkinter import *

# todo if calorie_sum > 1400: calorie_sum = RED
# todo save log to csv


BLACK = "#191919"
GREY = "#30475e"
WHITE = "#e8e8e8"
FONT = ("Courier", 10, "normal")

daily_goal = 1400
calorie_sum = 0


def one_add():
    global calorie_sum
    calorie_sum += 1
    total_label.config(text=f"{calorie_sum}/{daily_goal}")


def ten_add():
    global calorie_sum
    calorie_sum += 10
    total_label.config(text=f"{calorie_sum}/{daily_goal}")


def fifty_add():
    global calorie_sum
    calorie_sum += 50
    total_label.config(text=f"{calorie_sum}/{daily_goal}")


def points_add():
    global calorie_sum
    calorie_sum += 100
    total_label.config(text=f"{calorie_sum}/{daily_goal}")


def coffee_add():
    global calorie_sum
    calorie_sum += 35
    total_label.config(text=f"{calorie_sum}/{daily_goal}")


def noodles_add():
    global calorie_sum
    calorie_sum += 370
    total_label.config(text=f"{calorie_sum}/{daily_goal}")


def toast_add():
    global calorie_sum
    calorie_sum += 180
    total_label.config(text=f"{calorie_sum}/{daily_goal}")


def tea_add():
    global calorie_sum
    calorie_sum += 15
    total_label.config(text=f"{calorie_sum}/{daily_goal}")


def end_day():
    # write to csv
    pass


window = Tk()
window.title("CICO")
window.config(bg=BLACK)

# heading
heading = Label(text="Calorie Calculator", fg=WHITE, bg=BLACK, font=FONT)
heading.grid(column=1, row=0, columnspan=3)

# total
total_label = Label(text=f"0/{daily_goal}", fg=WHITE, bg=BLACK, font=FONT)
total_label.grid(column=0, row=4, columnspan=4)

one = Button(text="1", width=3, bg=BLACK, fg=WHITE, activebackground=GREY, command=one_add)
one.grid(column=0, row=2)

ten = Button(text="10", width=3, bg=BLACK, fg=WHITE, activebackground=GREY, command=ten_add)
ten.grid(column=1, row=2)

fifty = Button(text="50", width=3, bg=BLACK, fg=WHITE, activebackground=GREY, command=fifty_add)
fifty.grid(column=2, row=2)

points_btn = Button(text="100", bg=BLACK, fg=WHITE, activebackground=GREY, command=points_add)
points_btn.grid(column=3, row=2)

coffee = PhotoImage(file="./images/coffee.png")
coffee_btn = Button(image=coffee, bg=BLACK, activebackground=GREY, command=coffee_add)
coffee_btn.grid(column=1, row=3)

noodles = PhotoImage(file="./images/noodles.png")
noodles_btn = Button(image=noodles, bg=BLACK, activebackground=GREY, command=noodles_add)
noodles_btn.grid(column=2, row=3)

toast = PhotoImage(file="./images/toast.png")
toast_btn = Button(image=toast, bg=BLACK, activebackground=GREY, command=toast_add)
toast_btn.grid(column=0, row=3)

tea = PhotoImage(file="./images/tea.png")
tea_btn = Button(image=tea, bg=BLACK, activebackground=GREY, command=tea_add)
tea_btn.grid(column=3, row=3)
# reset new day button (saves the previous day to csv)
sun = PhotoImage(file="./images/sun.png")
sun_btn = Button(image=sun, bg=BLACK, activebackground=GREY, command=end_day)
sun_btn.grid(column=0, row=0)

window.mainloop()
