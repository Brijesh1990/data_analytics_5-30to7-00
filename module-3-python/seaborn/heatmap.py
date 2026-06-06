import seaborn as sns
import matplotlib.pyplot as plt 

tips=sns.load_dataset("tips")
corr=tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True,cmap="coolwarm")
# heatmap
plt.show()