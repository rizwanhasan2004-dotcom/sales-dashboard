import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

print("\n===== DATA PREVIEW =====")
print(df.head())

# ---------- SALES BY REGION ----------
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure()
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()

# ---------- SALES BY PRODUCT ----------
product_sales = df.groupby("Product")["Sales"].sum()

plt.figure()
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

# ---------- PROFIT DISTRIBUTION ----------
plt.figure()
plt.hist(df["Profit"], bins=5)
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.show()
