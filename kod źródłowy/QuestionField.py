from tkinter import *
from RoundButton import RoundButton
import playsound

class Question:
    def __init__(self):
        self.name = ""
        self.question = "<question>"
        self.firstCaption = "1"
        self.lastCaption = "2"
        self.count = 2
        self.levelNumberColor = ['#28BF1E', '#ACFA46', '#F6F61D', '#F7B329', '#F33022']
        self.selected = None
        self.padding = 200
        
        self.isCheckbox = False
        self.checkboxes = []


    def __repr__(self):
        return "<Question: name: '%s'; question: '%s'; selected: '%s'>" % (self.name, self.question, self.selected)

class QuestionField:
    def __init__(self, root):
        self.root = root
        self.width = 1000
        self.height = 320
        self.previousButtonPhoto = PhotoImage(file = "previousButton.png")
        self.nextButtonPhoto = PhotoImage(file = "nextButton.png")
        self.currentQuestion = 0
        self.questions = []
        self.mainField = Canvas(self.root, width = self.width, height = self.height)

    def Init(self):
        # self.mainField = Canvas(self.root, width = self.width, height = self.height, background = "#FF0000")
        self.mainField.delete("all")
        self.mainField.configure(background = "#5894fc", bd = 0, highlightthickness = 0, relief='ridge')
        self.draw_rectangle(1, 1, self.width+1, self.height+1, 50, "white")

        self.previousButton = Button(self.root, command = self.previousCallback, borderwidth = 0, image = self.previousButtonPhoto, background = "#ffffff", activebackground = "#ffffff", relief = FLAT)
        self.previousButton_window = self.mainField.create_window(70, 30, width = self.previousButtonPhoto.width(), height = self.previousButtonPhoto.height(), anchor=N, window=self.previousButton)

        self.nextButton = Button(self.root, command = self.nextCallback, borderwidth = 0, image = self.nextButtonPhoto, background = "#ffffff", activebackground = "#ffffff", relief = FLAT)
        self.nextButton_window = self.mainField.create_window(110, 30, width = self.nextButtonPhoto.width(), height = self.nextButtonPhoto.height(), anchor=NW, window=self.nextButton)

        self.mainField.create_text(200, 30, anchor="nw", text = "%d/%d %s"%(self.currentQuestion+1, len(self.questions), self.questions[self.currentQuestion].question), font=('Verdana', 25, 'bold'))

        self.levelButtons = []
        self.levelButtonsWindows = []
        self.callbacks = []
        self.callbacks.append(self.button1)
        self.callbacks.append(self.button2)
        self.callbacks.append(self.button3)
        self.callbacks.append(self.button4)
        self.callbacks.append(self.button5)
        d = self.width-2*self.questions[self.currentQuestion].padding
        for i in range(0, self.questions[self.currentQuestion].count):
            if i == 4:
                pass
            else:
                currentButton = RoundButton(self.root)
            if len(self.questions[self.currentQuestion].levelNumberColor)> i:
                if self.questions[self.currentQuestion].count == 2:
                    if i == 0:
                        currentButton.insideColor = self.questions[self.currentQuestion].levelNumberColor[0]
                    if i == 1:
                        currentButton.insideColor = self.questions[self.currentQuestion].levelNumberColor[4]
                else:
                    currentButton.insideColor = self.questions[self.currentQuestion].levelNumberColor[i]
            currentButton.diameter = 50
            currentButton.onClickCallback = self.callbacks[i]
            currentButton.Init()

            x = self.questions[self.currentQuestion].padding - currentButton.diameter/2
            currentButton_window = self.mainField.create_window(x+(d/(self.questions[self.currentQuestion].count-1)*i), 170, width = currentButton.diameter-3, height = currentButton.diameter-3, anchor=NW, window=currentButton.GetObject())
            if (self.questions[self.currentQuestion].selected is not None) and (i == self.questions[self.currentQuestion].selected):
                currentButton.SetSelection(True)
            
            self.levelButtons.append(currentButton)
            self.levelButtonsWindows.append(currentButton_window)

            if(i>0):
                self.nextButton_window = self.mainField.create_line(x+d/(self.questions[self.currentQuestion].count-1)*(i-1), 170+25, x+d/(self.questions[self.currentQuestion].count-1)*i, 170+25, width = 10, fill="#000000")


        self.mainField.create_text(x - len(self.questions[self.currentQuestion].firstCaption)*5, 170+60, anchor="nw", text = self.questions[self.currentQuestion].firstCaption, font=('Arial', 20, 'bold italic'))
        self.mainField.create_text(x+d/(self.questions[self.currentQuestion].count-1)*(self.questions[self.currentQuestion].count-1) - len(self.questions[self.currentQuestion].firstCaption)*5, 170+60, anchor="nw", text = self.questions[self.currentQuestion].lastCaption, font=('Arial', 20, 'bold italic'))

        

    def button1(self):
        for i in self.levelButtons:
            i.SetSelection(False)

        self.levelButtons[0].SetSelection(True)
        self.questions[self.currentQuestion].selected = 0
        self.root.update_idletasks()

    def button2(self):
        for i in self.levelButtons:
            i.SetSelection(False)

        self.levelButtons[1].SetSelection(True)
        self.questions[self.currentQuestion].selected = 1
        self.root.update_idletasks()

    def button3(self):
        for i in self.levelButtons:
            i.SetSelection(False)

        self.levelButtons[2].SetSelection(True)
        self.questions[self.currentQuestion].selected = 2
        self.root.update_idletasks()

    def button4(self):
        for i in self.levelButtons:
            i.SetSelection(False)

        self.levelButtons[3].SetSelection(True)
        self.questions[self.currentQuestion].selected = 3
        self.root.update_idletasks()

    def button5(self):
        for i in self.levelButtons:
            i.SetSelection(False)

        self.levelButtons[4].SetSelection(True)
        self.questions[self.currentQuestion].selected = 4
        self.root.update_idletasks()


    def Refresh(self):
        pass

    def GetObject(self):
        return self.mainField

    def nextCallback(self):
        if self.currentQuestion < len(self.questions)-1:
            self.currentQuestion +=1
            self.Init()

    def previousCallback(self):
        if self.currentQuestion >0:
            self.currentQuestion -=1
            self.Init()


    def AddQuestion(self, name, question, firstCaption, lastCaption, count):
        q = Question()
        q.question = question
        q.firstCaption = firstCaption
        q.lastCaption = lastCaption
        q.name = name
        q.count = count

        self.questions.append(q)

    def draw_rectangle(self, x1, y1, x2, y2, radius, fill="", outline=""):
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1,]
        self.mainField.create_polygon(points, fill=fill, outline=outline, smooth=True)


