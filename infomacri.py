import sqlite3
import pandas as pd
import plotly.express as px



conn = sqlite3.connect('twitter.db')
c = conn.cursor()

df = pd.read_sql("SELECT * FROM sentimiento WHERE tweet LIKE '%Macri%' ORDER BY unix DESC LIMIT 1000", conn)
print(df.tail(25))
print(df.describe())
print(df.head(25))
print(df.info())

fig2 = px.scatter(df, 
        x="unix", 
        y="sentimiento", 
        color="sentimiento", 
        text="sentimiento",
       title="ANALISIS DE SENTIMIENTOS SOBRE MAURICIO  MACRI TWEETS 24/9/2021",
       animation_frame="sentimiento")

fig2.show()