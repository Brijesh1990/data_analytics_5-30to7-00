# used all libraries 
import pandas as pd 
# import matplotlib lib for chart
import matplotlib.pyplot as plt
# create a data 
data={
	"name":["bhavika","sneha","priyanka","komal","shreya","kalpit","brijesh","dhruv"],
   "age":[20,21,22,23,24,25,26,27],
   "salary":[10000,20000,30000,40000,50000,60000,70000,80000],
   "department":["IT","HR","IT","HR","IT","HR","IT","HR"]
}

#create a dataframe or tabular data
df=pd.DataFrame(data)
print(df)
#create a total salary column
print("-----------------------")
total_salary=df["salary"].sum()
print("Total Salary:", total_salary)

# average salary
print("-----------------------")
average_salary=df["salary"].mean()
print("Average Salary:", average_salary)

# create a tabular data for age and salary
print("-----------------------")
age_salary_df=df[["age","salary"]]
print(age_salary_df)

# create a bar chart for employee name who get > salary than average salary
print("-----------------------")
high_earners=df[df["salary"] > average_salary]
print(high_earners)


# show department wise salary
print("-----------------------")
print(df.groupby("department")["salary"].sum())

# show two bar chart for department wise salary
department_salary=df.groupby("department")["salary"].sum()
print("-----------------------")
print(department_salary)

# display data of high earners in bar chart	

plt.title("High Earners Salary")
plt.bar(high_earners["name"],high_earners["salary"], color='coral')
plt.xlabel("Employee Name")
plt.ylabel("Salary")

# display data in line chart
# plt.title("High Earners Salary")
# plt.plot(high_earners["name"],high_earners["salary"], color='coral', marker='o')
# plt.xlabel("Employee Name")
# plt.ylabel("Salary")

# generated data in excel 
excel_generated_data=df.to_excel("employee_salary_data.xlsx", engine="openpyxl", index=False)
print("excels generated successuly", excel_generated_data)

plt.show()


