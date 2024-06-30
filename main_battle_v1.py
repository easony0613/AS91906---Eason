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
        self.battle_frame = Frame(bg="pink", width=790, height=470)
        self.battle_frame.grid(padx=5, pady=5)

        self.place_holder = Label(self.battle_frame, text="_")
        self.place_holder.grid(row=1, column=0)

        self.battle_heading = Label(self.battle_frame, text="▬▬▬▬▬▬Health bar▬▬▬▬▬▬", fg="red", bg="yellow", font=("Arial", "16"))
        self.battle_heading.grid(padx=5, pady=5, row=0, column=1)

        image_label = Label(self.battle_frame, image=boss_image1, bg="green")
        image_label.grid(padx=5, pady=5, row=1, column=1)



root = Tk()
root.title("Hardest Fight with Eason")
boss_image1 = PhotoImage(file="bossimage1.gif")
root.geometry("800x490")
root.resizable(0,0)
MainBattle()
root.mainloop()
    