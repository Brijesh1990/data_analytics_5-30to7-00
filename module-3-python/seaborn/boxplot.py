import seaborn as sns
import matplotlib.pyplot as plt 

tips=sns.load_dataset("tips")
# sns.barplot(x="total_bill",y="tip",data=tips)
sns.boxplot(x="day",y="total_bill",data=tips)
# show boxplot
plt.show()