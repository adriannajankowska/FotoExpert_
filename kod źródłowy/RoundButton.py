from tkinter import *

class RoundButton:
    def __init__(self, root):
        self.root = root
        self.insideColor = "#00ff00"
        self.outsideColor = "#000000"
        self.outsideColorHover = "#555555"
        self.diameter = 50
        self.thickness = 8
        self.onClickCallback = None
        self.isSelected = False

    def Init(self):
        self.canvas = Canvas(self.root, width = self.diameter, height = self.diameter, bd=0, highlightthickness=0, relief='ridge', background="white")
        self.canvas.create_oval(self.thickness/2, self.thickness/2, self.diameter-self.thickness, self.diameter-self.thickness, width = self.thickness+2, outline = self.outsideColor, fill = self.insideColor)

        self.canvas.bind("<Button-1>", self.__MouseClick)
        self.canvas.bind("<Enter>", self.__OnEnter)
        self.canvas.bind("<Leave>", self.__OnLeave)

    def SetSelection(self, isSelected):
        print(isSelected)
        self.isSelected = isSelected
        if(self.isSelected):
            self.canvas.create_oval(self.thickness+11, self.thickness+11, self.diameter-self.thickness-15, self.diameter-self.thickness-15, fill = "#000000")
        else:
            self.canvas.create_oval(self.thickness/2, self.thickness/2, self.diameter-self.thickness, self.diameter-self.thickness, width = self.thickness+2, outline = self.outsideColor, fill = self.insideColor)

    def __MouseClick(self, event):
        if self.__IsInCircle(event):
            self.onClickCallback()

    def __OnEnter(self, event):
        self.canvas.create_oval(self.thickness/2-1, self.thickness/2-1, self.diameter-self.thickness, self.diameter-self.thickness, width = self.thickness, outline = self.outsideColorHover, fill = self.insideColor)
        self.SetSelection(self.isSelected)

    def __OnLeave(self, event):
        self.canvas.create_oval(self.thickness/2-1, self.thickness/2-1, self.diameter-self.thickness, self.diameter-self.thickness, width = self.thickness, outline = self.outsideColor, fill = self.insideColor)
        self.SetSelection(self.isSelected)

    def __IsInCircle(self, event):
        return self.onClickCallback is not None and (event.x - self.diameter/2)**2 + (event.y - self.diameter/2)**2 < self.diameter**2/4
    

    def GetObject(self):
        return self.canvas


