from tkinter import*
from functools import partial
import json

'''version 1: displays the quiz window, the questions and the choices can be refreshed, the quiz does not fully work yet'''

counter = 1 # setting up the counter variable to count the amount of times the attack function is called

class MainBattle():
    def __init__(self):
        button_width = 12
        button_height = 2
        button_font = ("Arial", "12", "bold")

        self.main_frame = Frame(bg="#221B27", padx=10, pady=10)
        self.main_frame.grid()

        self.button_frame = Frame(padx=30, pady=30)
        self.button_frame.grid(row=0)

        self.main_feedback = Label(self.main_frame, text="", font=("Gothic", "15", "bold"))
        self.main_feedback.grid(row=1)

        self.attack_button = Button(self.button_frame, text="attack", bg="red", width=button_width, height=button_height, font=button_font, relief=SOLID, command=self.to_attack)
        self.attack_button.grid(row=2, column=0, columnspan=2)

    def to_attack(self):
        Attack(self)
        global counter
        counter +=1
 
class Attack:
    def __init__(self, partner):
        self.attack_quiz = Toplevel() # Making a new window but this window will appear on top of the previous window
        background = "#221B27"
        quiz = dict()

        # disable the help button when clicked on
        partner.attack_button.config(state=DISABLED)

        # if the users press cross at the top, closes help and releases help button
        self.attack_quiz.protocol('WM_DELETE_WINDOW', partial(self.close_attack, partner))

        # Making the frame for the quiz questions and choices
        self.quiz_frame = Frame(self.attack_quiz, width=300, height=200, bg=background)

        self.quiz_frame.grid()

        # the heading of the quiz window
        self.quiz_heading = Label(self.quiz_frame, bg=background, text="Eason's Quiz", font=("Gothic", "15", "bold"), fg="white")

        self.quiz_heading.grid(row=0)

        # the question of the quiz
        self.quiz_text = Label(self.quiz_frame, bg=background, text="", font=("Gothic", "15", "bold"), fg="white")

        self.quiz_text.grid(row=1)

        # the choices of the question
        self.choice_text1 = Label(self.quiz_frame, bg=background, text="", font=("Gothic", "15", "bold"), fg="white")
        self.choice_text1.grid(row=2, pady=2)

        self.choice_text2 = Label(self.quiz_frame, bg=background, text="", font=("Gothic", "15", "bold"), fg="white")
        self.choice_text2.grid(row=3, pady=2)

        self.choice_text3 = Label(self.quiz_frame, bg=background, text="", font=("Gothic", "15", "bold"), fg="white")
        self.choice_text3.grid(row=4, pady=2)

        self.choice_text4 = Label(self.quiz_frame, bg=background, text="", font=("Gothic", "15", "bold"), fg="white")
        self.choice_text4.grid(row=5, pady=2)

        self.feedback = Label(self.quiz_frame, bg=background, text="Please enter your answer in the box below", font=("Gothic", "10", "bold"), fg="green")
        self.feedback.grid(row=6)

        # the entry box for the user to type in the answer of the question
        self.answer_entry = Entry(self.quiz_frame, font=("Arial", "14"), fg="red")
        self.answer_entry.grid(row=7, pady=2)

        self.confirm_button = Button(self.quiz_frame, text="Confirm", bg="#F7B900", fg="black", width=12, height=2, font=("Gothic", "10", "bold"))
        self.confirm_button.grid(row=8, pady=5)

        # opening the json file and access the quiz
        with open("quiz.json") as f:
            quiz = json.load(f)

        # with the use of counter, the question and the choices can all change when I change the value of counter. 
        self.quiz_text.config(text=(f"Question{counter} :", quiz[f"question{counter}"]["question"]))

        self.choice_text1.config(text=quiz[f"question{counter}"]["choices"][0])

        self.choice_text2.config(text=quiz[f"question{counter}"]["choices"][1])

        self.choice_text3.config(text=quiz[f"question{counter}"]["choices"][2])

        self.choice_text4.config(text=quiz[f"question{counter}"]["choices"][3])


        # closes the attack window(used by the cross and the dismiss button) 

    def close_attack(self, partner):
        '''put help button back to normal'''
        partner.attack_button.config(state=NORMAL)
        self.attack_quiz.destroy()
    



root = Tk()
root.title("Hardest Fight with Eason")
MainBattle()
root.mainloop()