from tkinter import *

class ButtonTemplate(Button):
    def __init__(self):
        self.background = "#5894fc"
        self.activebackground = "#5894fc"
        self.relief = FLAT
        self.borderwidth = 0
        # ============ pola zmienne ============
        self.imageName = ""
        self.imagePhoto = PhotoImage(self.imageName)
        self.command = None

    def Init(self, imageName, command):
        self.imageName = imageName
        self.command = command


class ButtonController():
    def __init__(self):
        pass

    def Init(self):
        self.mockRestartButton = ButtonTemplate()
        self.mockRestartButton.Init("restartButtonphoto.png", self.Restart_Callback())
        self.mockRestartButton.grid(row = 0, column=0, pady=30)

        #self.restartButtonphoto = PhotoImage(file = "restartButtonphoto.png")
        #self.restartButton = Button(image = self.restartButtonphoto, command=self.Restart_Callback, activebackground = self.activebackground, bg = self.background, relief = FLAT, borderwidth = 0)
        #self.restartButton.grid(row = 0, column=0, pady=30)
        
        #self.helpButtonPhoto = PhotoImage(file = "helpButtonPhoto.png")
        #self.helpButton = Button(image = self.helpButtonPhoto, command=self.Restart_Callback, activebackground = self.activebackground, bg = self.background, relief = FLAT, borderwidth = 0)
        #self.helpButton.grid(row = 0, column=1, sticky = "w", pady=30)

        #self.aboutButtonPhoto = PhotoImage(file = "aboutButtonPhoto.png")
        #self.aboutButton = Button(image = self.aboutButtonPhoto, command=self.Restart_Callback, activebackground = self.activebackground, bg = self.background, relief = FLAT, borderwidth = 0)
        #self.aboutButton.grid(row = 0, column=2, sticky="e", padx=50, pady=30)

        #self.exitButtonPhoto = PhotoImage(file = "exitButtonPhoto.png")
        #self.ExitButton = Button(root, image = self.exitButtonPhoto, command=self.GetResult_Callback, activebackground = self.activebackground, bg = self.background, relief = FLAT, borderwidth = 0)
        #self.ExitButton.grid(row = 2, column=2, sticky="e",padx=50, pady=30)
 
    def Restart_Callback(self):
        print("a")

        
    def GetResult_Callback(self):
        pass