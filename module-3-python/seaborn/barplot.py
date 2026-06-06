# barplot is used to display or a data of two numerical variables

# barplot is used to provides relationship b/w two numeriacl variables 

# barplot is identifying patterns or corelations b/w two numerical variables  

# create a graph to provides relationship b/w total bill and tip

import seaborn as sns
import matplotlib.pyplot as plt 

tips=sns.load_dataset("tips")
# sns.barplot(x="total_bill",y="tip",data=tips)
sns.barplot(x="day",y="total_bill",data=tips)
# show barplot
plt.show()