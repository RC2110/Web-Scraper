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
def extract(url):
    response = requests.get(url)
    content = response.text
    return content

def create_table():
    with open("datb.db", 'w') as file:
        response = sqlite3.connect("datb.db")
        cursor = response.cursor()
        cursor.execute("CREATE TABLE temps(date TEXT, temperature TEXT)")
        response.commit()

def write_table(time, temp):
    response = sqlite3.connect("datb.db")
    cursor = response.cursor()
    cursor.execute("INSERT INTO temps VALUES(?,?)", (time, temp))
    response.commit()


def parse(content):
    assign = selectorlib.Extractor.from_yaml_file("extract1.yaml")
    parsed = assign.extract(content)['time']
    return parsed

if __name__ == "__main__":
    while True:
        ext = extract(url)
        data = parse(ext)
        print(data)

        if not os.path.exists("datb.db"):
            create_table()
            pass
        now = datetime.now()
        write_table(now, data)
        # df = pd.read_csv("data1.txt")
        # figure = px.line(x=df['date'] , y=df['temperature'], labels={'x':'date', 'y':'temperature'})
        # st.title("Temperature in the World!")
        # st.plotly_chart(figure)




