from tkinter import*
from functools import partial

class MainBattle():
    def __init__(self):
        button_width = 12
        button_height = 2
        button_font = ("Arial", "12", "bold")

        self.main_frame = Frame(bg="#221B27", padx=10, pady=10)
        self.main_frame.grid()

        self.button_frame = Frame(padx=30, pady=30)
        self.button_frame.grid(row=0)

        self.help_button = Button(self.button_frame, text="Help / Info", bg="Orange", width=button_width, height=button_height, font=button_font, relief=SOLID, command=self.to_help)
        self.help_button.grid(row=1, column=0, columnspan=2)

    def to_help(self):
        DisplayHelp(self)


class DisplayHelp:
    def __init__(self, partner):
        self.help_box = Toplevel() # ig this is similar to root = Tk(). Making a new window but instead the window is created to the self.help_box within the class
        background = "#ffe6cc"

        # disable the help button when clicked on
        partner.help_button.config(state=DISABLED)

        # if the users press cross at the top, closes help and releases help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300, height=200, bg=background)

        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame, bg=background, text="Help / Info", font=("Arial", "14", "bold"))

        self.help_heading_label.grid(row=0)

        help_text = '''You can choose between attacking, restoring shield, or breaking shield to make actions. While the boss shield is up, you deal reduced damage to the boss. While your shield is up, you take no damage from the boss. You do not start with a shield, therefore you need to restore one

        Attacking: after pressing the attack button, you will be asked a question and you have to select from the four options that appear. If you get the question correct, you do random damage to the boss and skip his turn. If you get it wrong, your shield will break and the boss starts deaking damage to you. 

        Break shield: after pressing the break shield button, you will be asked to select a number between 1 and 10. If you fail to guess the boss shield, you still lose your turn and the bosss attacks you. However you now do 2x damage. 
        
        Restore shield: after pressing the button, you will be asked to select a number betwwen 1 and 10 to act as your new shield for boss to guess. Howeveer resotring your shield loses your turn and the boss will do damage to you while you restore'''

        self.help_text_label = Label(self.help_frame, bg=background, text=help_text, wraplength=350, justify="left")

        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame, font=("Arial", "12", "bold"), text="Dismiss", bg="#CC6600", fg="white", command=partial(self.close_help, partner))

        self.dismiss_button.grid(row=2, padx=10, pady=10)

    # closes the help dialogue(used by the cross and the dismiss button) 
    def close_help(self, partner):
        # put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

root = Tk()
root.title("Hardest Fight with Eason")
MainBattle()
root.mainloop()