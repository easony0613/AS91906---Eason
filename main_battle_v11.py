'''
purpose: creating a quiz themed program that educates students about Eason while providing an epic battle
writer: Eason Yang
date: 24/06/24

version 1: the program will only show the visuals of the boss image, health bars, and where the buttons are. 
The buttons will not work at this stage. 

version 1.1: I have acquired help from online and was able to use some code to create a gradient frame that make 
my program cooler to look at. 

version 1.2: I played around with the gradient frame and see what I could do with it

version 2: I have added the first battle theme of the program. I have also chose the colour theme for phase1 1 of Eason which is purple. 
Sadly, the music does not stop after closing the GUI. 

version 2.1: I have chosen the colour theme for phase1 2 of Eason which is blue and cyan. I made a version to keep track of the 
colour codes

version 2.2: I have chosen the colour theme for phase1 3 of Eason which is dark red and red. I made a version to keep track of the
colour codes

verion 3: Since playsound only has one function which is to only play the sound, I decided to use alternative module which is 
more versatile than playsound. The winsound module allows me to do much more than just play the sound. After downloading the 
winsound module on my command prompt, I have put the code of winsound into my code. A problem I found with winsound is that 
It cannot play MP3 audios. So in order to use winsound, I have to convert my battle theme into a wav file instead of the usual
mp3 file. Even with the incrementation with winsound, the music still playing after the GUI is closed problem still have not been
fixed. In this version I tried the stop function of winsound, after pressing enter on the terminal, the music stops. This may be
useful to me later in my project. 

version 3.1: I made another version to keep the code of stopping winsound in version 3 while I can experiment with other things in
version 3.1. The same problem remains, the sound still plays after the GUI is closed. 

version 4: BIG NEWS. After turning winsound into an attribute by putting self. in front of winsound, the music became a part of 
the GUI. This allows the music to be stopped as soon as the the gui is closed. 

version 4.1: I have improved the aesthetic of the first frame by making the entire first frame purple all the way to the edge of
the window. 

version 4.2: I have to font of the buttons to make the program look more like a game. After evaluating the stakeholder feedback
I have decided to make the top 3 buttons bigger since they are more significant(used more than the other two). After incrementing 
this change, the purple phase1 of my program is being really weird again so I would need to increase the padx to fix it.
Also, for some reason the heart symbol of the health bar disappeared despite it being in the text. 

version 5: To make the program more aesthetically pleasing, I have made the phase1 of both the main frame and the button frame 
all the way to the window. This makes the program look more complete. Not only that, I have made the phase1 of the button frame
from a light orange into a dark purple to create contrast. This make my program look less shiny and make the eyes more comfortable
to look at. I have also integrated the help function into the main program. Now the user can click on the help button if they are
unsure how to use the program. 

version 6: after countless testing and improvement made on the attack function in another file, I have finally finished it and is
able to integrate the attack function into the main battle in this version. Now that the main functionality of the program has 
been added, the program can be tested by others. In this version, I have got rid of the break shield, restore shield, and the
history function since they are no longer needed. I have disabled the attack button while the help button is pressed, to prevent
too many windows. As the game ends, both bottons are disabled so the user can do nothing but to close the program. The game ends
immediately if the user closes the quiz without answering any questions. I have also optimized the wording of the program and
disables another button when one button is pressed to avoid creating multiple windows. 

version 7: in this version I started working on the phase1 of Eason. As Eason's health drop to 50%, his damage doubles. As Eason's
health drop to 25%, his damage doubles again. The program also tells the user when Eason is angry and when Eason is furious. When
Eason does excess damage to the user, the player's health will be 0%. For example, if the player had 40 health when Eason does 80
damage, the player will have 0% health after the attack instead of a -40% health since 40 - 80 = -40. 

version 8: in this version I stated working on changing the colour theme of the GUI as Eason change phases. After this 
implementation, the program looks much much more prettier and engaging. The main window colour can be changed. The help window can
be changed and the quiz window can be changed. 

version 9: in this version I started working on changing the music of the program as Eason change phases. After this implementation,
the program is even more like a a game. Now the soundtrack of any phase will be looped incase the user spends a long time thinking
about the choices and prevent the music from stopping when finished. 

version 10: in this version I started working on changing the iamge of the program as Eason change phases. After this implementation
my program is pretty much done. It looks so funny and everything is working. 

version 11: in this version I started working on the start window and the finish window for my game. I have created the start class 
which calls the main battle class and calls the other classes. I now have a window that welcomes the user and ask them to 
start the game.  I now also have a window that congratulate the user when they win and a window that laugh at the user when they 
lose. My program is now complete
'''
from tkinter import*
from functools import partial
import json
import winsound

BOSS_PERCENTAGE = 100
PLAYER_PERCENTAGE = 100
counter = 1 # setting up the counter variable to count 
# the amount of times the attack function is called
background_counter = 0 # setting up the counter variable the count the amount of times the background changes

# the background of each phase
phase1 = "#221B27"
phase2 = "#12294A"
phase3 = "#400101"

# the background of each phase to be put in the gradient frame(battle frame)
phase1_colour1 = "#4F0575"
phase1_colour2 = "#C3B1E1"
phase2_colour1 = "#014E52"
phase2_colour2 = "#3B8283"
phase3_colour1 = "#5E0202"
phase3_colour2 = "#FFD030"

phase1_boss_hp_colour = "purple"
phase2_boss_hp_colour = "#4575BE"
phase3_boss_hp_colour = "red"


phase1_button_frame_colour = "#431C75"
phase2_button_frame_colour = "#031535"
phase3_button_frame_colour = "#1B0000"

# these variables allows the changed music to keep playing without restarting
change_music = "yes"
change_music2 = "yes"


class Start():
    '''This class will welcome the user and ask them to start the game.'''

    def __init__(self):
        '''Sets up the frame for the starting window. '''
        title_font = ("Gothic", "20", "bold")
        text_font = ("Gothic", "10", "bold")
        button_font = ("Gothic", "15", "bold")

        self.start_frame = Frame(bg=phase1)
        self.start_frame.grid()

        self.start_heading = Label(self.start_frame, text="Welcome to your hardest fight with Eason", 
                                   bg=phase1, font=title_font, fg="white")
        
        self.start_heading.grid(row=0, padx=10, pady=10)

        credit_text = '''Phase 1 song: Suspicious Endeavors - LeviathanMusic

Phase 2 song: Battle against a true warrior - Toby Fox

Phase 3 song: The Army of Minotaur - Makai Symphony  '''
        
        self.credit = Label(self.start_frame, text=credit_text,
                        bg=phase1, font=text_font, justify=CENTER, fg="#F7B900")
        
        self.credit.grid(row=1)

        self.start_image_label = Label(self.start_frame, image=start_image)
        self.start_image_label.grid(row=2, pady=10)

        self.start_button = Button(self.start_frame, text="Start Game",fg="black",
                                   bg="#F7B900", relief=SOLID, font=button_font,
                                   height=2, width=20, command=self.start_battle)
        
        self.start_button.grid(row=3, padx=10, pady=10)
    
    def start_battle(self):
        '''This method starts the battle.'''

        self.start_frame.destroy()
        MainBattle()


'''From https://github.com/JeanExtreme002/GradientFrame-Tkinter/blob/master/GradientFrame.py'''
class GradientFrame(Canvas):
    '''this gives me a gradient frame'''

    global background_counter

    """
    Widget with gradient colors.
    """

    __tag = "GradientFrame"
    __hex_format = "#%04x%04x%04x"
    
    top2bottom = 1
    left2right = 2

    def __init__(self, parent, colors = ("", ""), direction = left2right, **kw):

        # Caso o usuário não tenha configurado uma geometria, será definido uma geometria padrão.
        kw["height"] = kw.get("height", 400)
        kw["width"] = kw.get("width", 400)
        
        # Chama o método construtor do Canvas.
        super().__init__(parent, **kw)

        # Instancia os parâmetros.
        self.__geometry = [kw["width"], kw["height"]]
        self.__colors = colors
        self.__direction = direction

        # Desenha o degradê no Canvas.
        self.__draw_gradient()
        
    def __draw_gradient(self):
        
        """
        Paint the Canvas with gradient colors.
        """

        # Apaga o degradê do Canvas.
        self.delete(self.__tag)

        # Recebe o limite de largura.
        limit = self.__geometry[0] if self.__direction == self.left2right else self.__geometry[1]
       
        # Recebe os valores RGB das cores.
        red1, green1, blue1 = self.winfo_rgb(self.__colors[0])
        red2, green2, blue2 = self.winfo_rgb(self.__colors[1])

        # Calcula os valores RGB de acréscimo de cores (Ex: while red1 != red2: red1 += r_ratio) 
        # dividindo o mesmo pelo limite de largura.
        r_ratio = (red2 - red1) / limit
        g_ratio = (green2 - green1) / limit
        b_ratio = (blue2 - blue1) / limit

        for pixel in range(limit):
            
            # Calcula a cor em formato RGB.
            red = int(red1 + (r_ratio * pixel))
            green = int(green1 + (g_ratio * pixel))
            blue = int(blue1 + (b_ratio * pixel))

            # Converte a cor de RGB para Hex.
            color = self.__hex_format % (red, green, blue)

            # Define as posições (x1, y1, x2, y2) do objeto.
            x1 = pixel if self.__direction == self.left2right else 0
            y1 = 0 if self.__direction == self.left2right else pixel
            x2 = pixel if self.__direction == self.left2right else self.__geometry[0]
            y2 = self.__geometry[1] if self.__direction == self.left2right else pixel

            # Cria uma linha no canvas com uma das cores do degradê.
            self.create_line(x1, y1, x2, y2, tag = self.__tag, fill = color)

        # Coloca o degradê atrás de todos os elementos do Canvas.
        self.tag_lower(self.__tag)

    def config(self, cnf = None, **kw):

        # Configura as cores do degradê.
        if "colors" in kw and len(kw["colors"]) > 1:
            self.__colors = kw.pop("colors")

        # Configura a direção do degradê.
        if "direction" in kw and kw["direction"] in (self.left2right, self.top2bottom):
            self.__direction = kw.pop("direction")

        # Configura a altura do degradê.  
        if "height" in kw:
            self.__geometry[1] = kw["height"]

        # Configura a largura do degradê.
        if "width" in kw:
            self.__geometry[0] = kw["width"]

        # Configura o Canvas e desenha o degradê.
        super().config(cnf, **kw)
        self.__draw_gradient()

    def configure(self, cnf = None, **kw):
        self.config(cnf, **kw)


class MainBattle():
    '''This class will show the main battle interface of the program.'''

    def __init__(self):
        '''Sets up the frame for the main battle window. '''
        global background_counter

        # the attack button will be wider so I have made a variable to assign to make it wider
        important_button_width = 30
        button_width = 15
        button_height = 2

        # font for button and text
        button_font = ("Gothic", "15", "bold")
        text_font = ("Gothic", "12", "bold")
        
        # setting up the main frame
        self.main_frame = Frame(bg=phase1, padx=130)
        self.main_frame.grid(sticky="SWE")
        
        # setting up GUI frame
        self.battle_frame = GradientFrame(self.main_frame, 
                                          colors=(phase1_colour1, phase1_colour2),
                                          relief=SOLID, borderwidth=2)
        
        self.battle_frame.grid(padx=60, row=0)

        # boss health
        self.boss_health = Label(self.battle_frame, text="♥ ▬▬▬▬100%▬▬▬▬", fg=phase1_boss_hp_colour, 
                                 bg=phase1, font=("Arial", "20"), relief=SOLID, width=20)
        
        self.boss_health.grid(padx=5, pady=5, row=1)

        # boss image
        self.image_label = Label(self.battle_frame, image=boss_image1, bg=phase1_boss_hp_colour)
        self.image_label.grid(padx=5, pady=5, row=2)

        # feedback message
        self.main_feedback = Label(self.battle_frame, text="Eason is currently happy", fg="red", 
                                   bg="#C3B1E1", font=text_font, wraplength=300)
        
        self.main_feedback.grid(row=3)

        # player health
        self.player_health = Label(self.battle_frame, text="♥ ▬▬▬▬100%▬▬▬▬", fg="green",
                                    bg=phase1, font=("Arial", "13"), relief=SOLID, width=25)
        
        self.player_health.grid(row=4)

        # frame for buttons
        self.button_frame = Frame(bg=phase1_button_frame_colour, relief=SOLID,
                                  borderwidth=2, padx=180, pady=2)
        self.button_frame.grid(row=5)

        self.attack_button = Button(self.button_frame, text="Attack", bg="red",
                                    width=important_button_width,
                                     height=button_height, font=button_font, relief=SOLID, command=self.to_attack)
        
        self.attack_button.grid(row=0, padx=5, pady=5)


        self.help_button = Button(self.button_frame, text="Help / Info", bg="Orange",
                                  width=button_width, 
                                  height=button_height, font=button_font, relief=SOLID, command=self.to_help)
        
        self.help_button.grid(row=1)

        self.music = winsound.PlaySound("phase1song.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
        # if we don't have async then any code after the music will not be played. # it is similar to threading. 
    

    def to_help(self):
        '''Calls the displayhelp class.'''

        DisplayHelp(self)
            

    def to_attack(self):
        '''Calls the attack class.'''


        Attack(self)
        # the program keep track of the amount of times the attack button is pressed to update the quiz along with the choices
        global counter
        counter +=1


class DisplayHelp:
    '''This class create the help window pop up.'''

    def __init__(self, partner):
        '''Sets up the frame for the help window'''

        # making a new window on top of an existing window
        self.help_box = Toplevel() 

        # background counter to indicate when to change background
        global background_counter 

        # disable the help button when clicked on
        partner.help_button.config(state=DISABLED)
        partner.attack_button.config(state=DISABLED)

        # if the users press cross at the top, closes help and releases help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300, height=200, bg=phase1)

        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame, bg=phase1, text="Help / Info",
                                        font=("Arial", "14", "bold"), fg="white")

        self.help_heading_label.grid(row=0)

        help_text = '''     Press the attack button to attack the boss. After pressing the attack button, you will be shown a quiz. 

        Getting the question of the quiz correct will damage the boss, while getting the question of the quiz incorrect will result
            in your taking huge damage. 
            
        Once the boss reaches a certain HP, he becomes angry and later become furious. He double's his damage
            each time he changes phase1. 
            
        This means that you must try to get as much question right as possible. One wrong step is all it takes
            for Eason to eat you alive. Good luck!
                '''
        
        self.help_text_label = Label(self.help_frame, bg=phase1, text=help_text,
                                     wraplength=350, justify=CENTER, fg="white")

        self.help_text_label.grid(row=1, padx=10, pady=10)

        self.dismiss_button = Button(self.help_frame, font=("Arial", "12", "bold"), text="Dismiss", 
                                     bg="#CC6600", fg="white", command=partial(self.close_help, partner))

        self.dismiss_button.grid(row=2, padx=10, pady=10)

        # if the background counter is 0, nothing happens
        if background_counter == 0: 
            pass

        # if the background counter is 1, the help window will change into the colour theme of phase 2
        elif background_counter == 1: 
            self.help_frame.config(bg=phase2)
            self.help_heading_label.config(bg=phase2)
            self.help_text_label.config(bg=phase2)

        else: 
            self.help_frame.config(bg=phase3) 
            self.help_heading_label.config(bg=phase3)
            self.help_text_label.config(bg=phase3)


    # closes the help dialogue(used by the cross and the dismiss button) 
    def close_help(self, partner):
        '''This method closes help window.'''

        # put help button back to normal
        partner.help_button.config(state=NORMAL)
        partner.attack_button.config(state=NORMAL)
        self.help_box.destroy()


class Attack:
    '''This class opens the quiz.'''

    def __init__(self, partner):
        '''Sets up the frame for the quiz window. '''

        # making a new window but this window will appear on top of the previous window
        self.attack_quiz = Toplevel() 

        # creating a dictionary to hold the json file
        quiz = dict()

        self.partner = partner

        # user cannot change the size of the window
        self.attack_quiz.resizable(0,0)

        # if the users press cross at the top, closes the quiz and disabled attack button
        self.attack_quiz.protocol('WM_DELETE_WINDOW', partial(self.close_attack, partner))

        # disable the attack button when clicked on
        self.disable_button()

        # making the frame for the quiz questions and choices
        self.quiz_frame = Frame(self.attack_quiz, width=300, height=200, bg=phase1)

        self.quiz_frame.grid()

        # the heading of the quiz window
        self.quiz_heading = Label(self.quiz_frame, bg=phase1, text="Eason's Quiz",
                                  font=("Gothic", "15", "bold"), fg="white")

        self.quiz_heading.grid(row=0)

        # the question of the quiz
        self.quiz_text = Label(self.quiz_frame, bg=phase1, text="",
                               font=("Gothic", "15", "bold"), fg="white")

        self.quiz_text.grid(row=1)

        # the choices of the question
        self.choice_text1 = Label(self.quiz_frame, bg=phase1, text="", 
                                  font=("Gothic", "15", "bold"), fg="white")
        
        self.choice_text1.grid(row=2, pady=2)

        self.choice_text2 = Label(self.quiz_frame, bg=phase1, text="",
                                  font=("Gothic", "15", "bold"), fg="white")
        
        self.choice_text2.grid(row=3, pady=2)

        self.choice_text3 = Label(self.quiz_frame, bg=phase1, text="",
                                  font=("Gothic", "15", "bold"), fg="white")
        
        self.choice_text3.grid(row=4, pady=2)

        self.choice_text4 = Label(self.quiz_frame, bg=phase1, text="",
                                  font=("Gothic", "15", "bold"), fg="white")
        
        self.choice_text4.grid(row=5, pady=2)

        self.feedback = Label(self.quiz_frame, bg=phase1, 
                              text="Please enter your number of choice in the box below", 
                              font=("Gothic", "10", "bold"), fg="green")
        self.feedback.grid(row=6)

        # the entry box for the user to type in the answer of the question
        self.answer_entry = Entry(self.quiz_frame, font=("Arial", "14"), fg="red")
        self.answer_entry.grid(row=7, pady=2)

        # the button for the answer to confirm and submit their answer
        self.confirm_button = Button(self.quiz_frame, text="Confirm", bg="#F7B900", fg="black",
                                     width=12, height=2, font=("Gothic", "10", "bold"), command= self.confirm_answer)
        
        self.confirm_button.grid(row=8, pady=5)

        # if background counter is not one yet, then no background will be changed
        if background_counter == 0: 
            pass

        # when the background counter is 1, everything in the attack window will be changed into the theme of phase 2
        elif background_counter == 1: 
            self.quiz_frame.config(bg=phase2) 
            self.quiz_heading.config(bg=phase2, fg=phase2_boss_hp_colour)
            self.choice_text1.config(bg=phase2, fg=phase2_boss_hp_colour)
            self.choice_text2.config(bg=phase2, fg=phase2_boss_hp_colour)
            self.choice_text3.config(bg=phase2, fg=phase2_boss_hp_colour)
            self.choice_text4.config(bg=phase2, fg=phase2_boss_hp_colour)
            self.quiz_text.config(bg=phase2, fg=phase2_boss_hp_colour)
            self.feedback.config(bg=phase2)

        # when the background counter is more than 1, everything in the attack window will be changed into theme of phase 3
        else:
            self.quiz_frame.config(bg=phase3)
            self.quiz_heading.config(bg=phase3, fg=phase3_boss_hp_colour)
            self.choice_text1.config(bg=phase3, fg=phase3_boss_hp_colour)
            self.choice_text2.config(bg=phase3, fg=phase3_boss_hp_colour)
            self.choice_text3.config(bg=phase3, fg=phase3_boss_hp_colour)
            self.choice_text4.config(bg=phase3, fg=phase3_boss_hp_colour)
            self.quiz_text.config(bg=phase3, fg=phase3_boss_hp_colour)
            self.feedback.config(bg=phase3)


        # opening the json file and access the quiz
        with open("quiz.json") as f:
            quiz = json.load(f)

        # with the use of counter, the question and the choices can all change when I change the value of counter. 
        self.quiz_text.config(text=(f"Question{counter} :", quiz[f"question{counter}"]["question"]))

        self.choice_text1.config(text="1." + quiz[f"question{counter}"]["choices"][0])

        self.choice_text2.config(text="2." + quiz[f"question{counter}"]["choices"][1])

        self.choice_text3.config(text="3." + quiz[f"question{counter}"]["choices"][2])

        self.choice_text4.config(text="4." + quiz[f"question{counter}"]["choices"][3])


    def restore_button(self):
        '''Restores the buttons back to normal.'''

        self.partner.attack_button.config(state=NORMAL)
        self.partner.help_button.config(state=NORMAL)


    def disable_button(self):
        '''Disables the buttons.'''

        self.partner.attack_button.config(state=DISABLED)
        self.partner.help_button.config(state=DISABLED)


    def close_attack(self, partner):
        '''Immediately ends the game if the user clicks on the cross.'''

        self.disable_button()
        partner.main_feedback.config(text="You cheated by not answering any question. Game over, you lose")
        partner.player_health.config(text="♥ ▬▬▬▬0%▬▬▬▬")
        winsound.PlaySound(None,0)
        self.attack_quiz.destroy()


    def change_background(self):
        '''Change the background of the program. '''

        # if changing background is not 1 yet, then nothing happens
        if background_counter == 0: 
            pass

        # once background counter has gone up, everything in the program will be changed into phase 2 colours and image
        elif background_counter == 1: 
            self.partner.main_frame.config(bg=phase2)
            self.partner.boss_health.config(bg=phase2)
            self.partner.player_health.config(bg=phase2)
            self.partner.battle_frame.config(colors=(phase2_colour1, phase2_colour2))
            self.partner.boss_health.config(fg=phase2_boss_hp_colour)
            self.partner.image_label.config(bg=phase2_boss_hp_colour)
            self.partner.button_frame.config(bg=phase2_button_frame_colour)
            self.partner.image_label.config(image=boss_image2)
            
        # when the background increase again, everything in the program will be changed into phase 3 colours and image
        else: 
            self.partner.main_frame.config(bg=phase3) 
            self.partner.boss_health.config(bg=phase3)
            self.partner.player_health.config(bg=phase3)
            self.partner.battle_frame.config(colors=(phase3_colour1, phase3_colour2))
            self.partner.boss_health.config(fg=phase3_boss_hp_colour)
            self.partner.image_label.config(bg=phase3_boss_hp_colour)
            self.partner.button_frame.config(bg=phase3_button_frame_colour)
            self.partner.image_label.config(image=boss_image3)
    

    def confirm_answer(self):
        '''Program checks the user's answer to the answer of the quiz and lets the user know
        if they have gotten the question correct. And ask them to close the window using the cross.'''

        with open("quiz.json") as f:
            quiz = json.load(f)

        # getting the user's response
        response = self.answer_entry.get()

        # boundary testing
        if response not in ["1", "2", "3", "4"]:
            self.feedback.config(text="Please enter the number from the choice givern above")
            response = self.answer_entry.get()
        
        else: 
            if response == "1":
                response = quiz[f"question{counter-1}"]["choices"][0]
            
            elif response == "2":
                response = quiz[f"question{counter-1}"]["choices"][1]
            
            elif response == "3":
                response = quiz[f"question{counter-1}"]["choices"][2]
            
            else:
                response = quiz[f"question{counter-1}"]["choices"][3]

            if response == quiz[f"question{counter-1}"]["answer"]: # if the response is the same as the answer then the player does damage to the boss
                global BOSS_PERCENTAGE
                global background_counter
                global change_music
                global change_music2

                if BOSS_PERCENTAGE > 50:
                    # immediately closes the quiz window
                    self.attack_quiz.destroy() 

                    # the buttons in the main program will be back to normal
                    self.restore_button() 

                    # updating and showing the new boss HP
                    self.partner.main_feedback.config(text="Correct answer! You did 5 damage to Eason!") 
                    self.partner.boss_health.config(text=f"♥ ▬▬▬▬{BOSS_PERCENTAGE-5}%▬▬▬▬")
                    BOSS_PERCENTAGE -= 5

                # when the boss reach between 50 and 26 HP, the phase changes
                elif BOSS_PERCENTAGE <= 50 and BOSS_PERCENTAGE > 25: 
                    background_counter = 1 

                    # if change music is yes, then music change into phase 2 music
                    if change_music == "yes": 
                        winsound.PlaySound("phase2song.wav", winsound.SND_ASYNC + winsound.SND_LOOP)

                    # change phase
                    self.change_background()
                    self.attack_quiz.destroy()
                    self.restore_button()
                    self.partner.main_feedback.config(text="Correct answer! You did 5 damage to Eason!")
                    self.partner.boss_health.config(text=f"♥ ▬▬▬▬{BOSS_PERCENTAGE-5}%▬▬▬▬")
                    BOSS_PERCENTAGE -= 5

                    # changing it to no so the phase2 music does not get played aagain when the user answer again
                    change_music = "no" 

                # when the boss reaches below 25hp, the phase change again
                else: 
                    background_counter = 2
                    if change_music2 == "yes":
                        winsound.PlaySound("phase3song.wav", winsound.SND_ASYNC + winsound.SND_LOOP)

                    self.change_background()
                    self.attack_quiz.destroy()
                    self.restore_button()
                    self.partner.main_feedback.config(text="Correct answer! You did 5 damage to Eason!")
                    self.partner.boss_health.config(text=f"♥ ▬▬▬▬{BOSS_PERCENTAGE-5}%▬▬▬▬")
                    BOSS_PERCENTAGE -= 5
                    change_music2 = "no"

                    # when the boss's health reach 0 hp, all the window closes and the window congratulating the user will show up
                    if BOSS_PERCENTAGE <=0: 
                        self.attack_quiz.destroy()
                        self.partner.main_frame.destroy()
                        self.partner.button_frame.destroy()
                        Win()

            else:
                global PLAYER_PERCENTAGE

                # while the health of the boss is still more the 50, the boss only does 20 damage
                if BOSS_PERCENTAGE > 50: 
                    self.attack_quiz.destroy()
                    self.restore_button()
                    self.partner.main_feedback.config(text="Wrong answer, Eason did 20 damage to you!")
                    self.partner.player_health.config(text=f"♥ ▬▬▬▬{PLAYER_PERCENTAGE-20}%▬▬▬▬")
                    PLAYER_PERCENTAGE -= 20

                    # if the player's health reaches 0 or less than zero after the boss attack
                    # the player loses and the window laughing at the user will show up
                    if PLAYER_PERCENTAGE <=0: 
                        self.attack_quiz.destroy()
                        self.partner.main_frame.destroy()
                        self.partner.button_frame.destroy()
                        Lose()

                # if the health of the boss is below 50 and more than 25, the boss now does 40 damage
                elif BOSS_PERCENTAGE <= 50 and BOSS_PERCENTAGE > 25: 
                    self.attack_quiz.destroy()
                    self.restore_button()
                    self.partner.main_feedback.config(text="Eason is now angry, Eason did 40 damage to you!")
                    self.partner.player_health.config(text=f"♥ ▬▬▬▬{PLAYER_PERCENTAGE-40}%▬▬▬▬")
                    PLAYER_PERCENTAGE -= 40
                    
                    if PLAYER_PERCENTAGE <=0:
                        self.attack_quiz.destroy()
                        self.partner.main_frame.destroy()
                        self.partner.button_frame.destroy()
                        Lose()
            
                else:
                    # if the health of the boss reaches below 25, the boss now does 80 damage
                    self.attack_quiz.destroy() 
                    self.restore_button()
                    self.partner.main_feedback.config(text="Eason is now furious, Eason did 80 damage to you!")
                    self.partner.player_health.config(text=f"♥ ▬▬▬▬{PLAYER_PERCENTAGE-80}%▬▬▬▬")
                    PLAYER_PERCENTAGE -= 80

                    if PLAYER_PERCENTAGE <= 0:
                        self.attack_quiz.destroy()
                        self.partner.main_frame.destroy()
                        self.partner.button_frame.destroy()
                        Lose()


class Win():
    '''This class will show a window congratulating the user when they win.'''

    def __init__(self):
        '''Sets up the frame for the winning window. '''

        title_font = ("Gothic", "20", "bold")
        text_font = ("Gothic", "10", "bold")

        self.win_frame = Frame(bg="#006B1E")
        self.win_frame.grid()

        self.win_heading = Label(self.win_frame, text="YOU WON!", bg="#006B1E", font=title_font, fg="#F7B900")
        self.win_heading.grid(row=0, padx=5, pady=10)

        self.win_text = Label(self.win_frame, 
                              text="YOU MUST HAVE CHEATED. HOW DID YOU BEAT THE COOLEST PERSON IN THE WORLD??!", 
                              font=text_font, bg="#006B1E", fg="#F7B900")
        
        self.win_text.grid(row=1, padx=5, pady=10)

        self.win_image = Label(self.win_frame, image=win_image, bg="#006B1E")
        self.win_image.grid(row=2, padx=5, pady=10)

        self.instruction = Label(self.win_frame, 
                                 text="You can close the window now", 
                                 font=text_font, fg="white", bg="#006B1E")
        
        self.instruction.grid(row=3, padx=5, pady=10)

        self.win_noise = winsound.PlaySound("Dying noise.wav", winsound.SND_ASYNC)


class Lose():
    '''This class will show a window laughing at the user when they lose.'''

    def __init__(self):
        '''Sets up the frame for the losing window. '''
        
        title_font = ("Gothic", "20", "bold")
        text_font = ("Gothic", "10", "bold")

        self.lose_frame = Frame(bg="#56575C")
        self.lose_frame.grid()

        self.lose_heading = Label(self.lose_frame, text="YOU LOST!", 
                                  bg="#56575C", font=title_font, fg="#F7B900")
        
        self.lose_heading.grid(row=0, padx = 5, pady=10)

        self.lose_text = Label(self.lose_frame,
                               text="YOU CANNOT BEAT THE COOLEST PERSON IN THE WORLD HAHAHAHAHAHA!!!",
                               font=text_font, bg="#56575C", fg="#F7B900")
        
        self.lose_text.grid(row=1, padx=5, pady=10)

        self.lose_image = Label(self.lose_frame, image=loss_image, bg="#56575C")
        self.lose_image.grid(row=2, padx=5, pady=10)

        self.instruction = Label(self.lose_frame, text="You can close the window now",
                                font=text_font, fg="white", bg="#56575C")
        
        self.instruction.grid(row=3, padx=5, pady=10)

        self.lose_noise = winsound.PlaySound("Laughing noise.wav", winsound.SND_ASYNC)


root = Tk()
root.title("Hardest Fight with Eason")
start_image = PhotoImage(file="startimage.gif")
boss_image1 = PhotoImage(file="bossimage1.gif")
boss_image2 = PhotoImage(file="bossimage2.gif")
boss_image3 = PhotoImage(file="bossimage3.gif")
win_image = PhotoImage(file="Dying image.gif")
loss_image = PhotoImage(file="Laughing image.gif")

# the user cannot resize the window
root.resizable(0,0)
Start()
root.mainloop()