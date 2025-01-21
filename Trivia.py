from tkinter import *
import requests
import random
root = Tk()
root.title("Art Trivia !")
root.geometry("1000x800")
root.resizable(0, 0)
root["bg"] = "black" # TK window

# variables for quick access 
b = "black"
f = "#9B6A6C"
btn = "#E75A7C"
t = "#F3E9DC"
r_bg = "#4C4C9D"
url = "https://opentdb.com/api.php?amount=10&category=25&difficulty=easy&type=multiple"
q_f = ("Courier New", 30)
c_f = ("Courier New", 25)
b_f = ("Times", 45)

# variables for commands
qs = []
current_q = 0
current_score = 0 # these are the default values for the quiz, users' current status upon opening the program

# commands 

# fetch data from API
def get_data():
    global qs # so it's accessible anywhere
    r = requests.get(url)
    data = r.json()
    result = data["results"]
    for i in result:
        q_item = i["question"]
        a_right = i["correct_answer"]
        a_wrong = i["incorrect_answers"]
        choices = a_wrong + [a_right]
        random.shuffle(choices)
        qs.append({
            "question" : q_item,
            "correct" : a_right,
            "choices" : choices
        })

def display_page():
    quiz_page.tkraise()
    title.config(text="Type the letter of the correct answer", font=("Times", 40))
    title.place(x=110, y=44)
    load_q()

def load_q():
    global current_q, qs
    if current_q < len(qs):
        quest = qs[current_q]
        question.config(text=quest["question"])
        c_1.config(text=quest["choices"][0], fg=t, bg=f, font=c_f)
        c_2.config(text=quest["choices"][1], fg=t, bg=f, font=c_f)
        c_3.config(text=quest["choices"][2], fg=t, bg=f, font=c_f)
        c_4.config(text=quest["choices"][3], fg=t, bg=f, font=c_f)
        feedback.config(text="")
        a.delete(0, END)
    else:
        show_results()

def if_answer_right():
    global current_q, current_score, qs
    if current_q < len(qs):
        user_input = a.get().strip().upper() # takes user's input


def replay():
    m_f.tkraise()
def quit():
    root.destroy()

# title frame 
title = Label(root, text="ART TRIVIA", fg=t, bg=b, font=("Times", 64))
title.place(x=270, y=44)
m_f = Frame(root, bg=f)
m_f.place(x=25, y=159, width=950, height=616)
m_b = Button(m_f, text="Begin", fg=t, bg=btn, font=b_f, width=20, command=display_page)
m_b.place(x=150, y=200)

# quiz frame
quiz_page = Frame(root, bg=f)
quiz_page.place(x=25, y=159, width=950, height=616)
question =  Label(quiz_page, text="", fg=t, bg=f, font=("Times", 27)) # gets configured with the trivia questions
question.place(x=30, y=25)
c_1 = Label(quiz_page, text="A. ", fg=t, bg=f, font=c_f) # multiple choice
c_1.place(x=140, y=170)
c_2 = Label(quiz_page, text="B. ", fg=t, bg=f, font=c_f)
c_2.place(x=500, y=170)
c_3 = Label(quiz_page, text="C. ", fg=t, bg=f, font=c_f)
c_3.place(x=140, y=230)
c_4 = Label(quiz_page, text="D. ", fg=t, bg=f, font=c_f)
c_4.place(x=500, y=230)

# where user inputs their answer
a = Entry(quiz_page, fg="black", bg="#BFBCCB", width=23, font=b_f) 
a.place(x=140, y=300)
submit = Button(quiz_page, text="submit", fg=t, bg=btn, font=("Times", 30)) 
submit.place(x=390, y=400)
next = Button(quiz_page, text="next", fg=t, bg=btn, font=("Times", 30))
next.place(x=410, y=500)

# feedback
feedback = Label(quiz_page, text="", fg=t, bg=f, font=("Times", 30))
feedback.place(x=380, y=500)

# result frame
result_frame = Frame(root, bg=r_bg)
result_frame.place(x=25, y=159, width=950, height=616)
score = Label(result_frame, text="10/10", fg=t, bg=r_bg, font=("Courier New", 70))
score.place(x=340, y=50)
reattempt = Button(result_frame, text="Play Again", fg=t, bg=r_bg, font=b_f, command=replay)
reattempt.place(x=330, y=230)
exit = Button(result_frame, text="Quit", fg=t, bg=r_bg, font=b_f, command=quit)
exit.place(x=400, y=390)

m_f.tkraise()
root.mainloop()