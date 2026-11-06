import pandas as pd

# Load dataset using Pandas
df = pd.read_csv("data/sales_data.csv")

print("\n--- First 5 Records ---")
print(df.head())

print("\n--- Dataset Information ---")
df.info()

print("\n--- Dataset Shape ---")
print(df.shape)

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Duplicate Records ---")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df["Product"] = df["Product"].fillna("Unknown")
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
df["Unit_Price"] = df["Unit_Price"].fillna(df["Unit_Price"].median())

# Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

# Save cleaned data
df.to_csv("data/cleaned_sales_data.csv", index=False)

print("\n--- After Data Cleaning ---")
print(df.isnull().sum())
print("Duplicate Records:", df.duplicated().sum())
print("Cleaned Shape:", df.shape)

print("\nData Cleaning Completed Successfully!")

import matplotlib.pyplot as plt

# Product-wise Sales
product_sales = df.groupby("Product")["Total_Sales"].sum()

# Bar Chart
plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar")
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

# Line Chart
plt.figure(figsize=(8, 5))
product_sales.plot(kind="line", marker="o")
plt.title("Product-wise Sales Trend")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("line_chart.png")
plt.show()

# Pie Chart
plt.figure(figsize=(7, 7))

product_sales.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Product-wise Sales Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("pie_chart.png")
plt.show()
plt.close()