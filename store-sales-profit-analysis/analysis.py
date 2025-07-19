import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Sample - Superstore.csv", encoding='latin1')
data.columns = [col.strip() for col in data.columns]

print("First 5 rows:\n", data.head())
print("\nSummary Stats:\n", data.describe(include='all'))

category_sales = data.groupby('Category')['Sales'].sum().sort_values(ascending=False)
category_profit = data.groupby('Category')['Profit'].sum().sort_values(ascending=False)

print("\nSales by Category:\n", category_sales)
print("\nProfit by Category:\n", category_profit)

plt.figure(figsize=(10,5))
sns.barplot(x=category_sales.index, y=category_sales.values, color='skyblue', label='Sales')
sns.barplot(x=category_profit.index, y=category_profit.values, color='orange', alpha=0.7, label='Profit')
plt.title('Sales and Profit by Category')
plt.legend()
plt.tight_layout()
plt.savefig("category_sales_profit.png")
plt.show()
