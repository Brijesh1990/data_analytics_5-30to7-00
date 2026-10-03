# create a canteen management systems and evaluate by chart which food max'

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Food': ['Pizza', 'Burger', 'Pasta', 'Salad', 'Sushi'],
    'Quantity Sold': [150, 200, 120, 80, 90],
    "wastage_food":[20,10,40,50,30]
}

df = pd.DataFrame(data) 
print(df)
# Find maximum wastage
max_wastage = df['wastage_food'].max()

# Find food with maximum wastage
max_food = df.loc[df['wastage_food'].idxmax(), 'Food']

print("\nMaximum Wastage:", max_wastage)
print("Food with Maximum Wastage:", max_food)
# create pie chart to find wastage food
plt.title('find wastage food')
plt.pie(
    df["wastage_food"],
    labels=df['Food'],
    autopct='%1.1f%%',
    startangle=-90  
)
plt.show()