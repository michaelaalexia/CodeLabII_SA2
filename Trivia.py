from tkinter import *
root = Tk()
root.title("Art Trivia !")
root.geometry("1000x700")
root.resizable(0, 0)
root["bg"] = "black" # TK window

# variables for quick access 
b = "black"
f = "#9B6A6C"
btn = "#E75A7C"
t = "#F3E9DC"
url = "https://opentdb.com/api.php?amount=10&category=25&difficulty=easy"

# commands 
def display_page():
    quiz_page.tkraise()

title = Label(root, text="ART TRIVIA", fg=t, bg=b, font=("Times", 64))
title.place(x=270, y=44)

m_f = Frame(root, bg=f)
m_f.place(x=25, y=159, width=950, height=516)
m_b = Button(m_f, text="Begin", fg=t, bg=btn, font=("Times", 45), width=20, command=display_page)
m_b.place(x=150, y=200)

quiz_page = Frame(root, bg=f)
quiz_page.place(x=25, y=159, width=950, height=516)
q_title = Label(quiz_page, text="answer these questions", fg=t, bg=f, font=("Courier New", 40))
q_title.place(x=140, y=25)

m_f.tkraise()
root.mainloop()