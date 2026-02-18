import sqlite3
import pandas as pd

# Connect to database (creates if not exists)
conn = sqlite3.connect("sales.db")

# Load CSV data
df = pd.read_csv("data.csv")

# Store data in SQL table
df.to_sql("sales", conn, if_exists="replace", index=False)

print("Data inserted into database")

# Query data
query = """
SELECT Region, SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Region
"""

result = pd.read_sql(query, conn)

print("\nSales by Region from Database:")
print(result)

conn.close()
