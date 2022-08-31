import pandas as pd
import plotly.express as px
import numpy as np

data = pd.read_csv("project114.csv")

score = data["TOEFL Score"].tolist()
chance = data["Chance of Admit "].tolist()

graph = px.scatter(x = score, y = chance)
graph.show()


scoreArray = np.array(score)
chanceArray = np.array(chance)

m , b = np.polyfit(scoreArray , chanceArray , 1)


y = []

for x in score:
    y2 = m*x+b
    y.append(y2)


graph = px.scatter(x = scoreArray, y = chanceArray)

graph.update_layout(shapes=[
    dict(
      type= 'line',
      y0= min(y), y1= max(y),
      x0= min(scoreArray), x1= max(scoreArray)
    )
])

graph.show()







