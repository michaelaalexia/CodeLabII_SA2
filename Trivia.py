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
q_f = ("Courier New", 40)
b_f = ("Times", 45)

# commands 
def display_page():
    quiz_page.tkraise()

title = Label(root, text="ART TRIVIA", fg=t, bg=b, font=("Times", 64))
title.place(x=270, y=44)

m_f = Frame(root, bg=f)
m_f.place(x=25, y=159, width=950, height=516)
m_b = Button(m_f, text="Begin", fg=t, bg=btn, font=b_f, width=20, command=display_page)
m_b.place(x=150, y=200)

quiz_page = Frame(root, bg=f)
quiz_page.place(x=25, y=159, width=950, height=516)
q_title = Label(quiz_page, text="Answer These Questions", fg=t, bg=f, font=q_f)
q_title.place(x=140, y=25)
question =  Label(quiz_page, text="hello", fg=t, bg=f, font=("Courier New", 30))
question.place(x=140, y=115)
a_1 = Button(quiz_page, fg=t, bg=btn, width=10, font=b_f)
a_1.place(x=100, y=185)
a_2 = Button(quiz_page, fg=t, bg=btn, width=10, font=b_f)
a_2.place(x=540, y=185)
a_3 = Button(quiz_page, fg=t, bg=btn, width=10, font=b_f)
a_3.place(x=100, y=330)
a_4 = Button(quiz_page, fg=t, bg=btn, width=10, font=b_f)
a_4.place(x=540, y=330)

m_f.tkraise()
root.mainloop()