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

# # display all data in graph (pie chart | line chart | bar chart etc)

# plt.figure(figsize=(9,9))


# horizontal bar chart create 


# plt.figure(figsize=(6,4))
# plt.barh(df["wastage"],df["food"])
# plt.xlabel("wastage")
# plt.ylabel("food")



# plt.figure(figsize=(8,6))
# plt.bar(df["wastage"],df["food"])
# plt.xlabel("wastage")
# plt.ylabel("food")


# create chart of pie
plt.figure(figsize=(5,5))
plt.pie(
    
    df["wastage"],    # values
    labels=df["food"], # labels 
    autopct='%1.1f%%', # percentage formatter
    startangle=90  #rotate the chart
    
)

# bar chart display data 
# plt.figure(figsize=(6,4))
# plt.bar(df["wastage"],df["food"])
# plt.xlabel("wastage")
# plt.ylabel("food")


#display data in line chart 
# plt.plot(df["wastage"],df["food"], marker='o') 
# plt.xlabel("wastage")
# plt.ylabel("food")
# plt.grid(True)



# chart title 
plt.title("Canteen management systems food wastage bar chart dynamic app")
# show chart 
plt.show()