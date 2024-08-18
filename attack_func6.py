from tkinter import*
from functools import partial
import json

'''version 1: displays the quiz window, the questions and the choices can be refreshed, the quiz does not fully work yet

version 2: checking the input of answer, the quiz now works

version 3: answering the question correctly or incorrectly will ask the user to close the quiz window and bring them back to the main window 
with the attack button enabled again.

version 4: The main window will know if the answer is correct or incorrect and display the respective text to the user 

version 5: The quiz now displays the choice with numbers and takes numbers instead of the user typing in the choices
program also does boundary input on the numbers inputted. The quiz window immediately closes as the confirm button is pressed

version 6: The Health bar has been added. The health bars decrease base on the user's answers'''


counter = 1 # setting up the counter variable to count the amount of times the attack function is called
BOSS_PERCENTAGE = 100 # setting up the constant to keep track of the boss health percentage
PLAYER_PERCENTAGE = 100 # setting up the constant to keep track of the player health percentage

class MainBattle():
    '''this class will show the main battle interface of the program'''
    def __init__(self):
        button_width = 12
        button_height = 2
        button_font = ("Arial", "12", "bold")

        self.main_frame = Frame(padx=10, pady=10)
        self.main_frame.grid(row=0)

        self.button_frame = Frame(padx=30, pady=30)
        self.button_frame.grid(row=1)

        self.main_feedback = Label(self.main_frame, text="", font=("Gothic", "15", "bold"))
        self.main_feedback.grid(row=1)

        self.boss_health = Label(self.main_frame, text="♥ ▬▬▬▬100%▬▬▬▬", fg="purple", bg="#221B27", font=("Arial", "20"), relief=SOLID, width=20)
        self.boss_health.grid(row=2, pady=10)

        self.player_health = Label(self.main_frame, text="♥ ▬▬▬▬100%▬▬▬▬", fg="green", bg="#221B27", font=("Arial", "13"), relief=SOLID, width=25)
        self.player_health.grid(row=3)

        self.attack_button = Button(self.button_frame, text="attack", bg="red", width=button_width, height=button_height, font=button_font, relief=SOLID, command=self.to_attack)
        self.attack_button.grid(row=1, column=0, columnspan=2)

    def to_attack(self): 
        '''this method start the attack class and show the user the quiz'''
        Attack(self)
        # the program keep track of the amount of times the attack button is pressed to update the quiz along with the choices
        global counter
        counter +=1
 
class Attack:
    '''this class opens the quiz'''
    def __init__(self, partner):
        self.attack_quiz = Toplevel() # Making a new window but this window will appear on top of the previous window
        background = "#221B27"
        quiz = dict()

        self.partner = partner

        # disable the attack button when clicked on
        partner.attack_button.config(state=DISABLED)

        # if the users press cross at the top, closes attack and releases attack button
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

        self.confirm_button = Button(self.quiz_frame, text="Confirm", bg="#F7B900", fg="black", width=12, height=2, font=("Gothic", "10", "bold"), command= self.confirm_answer)
        self.confirm_button.grid(row=8, pady=5)

        # opening the json file and access the quiz
        with open("quiz.json") as f:
            quiz = json.load(f)

        # with the use of counter, the question and the choices can all change when I change the value of counter. 
        self.quiz_text.config(text=(f"Question{counter} :", quiz[f"question{counter}"]["question"]))

        self.choice_text1.config(text="1." + quiz[f"question{counter}"]["choices"][0])

        self.choice_text2.config(text="2." + quiz[f"question{counter}"]["choices"][1])

        self.choice_text3.config(text="3." + quiz[f"question{counter}"]["choices"][2])

        self.choice_text4.config(text="4." + quiz[f"question{counter}"]["choices"][3])


    def close_attack(self, partner):
        '''put help button back to normal'''
        partner.attack_button.config(state=NORMAL)
        self.attack_quiz.destroy()
    
    def confirm_answer(self):
        '''program checks the user's answer to the answer of the quiz and lets the user know
        if they have gotten the question correct. And ask them to close the window using the cross'''
        with open("quiz.json") as f:
            quiz = json.load(f)

        # getting the user's response
        response = self.answer_entry.get()

        # boundary testing
        if response not in ["1", "2", "3", "4"]:
            self.feedback.config(text="Please enter the number from the choice givern above")
            response = self.answer_entry.get()
         
        else:  # the following number corresponds to the choices from the json file
            if response == "1":
                response = quiz[f"question{counter-1}"]["choices"][0]
            
            elif response == "2":
                response = quiz[f"question{counter-1}"]["choices"][1]
            
            elif response == "3":
                response = quiz[f"question{counter-1}"]["choices"][2]
            
            else:
                response = quiz[f"question{counter-1}"]["choices"][3]

            if response == quiz[f"question{counter-1}"]["answer"]: 
                global BOSS_PERCENTAGE
                self.attack_quiz.destroy()
                self.partner.attack_button.config(state=NORMAL)
                self.partner.main_feedback.config(text="You did 5 damage to Eason!")
                self.partner.boss_health.config(text=f"♥ ▬▬▬▬{BOSS_PERCENTAGE-5}%▬▬▬▬")
                BOSS_PERCENTAGE -= 5


            else: 
                global PLAYER_PERCENTAGE
                self.attack_quiz.destroy()
                self.partner.attack_button.config(state=NORMAL)
                self.partner.main_feedback.config(text="Eason did 20 damage to you!")
                self.partner.player_health.config(text=f"♥ ▬▬▬▬{PLAYER_PERCENTAGE-20}%▬▬▬▬")
                PLAYER_PERCENTAGE -= 20

# main program
root = Tk()
root.title("Hardest Fight with Eason")
MainBattle()
root.mainloop()