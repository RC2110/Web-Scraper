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

def extract(url):
     response = requests.get(url, headers=HEADERS)
     content = response.text
     return content

def parse_data(content):
     selector = selectorlib.Extractor.from_yaml_file("extract.yaml")
     data = selector.extract(content)['tours']
     return data

def create_table():
     file = open("dataab.db", 'w')
     rsp = sqlite3.connect("dataab.db")
     cursor = rsp.cursor()
     cursor.execute("CREATE TABLE 'musictour'('Band' TEXT, 'City' TEXT, 'Date' TEXT)")
     rsp.commit()
    # emp = file.read()
    # return emp


def read_file(ext):
    lst = ext.split(',')
    lst = [item.strip() for item in lst]
    band, city, date = lst
    rsp = sqlite3.connect("dataab.db")
    cursor = rsp.cursor()
    cursor.execute("SELECT * FROM musictour WHERE Band=? AND City= ? AND Date=?",(band, city, date))
    rows = cursor.fetchall()
    print(rows)
    return rows


def write_msg(data):
    resp = sqlite3.connect("dataab.db")
    cursor = resp.cursor()
    lst = ext.split(',')
    lst = [item.strip() for item in lst]
    band, city, date = lst
    cursor.execute("INSERT INTO musictour VALUES(?,?,?)", lst)
    resp.commit()

def send_email(msg):
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
        phase1 = extract(url)
        ext = parse_data(phase1)
        print(ext)

        if not os.path.exists('dataab.db'):
             create_table()
             pass

        if ext != "No upcoming tours":
            file = read_file(ext)

            if not file:
                write_msg(ext)

                send_email(ext)
                print("The tour information has been emailed!")

        time.sleep(1)





