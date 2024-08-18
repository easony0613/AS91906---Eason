from tkinter import*
import winsound
'''version 1: the program will only show the visuals of the boss image, health bars, and where the buttons are. 
The buttons will not work at this stage. 

version 1.1: I have acquired help from online and was able to use some code to create a gradient frame that make 
my program cooler to look at. 

version 1.2: I played around with the gradient frame and see what I could do with it

version 2: I have added the first battle theme of the program. I have also chose the colour theme for phase 1 of Eason which is purple. 
Sadly, the music does not stop after closing the GUI. 

version 2.1: I have chosen the colour theme for phase 2 of Eason which is blue and cyan. I made a version to keep track of the 
colour codes

version 2.2: I have chosen the colour theme for phase 3 of Eason which is dark red and red. I made a version to keep track of the
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
the GUI. This allows the music to be stopped as soon as the the gui is closed. The GUI still does not look pleasant since there
are white blocks near the edge of the first frame.  

'''

'''From https://github.com/JeanExtreme002/GradientFrame-Tkinter/blob/master/GradientFrame.py'''
class GradientFrame(Canvas):
    
    """
    Widget with gradient colors.
    """

    __tag = "GradientFrame"
    __hex_format = "#%04x%04x%04x"
    
    top2bottom = 1
    left2right = 2

    def __init__(self, parent, colors = ("#4F0575", "#C3B1E1"), direction = left2right, **kw):

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
    '''this class will show the main battle interface of the program'''
    def __init__(self):
        global  boss_image1
        button_width = 12
        button_height = 2
        button_font = ("Arial", "12", "bold")
        
        # setting up the main frame
        self.main_frame = Frame(bg="#221B27", padx=60)
        self.main_frame.grid()
        
        # setting up the battle frame
        self.battle_frame = GradientFrame(self.main_frame, relief=SOLID, borderwidth=2)
        self.battle_frame.grid(padx=5, pady=5, row=0)

        self.boss_health = Label(self.battle_frame, text="♥ ▬▬▬▬100%▬▬▬▬", fg="purple", font=("Arial", "20"), relief=SOLID)
        self.boss_health.grid(padx=5, pady=5, row=1, sticky="WE")

        image_label = Label(self.battle_frame, image=boss_image1, bg="green")
        image_label.grid(padx=5, pady=5, row=2)

        # feedback message
        mood = "Eason is currently happy"
        self.feedback = Label(self.battle_frame, text=mood, fg="red")
        self.feedback.grid(row=3)

        #player health
        self.player_health = Label(self.battle_frame, text="▬▬▬Health bar▬▬▬", fg="green", font=("Arial", "13"), relief=SOLID)
        self.player_health.grid(row=4)

        #frame for buttons
        self.button_frame = Frame(bg="#FFE6CC", relief=SOLID, width=10, height=10, borderwidth=2, padx=30, pady=5)
        self.button_frame.grid(row=5, padx=5, pady=5)

        self.attack_button = Button(self.button_frame, text="Attack", bg="red", width=button_width, height=button_height, font=button_font, relief=SOLID)
        self.attack_button.grid(row=0, column=0, padx=5, pady=5)

        self.break_shield_button = Button(self.button_frame, text="Break Shield", bg="#ECCA3D", width=button_width, height=button_height, font=button_font, relief=SOLID)
        self.break_shield_button.grid(row=0, column=1, padx=5, pady=5)

        self.restore_shield_button = Button(self.button_frame, text="Restore Shield", bg="#B0E3E6", width=button_width, height=button_height, font=button_font, relief=SOLID)
        self.restore_shield_button.grid(row=0, column=2, padx=5, pady=5)

        self.help_button = Button(self.button_frame, text="Help / Info", bg="Orange", width=button_width, height=button_height, font=button_font, relief=SOLID)
        self.help_button.grid(row=1, column=0, columnspan=2)

        self.history_button = Button(self.button_frame, text="History / Info", bg="purple", width=button_width, height=button_height, font=button_font, relief=SOLID)
        self.history_button.grid(row=1, column=1, columnspan=2)

        # music for the program
        self.music = winsound.PlaySound("Phase1song.wav", winsound.SND_ASYNC) # if we don't have async then any code after the music will not be played. # it is similar to threading. 
        

# main program
root = Tk()
root.title("Hardest Fight with Eason")
boss_image1 = PhotoImage(file="bossimage1.gif")
root.resizable(0,0) # user cannot change the size of the window
MainBattle()
root.mainloop()