import matplotlib.pyplot as plt
import pandas as pd


employees = pd.DataFrame(
	[
		{"name": "Ava Patel", "department": "Engineering", "salary": 92000},
		{"name": "Liam Chen", "department": "Engineering", "salary": 88000},
		{"name": "Noah Williams", "department": "Engineering", "salary": 96000},
		{"name": "Mia Garcia", "department": "Sales", "salary": 72000},
		{"name": "Ethan Brown", "department": "Sales", "salary": 68000},
		{"name": "Isabella Davis", "department": "Sales", "salary": 81000},
		{"name": "Lucas Wilson", "department": "Human Resources", "salary": 64000},
		{"name": "Amelia Martinez", "department": "Human Resources", "salary": 70000},
		{"name": "Mason Anderson", "department": "Human Resources", "salary": 66000},
		{"name": "Harper Thomas", "department": "Finance", "salary": 85000},
		{"name": "James Taylor", "department": "Finance", "salary": 79000},
		{"name": "Evelyn Moore", "department": "Finance", "salary": 90000},
	]
)

department_average = employees.groupby("department")["salary"].mean()
overall_average = employees["salary"].mean()
above_average = employees[employees["salary"] > overall_average]

print("Employee data:")
print(employees.to_string(index=False))
print("\nAverage salary by department:")
print(department_average.to_string())
print(f"\nOverall average salary: ${overall_average:,.2f}")
print("\nEmployees earning more than the overall average:")
print(above_average.to_string(index=False))

department_average.plot(kind="bar", color="steelblue", edgecolor="black")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary ($)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("department_average_salaries.png", dpi=150)
plt.show()
