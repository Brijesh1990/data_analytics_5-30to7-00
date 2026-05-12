import pandas as pd 
res=pd.read_csv('user_data.csv')
# print(res)

# give or view first row of data start 5 rows 
# df=res.head()
# print(df)


# give last 5 read rows 
# df=res.tail()
# print(df)


# read one column only 
# print(res['Name'])
# print(res['Name'][0])

# give (rows , column)
# print(res.shape)

print(res[["Name","Age","City","Country","Email"][0]])


