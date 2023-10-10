import os
import requests
import selectorlib
import smtplib
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

def create_file():
    file = open("data.txt", 'w')
    # emp = file.read()
    # return emp


def read_file():
    with open("data.txt", 'r') as file:
         content = file.read()
         return content


def write_msg(data):
    with open("data.txt", 'a') as file:
        file.write( data +'\n')


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
    phase1 = extract(url)
    ext = parse_data(phase1)
    print(ext)
    if not os.path.exists("data.txt"):
         create_file()
         pass
    file = read_file()
    if ext != "No upcoming tours":
        if ext not in file:
            write_msg(ext)
            send_email(ext)


