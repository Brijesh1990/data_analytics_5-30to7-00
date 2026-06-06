import seaborn as sns
import matplotlib.pyplot as plt 

tips=sns.load_dataset("tips")
# sns.barplot(x="total_bill",y="tip",data=tips)
sns.histplot(tips["total_bill"], kde=True)
# show boxplot
plt.show()