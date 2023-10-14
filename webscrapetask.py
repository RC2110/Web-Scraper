import requests
import selectorlib
import os
from datetime import datetime
import plotly.express as px
import pandas as pd
import streamlit as st
import sqlite3

url = "http://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

class WebScrape:
    def extract(self, url):
        response = requests.get(url)
        content = response.text
        return content

    def parse(self, content):
        assign = selectorlib.Extractor.from_yaml_file("extract1.yaml")
        parsed = assign.extract(content)['time']
        return parsed

class DataBase:
    def __init__(self, url):
        self.response = sqlite3.connect(url) #"datb.db"
        self.cursor = self.response.cursor()
    def create(self, url):
        file = open(url, 'w')
        self.cursor.execute("CREATE TABLE temps(date TEXT, temperature TEXT)")
        self.response.commit()
        file.close()
    def write(self, time, temp):
        self.cursor.execute("INSERT INTO temps VALUES(?,?)", (time, temp))
        self.response.commit()

if __name__ == "__main__":
    while True:
        web=WebScrape()
        ext = web.extract(url)
        data = web.parse(ext)
        print(data)

        if not os.path.exists("datb.db"):
            db = DataBase("datb.db")
            db.create(url="datb.db")
            print("hi")
            pass
        db= DataBase("datb.db")
        now = datetime.now()
        db.write(now, data)
        # df = pd.read_csv("data1.txt")
        # figure = px.line(x=df['date'] , y=df['temperature'], labels={'x':'date', 'y':'temperature'})
        # st.title("Temperature in the World!")
        # st.plotly_chart(figure)




