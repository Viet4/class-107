import csv
import pandas as bear
import plotly.graph_objects as go

df = bear.read_csv("data.csv")

student_id = input("Enter the Student ID: ")
full_id = str("TRL_" + student_id)
direction = str(input("v or h: "))

student_data = df.loc[df["student_id"] == full_id]

mean = student_data.groupby("level")["attempt"].mean()

if (direction == "v"):
    fig = go.Figure(go.Bar(
        y = mean, 
        x = ["Level 1", "Level 2", "Level 3", "Level 4"], 
        orientation = "v"
    ))
elif (direction == "h"):
    fig = go.Figure(go.Bar(
        x = mean, 
        y = ["Level 1", "Level 2", "Level 3", "Level 4"], 
        orientation = "h"
    ))

fig.show()
