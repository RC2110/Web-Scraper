import sqlite3

response = sqlite3.connect("datab.db")
cursor = response.cursor()

cmd = cursor.execute("SELECT city, band FROM events WHERE date=('01-01-2024')")
data = cmd.fetchall()
print(data)

# cmd2 = cursor.execute("INSERT INTO events VALUES('Lightmusic','City of music', '01-01-2024')")
# response.commit()

# metadata = [('Style', 'Vegas', '01-01-2024'),
#             ('Dance', 'Malibu', '25-12-2023')]
#
# cmd3 = cursor.executemany("INSERT INTO events VALUES(?,?,?)", metadata)
# response.commit()


cmd3 = cursor.execute("CREATE TABLE 'musictour1_dates'('Band' TEXT, 'City' TEXT,'Date'  TEXT)")
response.commit()
