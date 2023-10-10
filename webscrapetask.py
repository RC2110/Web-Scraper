import requests
import selectorlib
import os
from datetime import datetime
import plotly.express as px
import pandas as pd
import streamlit as st

url = "http://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
def extract(url):
    response = requests.get(url)
    content = response.text
    return content

def create_file():
    file = open("data1.txt", 'w')
    file.write("date,temperature" + '\n')
    file.close()

def write_file(time, temp):
      with open("data1.txt", 'a') as file:
          file.write (f"{time},{temp}" +'\n')


def parse(content):
    assign = selectorlib.Extractor.from_yaml_file("extract1.yaml")
    parsed = assign.extract(content)['time']
    return parsed

if __name__ == "__main__":
    ext = extract(url)
    data = parse(ext)
    print(data)

    if not os.path.exists("data1.txt"):
        create_file()
        pass
    now = datetime.now()
    write_file(now, data)
    df = pd.read_csv("data1.txt")
    figure = px.line(x=df['date'] , y=df['temperature'], labels={'x':'date', 'y':'temperature'})
    st.title("Temperature in the World!")
    st.plotly_chart(figure)




