import streamlit as st
import plotly.express as px
import sqlite3

st.title("Temperature of the World!")
response=sqlite3.connect("datb.db")
cursor = response.cursor()
cursor.execute("SELECT * FROM temps")
col1 = cursor.fetchall()

dte=[]
tmp=[]
for i in col1:
    dte.append(i[0])
    tmp.append(i[1])

figure= px.line(x=dte, y=tmp, labels={'x':'Date', 'y':'temperature in Celsius'})
st.plotly_chart(figure)