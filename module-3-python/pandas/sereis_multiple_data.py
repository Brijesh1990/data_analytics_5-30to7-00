import pandas as pd 
data={
    "name":["brjesh","het","divyang","krish"],
    "age":[25,20,28,29],
    "salary":[35500,15500,55000,20500]
}

res=pd.Series(data)
print(res)