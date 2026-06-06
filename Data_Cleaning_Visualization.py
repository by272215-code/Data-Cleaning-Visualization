# Data Cleaning and Visualization Project
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data.csv")
print("Original Dataset")
print(df.head())
df = df.drop_duplicates()
df["Sales"] = df["Sales"].fillna(df["Sales"].mean())
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

df = df[(df["Sales"] >= lower_limit) & (df["Sales"] <= upper_limit)]
print("\nCleaned Dataset")
print(df.head())
total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()
print(f"\nTotal Sales: {total_sales}")
print(f"Average Sales: {average_sales:.2f}")
# Visualization
plt.figure(figsize=(8, 5))
df.groupby("Region")["Sales"].sum().plot(kind="bar")

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

