import os
import requests
import selectorlib
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


class TextFile:
    def create(self):
        file = open("data.txt", 'w')
    # emp = file.read()
    # return emp
    def read(self):
        with open("data.txt", 'r') as file:
             content = file.read()
             return content
    def write(self, data):
        with open("data.txt", 'a') as file:
            file.write( data +'\n')

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
        web =WebScrape()
        phase1 = web.extract(url)
        ext = web.parse(phase1)
        print(ext)
        txt = TextFile()
        if not os.path.exists("data.txt"):
             txt.create()
             pass
        file = txt.read()
        if ext != "No upcoming tours":
            if ext not in file:
                email=Emailing()
                txt.write(ext)
                email.send(ext)

        time.sleep(1)


