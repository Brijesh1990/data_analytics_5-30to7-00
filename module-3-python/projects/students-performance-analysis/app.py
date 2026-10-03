import matplotlib.pyplot as plt
import pandas as pd

students = {
	"Name": [
		"Ava Patel",
		"Liam Chen",
		"Mia Johnson",
		"Noah Williams",
		"Sofia Garcia",
		"Ethan Brown",
		"Isabella Davis",
		"Lucas Wilson",
		"Amara Okafor",
		"Oliver Martin",
	],
	"Mathematics": [92, 78, 88, 85, 95, 73, 90, 81, 87, 79],
	"Science": [89, 84, 91, 79, 93, 82, 86, 88, 94, 80],
	"English": [94, 81, 85, 90, 88, 87, 92, 84, 91, 86],
}

df = pd.DataFrame(students)

# create a tabular layout of subjects
subjects = ["Mathematics", "Science", "English"]

# create a total of marks 

df["Total"] = df[subjects].sum(axis=1)

# average of subject 

df["Average"] = df[subjects].mean(axis=1)

# create  marks of max than average marks 

top_student = df.loc[df["Average"].idxmax()]

print("Student marks and results:")
print(df.to_string(index=False, formatters={"Average": "{:.2f}".format}))
print(
	f"\nHighest average: {top_student['Name']} "
	f"({top_student['Average']:.2f})"
)

plt.figure(figsize=(10, 6))
plt.bar(df["Name"], df["Average"], color="steelblue")
plt.title("Average Marks by Student")
plt.xlabel("Student")
plt.ylabel("Average marks")
plt.ylim(0, 100)
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.show()
