import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data.csv")

X = df[["Quantity","Discount"]]
y = df["Sales"]

model = LinearRegression()
model.fit(X,y)

# Correct prediction input format
new_data = pd.DataFrame([[3,0.1]], columns=["Quantity","Discount"])

prediction = model.predict(new_data)

print("\nPredicted Sales =", prediction[0])

