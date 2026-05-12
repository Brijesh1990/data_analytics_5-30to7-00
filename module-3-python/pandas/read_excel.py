import pandas as pd 
res=pd.read_excel('employee_data_sample.xlsx')
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

# print(res[["Full Name"][0]])
# print(res[["Department"]])

# print(res.shape)

# How to rename the columns

# syntax to change a column name 
# rename(columns={"name":"value"}, inplace=True)

# res.rename(columns={"Full Name":"Name"},inplace=True)
# print(res)


# drop a column 

# res.drop("Full Name", axis=1, inplace=True)
# print(res)

# add columns 
# res["added-date"]=["12-05-2026","12-05-2026","12-05-2026","12-05-2026","12-05-2026","12-05-2026"]
# print(res)

# filter data salary filter greater than $80000

# res = res[res["Perf Score"] > 4]
# print(res)

res = res[res["Annual Salary"] > 80000]
print(res)