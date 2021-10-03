import sqlite3
import pandas as pd
import plotly.express as px


conn = sqlite3.connect('twitter-Alberto.db')
c = conn.cursor()

df = pd.read_sql("SELECT * FROM sentimiento WHERE tweet LIKE '%Alberto Fernandez%' ORDER BY unix DESC LIMIT 7000", conn)
print(df.tail(25))
print(df.describe())
print(df.head(25))
print(df.info())

fig = px.scatter(df, 
        x="unix", 
        y="sentimiento", 
        color="sentimiento", 
        text="sentimiento",
       title="ANALISIS DE SENTIMIENTOS SOBRE ALBERTO FERNANDEZ TWEETS 24/9/2021")
fig.show()




