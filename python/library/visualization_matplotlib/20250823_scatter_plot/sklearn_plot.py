import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "store": ["A","A","A","B","B","B","C","C","C"],
    "sales": [100, 120, 130, 80, 95, 110, 60, 70, 90],
    "customers": [30, 35, 40, 25, 28, 33, 15, 18, 22],
    "ad_spend": [10, 15, 20, 8, 12, 10, 5, 7, 9]
})

X = df[["customers", "ad_spend"]]
y = df["sales"]

model = LinearRegression()
model.fit(X, y)

print("回帰係数:", model.coef_)
print("切片:", model.intercept_)

df["predicted_sales"] = model.predict(X)

print(df)

plt.scatter(df["customers"], df["sales"], label="Actual")
plt.scatter(df["customers"], df["predicted_sales"], label="Predicted", marker="x")
plt.xlabel("Customers")
plt.ylabel("Sales")
plt.legend()
plt.show()