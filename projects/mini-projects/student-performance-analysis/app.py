# third party module 
# third party module is installable 
# pip install modulename
# python -m pip install modulename
# module name of third party 

# pandas 
# numpy 
# matplotlib 
# seaborn 
# requests

import pandas as pd 
import matplotlib.pyplot as plt
data ={
    "name":["kalpit","dhruv","bhavika","om","dhruvraj","divraj","brijesh","samar","sanket"],
    "attendance":[0,1,1,1,1,0,1,1,1]
}

# create a pie chart
df=pd.DataFrame(data)
print(df)

# find absent and present 
present=(df["attendance"]==1).sum()
absent=(df["attendance"]==0).sum()

colors=["green","red"]
values=[present,absent]
labels=["Present","Absent"]

print("total present students list is :",present)
print("total absent students list is :",absent)

# find the dynamic details in list in graph or chart
plt.title("students attendance management systems")
plt.pie(
    values,
    labels=labels, 
    colors=["green","red"], 
    autopct="%1.1f%%"    
)

plt.show()
