from tkinter import *
import requests
import random
import html # this turns certain characters in the API into something more readable
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
c_f = ("Courier New", 20)
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
        q_item = html.unescape(i["question"])
        a_right = html.unescape(i["correct_answer"])
        a_wrong = [html.unescape(wrong) for wrong in i["incorrect_answers"]]
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
        c_1.config(text=f"A. {quest["choices"][0]}", fg=t, bg=f, font=c_f)
        c_2.config(text=f"B. {quest["choices"][1]}", fg=t, bg=f, font=c_f)
        c_3.config(text=f"C. {quest["choices"][2]}", fg=t, bg=f, font=c_f)
        c_4.config(text=f"D. {quest["choices"][3]}", fg=t, bg=f, font=c_f)
        feedback.config(text="")
        a.delete(0, END)
    else:
        show_results()

def if_answer_right():
    global current_q, current_score, qs
    if current_q < len(qs):
        user_input = a.get().strip().upper() # takes user's input, makes it uppercase regardless of what is entered
        if user_input in ["A", "B", "C", "D"]:
            a_i = ["A", "B", "C", "D"].index(user_input) # converts to API index
            user_a = qs[current_q]["choices"][a_i]
            right_a = qs[current_q]["correct"]
            if user_a == right_a:
                feedback.config(text="That's right!") # what displays when question is answered correctly
                current_score += 1 # scores add up by 1 point
            else:
                feedback.config(text=f"Correct answer: {right_a}") 
                # if user answers incorrectly, correct answer shown here
        else: 
            feedback.config(text="Please enter a valid letter.") # if user answers something other than choices

def next_q():
    global current_q
    current_q += 1
    load_q()

def show_results():
    result_frame.tkraise()
    score.config(text=f"{current_score}/{len(qs)}") # displays user's score

def replay():
    global current_q, current_score, qs
    current_q = 0
    current_score = 0
    qs = []
    get_data()
    m_f.tkraise() # resets everything and opens beginning frame

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
question =  Label(quiz_page, text="", fg=t, bg=f, font=("Times", 25), wraplength=900, justify="center") # gets configured with the trivia questions
question.place(x=15, y=25)
c_1 = Label(quiz_page, text="A. ", fg=t, bg=f, font=c_f, wraplength=600) # multiple choice
c_1.place(x=20, y=170)
c_2 = Label(quiz_page, text="B. ", fg=t, bg=f, font=c_f, wraplength=600)
c_2.place(x=500, y=170)
c_3 = Label(quiz_page, text="C. ", fg=t, bg=f, font=c_f, wraplength=600)
c_3.place(x=20, y=230)
c_4 = Label(quiz_page, text="D. ", fg=t, bg=f, font=c_f, wraplength=600)
c_4.place(x=500, y=230)

# where user inputs their answer
a = Entry(quiz_page, fg="black", bg="#BFBCCB", width=23, font=b_f) 
a.place(x=140, y=300)
submit = Button(quiz_page, text="check", fg=t, bg=btn, font=("Times", 30), command=if_answer_right) 
submit.place(x=290, y=400)
next = Button(quiz_page, text="next", fg=t, bg=btn, font=("Times", 30), command=next_q)
next.place(x=510, y=400)

# feedback
feedback = Label(quiz_page, text="", fg=t, bg=f, font=("Times", 30))
feedback.place(x=300, y=500)

# result frame
result_frame = Frame(root, bg=r_bg)
result_frame.place(x=25, y=159, width=950, height=616)
score = Label(result_frame, text="10/10", fg=t, bg=r_bg, font=("Courier New", 70))
score.place(x=340, y=50)
reattempt = Button(result_frame, text="Play Again", fg=t, bg=r_bg, font=b_f, command=replay)
reattempt.place(x=330, y=230)
exit = Button(result_frame, text="Quit", fg=t, bg=r_bg, font=b_f, command=quit)
exit.place(x=400, y=390)

get_data()
m_f.tkraise()
root.mainloop()