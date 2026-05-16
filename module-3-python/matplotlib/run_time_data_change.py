# import libraries 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# create a dataframes using pandas 
data={
    
    "food":["ringda bateta","paneer tikka","tameta raswala","flower sabji","paneer bhurji"],
    
    "wastage":[40,15,5,15,20]
    
}

# create a DataFrame
df=pd.DataFrame(data)

# display dataframe 
print(df)

#create a figure 

# fig, ax=plt.subplots(figsize=(7,7))
ax=plt.figure(figsize=(7,7))

# create a function for update chart 
def update(frame):
    # clear old chart 
    ax.clear()
    
    # generate a dynamic random new values in chart
    df["wastage"]=[
        
        random.randint(0,20),
        random.randint(0,30),
        random.randint(0,10),
        random.randint(0,10),
        random.randint(0,40)
    ]

# create chart of pie

plt.pie(
    
    df["wastage"],    # values
    labels=df["food"], # labels 
    autopct='%1.1f%%', # percentage formatter
    startangle=90  #rotate the chart
    
)

# chart title 
ax.set_title("Canteen management systems food wastage bar chart dynamic app")

# applied the animations 
ani=FuncAnimation(
    fig,
    update,
    interval=2000  # 2 second every data update
)
# show chart 
plt.show()