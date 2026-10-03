import matplotlib.pyplot as plt
import pandas as pd


sales_data = {
	"Month": [
		"January",
		"February",
		"March",
		"April",
		"May",
		"June",
		"July",
		"August",
		"September",
		"October",
		"November",
		"December",
	],
	"Sales": [12500, 13800, 14200, 15700, 16300, 17800, 18500, 19200, 17600, 20100, 22400, 25800],
}

sales_df = pd.DataFrame(sales_data)

annual_sales = sales_df["Sales"].sum()

highest_sales = sales_df.loc[sales_df["Sales"].idxmax()]

lowest_sales = sales_df.loc[sales_df["Sales"].idxmin()]


print(sales_df.to_string(index=False))
print(f"\nTotal annual sales: ${annual_sales:,.2f}")
print(f"Highest sales: {highest_sales['Month']} (${highest_sales['Sales']:,.2f})")
print(f"Lowest sales: {lowest_sales['Month']} (${lowest_sales['Sales']:,.2f})")

plt.figure(figsize=(10, 5))

plt.plot(sales_df["Month"], sales_df["Sales"], marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
