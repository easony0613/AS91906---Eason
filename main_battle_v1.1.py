'''
Purpose: As time passes by, gamification has become a common thing within the world. 
Gamification is defined as applying game mechanics into a non-game environment, online community, learning management system or business' intranet to increase participation. 
The goal of gamification is to engage with consumers, employees and partners to inspire collaborate, share, and interact. 
Many educational organizations such as Duolingo, Education Perfect, and Brilliant.org has incorporated gamification within their website and app to make learning fun
and it is working very well. I would like to make an educational program with gamification to help users learn while playing the game. 

Writer: Eason Yang
Date: 25/06/24

Version1: Version one of the program will only show the visuals of the boss image, health bars, and where the buttons are. The buttons will not work at this stage. 
'''

from tkinter import*

class MainBattle():
    '''this class will show the main battle interface of the program'''
    def __init__(self):
        global  boss_image1

        # setting up GUI frame
        self.battle_frame = Frame(root, width=10, height=10, bg="#B1DDF0",relief=SOLID, borderwidth=1, padx=5, pady=5)
        self.battle_frame.grid(padx=5, pady=5)

        self.boss_health = Label(self.battle_frame, text="▬▬▬▬▬▬Health bar▬▬▬▬▬▬", fg="red", font=("Arial", "16"))
        self.boss_health.grid(padx=5, pady=5, row=0, sticky="WE")

        image_label = Label(self.battle_frame, image=boss_image1, bg="green")
        image_label.grid(padx=5, pady=5, row=1)

        # feedback message
        mood = "Eason is currently happy"
        self.feedback = Label(self.battle_frame, text=mood, fg="red")
        self.feedback.grid(row=2)

        #player health
        self.player_health = Label(self.battle_frame, text="▬▬▬Health bar▬▬▬", fg="red", font=("Arial", "16"))
        self.player_health.grid(row=3)

        #frame for buttons
        self.button_frame = Frame(self.battle_frame, bg="#FFE6CC", relief=SUNKEN)
        self.button_frame.grid(row=4)

root = Tk()
root.title("Hardest Fight with Eason")
boss_image1 = PhotoImage(file="bossimage1.gif")
root.resizable(0,0)
MainBattle()
root.geometry("800x490")
root.mainloop()
    