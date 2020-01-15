from tkinter import *
import QuestionField
from ButtonController import *
import sqlite3


class MainWindow:
    def __init__(self):
        self.title = "FotoExpert"
        self.background = "#5894fc"
        self.width = 1070
        self.height = 570

    def Init(self):
        self.root = Tk()
        self.root.title(self.title)
        self.root.configure(background = self.background)
        self.root.geometry("%dx%d" % (self.width, self.height))

        self.restartButtonphoto = PhotoImage(file = "restartButtonphoto.png")
        self.restartButton = Button(self.root, image = self.restartButtonphoto, command=self.Restart_Callback, activebackground = self.background, bg = self.background, relief = FLAT, borderwidth = 0)
        self.restartButton.grid(row = 0, column=0, sticky="w", padx=50, pady=30)

        self.exitButtonPhoto = PhotoImage(file = "exitButtonPhoto.png")
        self.ExitButton = Button(self.root, image = self.exitButtonPhoto, command=self.Exit_Callback, activebackground = self.background, bg = self.background, relief = FLAT, borderwidth = 0)
        self.ExitButton.grid(row = 2, column=2, sticky="e", padx=50, pady=30)


        self.mainField = QuestionField.QuestionField(self.root)
        self.mainField.AddQuestion('pyt1', 'Jaką fotografią się interesujesz?', 'Cyfrową', 'Analogową', 2)
        self.mainField.AddQuestion('pyt2', 'Określ stopień swojego \n       doświadczenia w fotografii.', 'Początkujący', 'Profesjonalista', 5)
        self.mainField.AddQuestion('pyt4', 'Czy planujesz piesze wycieczki \n       z aparatem?', 'Nie', 'Tak', 2)
        self.mainField.AddQuestion('pyt5', 'Czy interesuje Cię makrofotografia?', 'Nie', 'Tak', 2)
        self.mainField.AddQuestion('pyt6', 'Czy robisz zdjęcia w nocy?', 'Nie', 'Tak', 2)
        self.mainField.AddQuestion('pyt7', 'Czy kręcisz filmy wideo?', 'Nie', 'Tak', 2)
        self.mainField.AddQuestion('pyt8', 'Czy relacjonujesz wydarzenia \n       sportowe?', 'Nie', 'Tak', 2)
        self.mainField.AddQuestion('pyt9', 'Czy robisz zdjęcia portretowe?', 'Nie', 'Tak', 2)
        self.mainField.Init()
        self.mainField.GetObject().grid(row = 1, column = 0, columnspan = 3, sticky = "we", padx = 30)

        self.root.mainloop()

    def Restart_Callback(self):
        self.mainField.currentQuestion = 0
        for i in range(0, len(self.mainField.questions)):
            self.mainField.questions[i].selected = None
        self.mainField.Init()

        self.textBackground.destroy()

    def Exit_Callback(self):
        for question in self.mainField.questions:
            if question.selected is None:
                return
        
        conn = sqlite3.connect('aparaty.db')

        if(self.mainField.questions[0].selected == 0):
            if self.mainField.questions[1].selected == 0:
                price_range = "(Cena >= 200 AND Cena <=2000)"
            elif self.mainField.questions[1].selected == 1:
                price_range = "(Cena >= 2001 AND Cena <=5000)"
            elif self.mainField.questions[1].selected == 2:
                price_range = "(Cena >= 5001 AND Cena <=10000)"
            elif self.mainField.questions[1].selected == 3:
                price_range = "(Cena >= 10001 AND Cena <=20000)"
            elif self.mainField.questions[1].selected == 4:
                price_range = "(Cena >= 20001 AND Cena <=30000)"
        else:
            if self.mainField.questions[1].selected == 0:
                price_range = "(Cena >= 40 AND Cena <=100)"
            elif self.mainField.questions[1].selected == 1:
                price_range = "(Cena >= 101 AND Cena <=200)"
            elif self.mainField.questions[1].selected == 2:
                price_range = "(Cena >= 201 AND Cena <=300)"
            elif self.mainField.questions[1].selected == 3:
                price_range = "(Cena >= 301 AND Cena <=500)"
            elif self.mainField.questions[1].selected == 4:
                price_range = "(Cena >= 501 AND Cena <=800)"

        if self.mainField.questions[3].selected==1:
            mass_range = "Waga <= '415'"
        else:
            mass_range = "1=1"

        query = (
                "SELECT "
                    "* "
                "FROM "
                    "BODY "
                "WHERE "
                    "CzyAnalogowy = '%s' AND "
                    "%s AND "
                    "%s AND "
                    "CzyDoFilmow = '%s' AND "
                    "CzyDoSportu = '%s' "
                    "ORDER BY "
                        "Cena ASC;"
                ) % (
                    self.mainField.questions[0].selected,
                    price_range,
                    mass_range,
                    self.mainField.questions[5].selected,
                    self.mainField.questions[6].selected,
                )
        print(query)
        cursor = conn.execute(query)
        body = None
        for i in cursor:
            body = i
            break

        print(body)
        if body is not None:
            text = "Body:        " + body[0] + " " + body[1]
        else:
            text = "Brak"

        self.textBackground = Canvas(self.root, width = 500, height = 90, background = "#FF0000")
        self.textBackground.create_text(10, 10, anchor="nw", text = text, font=('Arial', 20, 'bold italic'))
        self.textBackground.grid(row = 2, column = 0, columnspan = 2, sticky = "we", padx = 30)

        if body is not None and body[5] != '-':
            query = (
                    "SELECT "
                        "* "
                    "FROM "
                        "OBIEKTYWY "
                    "WHERE "
                        "TypGwintu = '%s' "
                    "ORDER BY "
                        "Cena ASC;"
                    ) % (
                        body[5]
                    )
            print(query)
            cursor = conn.execute(query)
            lens = None
            for i in cursor:
                lens = i
                break
            print(lens)
            if lens is not None:
                text = "Obiektyw: " + lens[0] + " " + lens[1]
            else:
                text = "Brak"
            self.textBackground.create_text(10, 50, anchor="nw", text = text, font=('Arial', 20, 'bold italic'))

