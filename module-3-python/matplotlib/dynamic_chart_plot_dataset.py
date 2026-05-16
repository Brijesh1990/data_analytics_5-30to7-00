# import libraries 
import pandas as pd
import matplotlib.pyplot as plt

# create a dataframes using pandas 
data={
    
    "food":["ringda bateta","paneer tikka","tameta raswala","flower sabji","paneer bhurji"],
    
    "wastage":[40,15,5,15,20]
    
}

# create a DataFrame
df=pd.DataFrame(data)

# display dataframe 
print(df)

# display all data in graph (pie chart | line chart | bar chart etc)

plt.figure(figsize=(9,9))

# create chart of pie

plt.pie(
    
    df["wastage"],    # values
    labels=df["food"], # labels 
    autopct='%1.1f%%', # percentage formatter
    startangle=90  #rotate the chart
    
)

# chart title 

plt.title("Canteen management systems food wastage app")

# show chart 
plt.show()