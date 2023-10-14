import os
import requests
import selectorlib
import sqlite3
import smtplib
import time
from email.message import EmailMessage

url = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


class WebScrape:
    def __init__(self):
        self.response = requests.get(url, headers=HEADERS)

    def extract(self, url):
            content = self.response.text
            return content
    def parse(self, content):
         selector = selectorlib.Extractor.from_yaml_file("extract.yaml")
         data = selector.extract(content)['tours']
         return data


class DataBase:
    def __init__(self, url):
        self.rsp = sqlite3.connect(url)
        self.cursor = self.rsp.cursor()
    def create(self):
         # print("hi")
         file = open("dataab.db", 'w') #"dataab.db"
         self.cursor.execute("CREATE TABLE 'musictour'('Band' TEXT, 'City' TEXT, 'Date' TEXT)")
         self.rsp.commit()
         file.close()
         #emp = file.read()
         # return emp
    def read(self, ext):
        lst = ext.split(',')
        lst = [item.strip() for item in lst]
        band, city, date = lst
        self.cursor.execute("SELECT * FROM musictour WHERE Band=? AND City= ? AND Date=?",(band, city, date))
        rows = self.cursor.fetchall()
        print(rows)
        return rows
    def write(self, data):
        lst = ext.split(',')
        lst = [item.strip() for item in lst]
        band, city, date = lst
        self.cursor.execute("INSERT INTO musictour VALUES(?,?,?)", lst)
        self.rsp.commit()

class Emailing:
    def send(self, msg):
        host= "smtp.gmail.com"
        port= 587
        user_email="rajaachandramohan@gmail.com"
        rec_email="rajaachandramohan@gmail.com"
        pas= os.getenv("aivideo")
        message= EmailMessage()
        message.set_content(msg)
        server=smtplib.SMTP(host, port)
        server.ehlo()
        server.starttls()
        server.login(user_email, pas)
        server.sendmail(user_email, rec_email, message.as_string())
        print("message sent!")
        server.quit()


if __name__ == "__main__":
    while True:
        web = WebScrape()
        phase1 = web.extract(url)
        ext = web.parse(phase1)
        print(ext)

        if not os.path.exists('dataab.db'):
               db = DataBase("dataab.db")
               db.create()
               pass

        db = DataBase("dataab.db")
        if ext != "No upcoming tours":
            file = db.read(ext)

            if not file:
                db.write(ext)
                em =Emailing()
                em.send(ext)
                print("The tour information has been emailed!")

        time.sleep(1)





