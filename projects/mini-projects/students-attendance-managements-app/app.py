# create a attendance managements systems
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
# create a students attendance data
data={
    "studentname":["rahul","dhruv","bhavika","brijesh","kalpit","parakruti","mitesh"],
    "total_days":[100,100,100,100,100,100,100],
    "absent_days":[10,5,20,25,15,2,9]
}

# print data
# calculate in tabular layout
df=pd.DataFrame(data) 
print(df)
# total attendance days 
print('--------------------------------------')
total_days=df["total_days"].sum()
print("Total attendance days is :",total_days)

# total absent days 
print('--------------------------------------')
absent_days=df["absent_days"].sum()
print("Total Absents days is :",absent_days)

# maximum absent students  
print('--------------------------------------')
maximum_absent_student=df["absent_days"].max()
print("Total maximum absent days is :",maximum_absent_student)


# maximum absent students  name who is max absent
print('--------------------------------------')
maximum_absent_student=df.loc[df["absent_days"].idxmax(),"studentname"]
print("Maximum absent students is :",maximum_absent_student)
print("Maximum absent days is :",maximum_absent_student,"days")

# data visualised using matlotlib in chart
plt.title("maximum absent students data visulaized")
plt.pie(
    df["absent_days"],
    labels=df["studentname"],
    colors=["yellow","green","blue","red","lightgray","pink","coral"],
    autopct="%1.1f%%"
    
)

# generate data in excel 
excel_students_data=df.to_excel("students_data.xlsx", engine="openpyxl", index="False")
print("data generated in excel successfully",excel_students_data)

plt.show()







