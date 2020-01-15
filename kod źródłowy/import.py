import sqlite3

f = open("obiektywy.csv", 'r')

data = f.read()
print(data)

conn = sqlite3.connect('aparaty.db')

lines = data.split('\n')
for line in lines:
    entries = line.split(';')
    if len(entries) > 9: 
        query = ("INSERT INTO OBIEKTYWY (Producent,Model,Cena,Waga,PrzyslonaMin,CzyStaloogniskowy,TypGwintu,CzyDoPortretu,CzyDoMakrofotografii,CzyDoNocnych)"
                "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                ) % (entries[0], entries[1],entries[2],entries[3],entries[4],entries[5],entries[6],entries[7],entries[8],entries[9])
        conn.execute(query)
        print(query)

conn.commit()
f.close()