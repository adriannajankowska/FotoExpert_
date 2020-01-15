import MainWindow
import sqlite3

mw = MainWindow.MainWindow()

# def Exit_Callback():
#     for question in mw.mainField.questions:
#         if question.selected is None:
#             return
    
#     conn = sqlite3.connect('aparaty.db')

#     if(mw.mainField.questions[0].selected == 0):
#         if mw.mainField.questions[1].selected == 0:
#             price_range = "(Cena >= 200 AND Cena <=2000)"
#         elif mw.mainField.questions[1].selected == 1:
#             price_range = "(Cena >= 2001 AND Cena <=5000)"
#         elif mw.mainField.questions[1].selected == 2:
#             price_range = "(Cena >= 5001 AND Cena <=10000)"
#         elif mw.mainField.questions[1].selected == 3:
#             price_range = "(Cena >= 10001 AND Cena <=20000)"
#         elif mw.mainField.questions[1].selected == 4:
#             price_range = "(Cena >= 20001 AND Cena <=30000)"
#     else:
#         if mw.mainField.questions[1].selected == 0:
#             price_range = "(Cena >= 40 AND Cena <=100)"
#         elif mw.mainField.questions[1].selected == 1:
#             price_range = "(Cena >= 101 AND Cena <=200)"
#         elif mw.mainField.questions[1].selected == 2:
#             price_range = "(Cena >= 201 AND Cena <=300)"
#         elif mw.mainField.questions[1].selected == 3:
#             price_range = "(Cena >= 301 AND Cena <=500)"
#         elif mw.mainField.questions[1].selected == 4:
#             price_range = "(Cena >= 501 AND Cena <=800)"

#     if mw.mainField.questions[3].selected==1:
#         mass_range = "Waga <= '415'"
#     else:
#         mass_range = "1=1"

#     query = (
#             "SELECT "
#                 "* "
#             "FROM "
#                 "BODY "
#              "WHERE "
#                 "CzyAnalogowy = '%s' AND "
#                 "%s AND "
#                 "%s AND "
#                 "CzyDoFilmow = '%s' AND "
#                 "CzyDoSportu = '%s' "
#                 "ORDER BY "
#                     "Cena ASC;"
#             ) % (
#                 mw.mainField.questions[0].selected,
#                 price_range,
#                 mass_range,
#                 mw.mainField.questions[5].selected,
#                 mw.mainField.questions[6].selected,
#             )
#     print(query)
#     cursor = conn.execute(query)
#     body = None
#     for i in cursor:
#         body = i
#         break

#     print(body)

#     if body is not None and body[5] != '-':
#         query = (
#                 "SELECT "
#                     "* "
#                 "FROM "
#                     "OBIEKTYWY "
#                 "WHERE "
#                     "TypGwintu = '%s' "
#                 "ORDER BY "
#                     "Cena ASC;"
#                 ) % (
#                     body[5]
#                 )
#         print(query)
#         cursor = conn.execute(query)
#         lens = None
#         for i in cursor:
#             lens = i
#             break
#         print(lens)

#     # self.mainField.AddQuestion('pyt1', 'Jaką fotografią się interesujesz?', 'Cyfrową', 'Analogową', 2)
#     # self.mainField.AddQuestion('pyt2', 'Określ stopień swojego \n       doświadczenia w fotografii', 'Początkujący', 'Profesjonalista', 5)
#     # self.mainField.AddQuestion('pyt4', 'Czy planujesz piesze wycieczki z aparatem?', 'Tak', 'Nie', 2)

#         # self.mainField.AddQuestion('pyt5', 'Czy interesuje Cię makrofotografia?', 'Tak', 'Nie', 2)
#         # self.mainField.AddQuestion('pyt6', 'Czy robisz zdjęcia w nocy?', 'Tak', 'Nie', 2)
#     # self.mainField.AddQuestion('pyt7', 'Czy kręcisz filmy wideo', 'Tak', 'Nie', 2)

#     # self.mainField.AddQuestion('pyt8', 'Czy relacjonujesz wydarzenia sportowe?', 'Tak', 'Nie', 2)
#         # self.mainField.AddQuestion('pyt9', 'Czy robisz zdjęcia portretowe?', 'Tak', 'Nie', 2)

# mw.Exit_Callback = Exit_Callback
mw.Init()
