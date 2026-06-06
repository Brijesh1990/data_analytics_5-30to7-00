# scatterplot is used to display or a data of two numerical variables

# scaterplot is used to provides relationship b/w two numeriacl variables 

# scatterplot is identifying patterns or corelations b/w two numerical variables  

# create a graph to provides relationship b/w total bill and tip

import seaborn as sns
import matplotlib.pyplot as plt 

tips=sns.load_dataset("tips")
sns.scatterplot(x="total_bill",y="tip",hue="day",data=tips)
# show sactterplot
plt.show()