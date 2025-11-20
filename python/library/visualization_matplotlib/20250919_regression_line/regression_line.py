import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({
    "store": ["A","A","A","B","B","B","C","C","C"],
    "sales": [100, 120, 130, 80, 95, 110, 60, 70, 90],
    "customers": [30, 35, 40, 25, 28, 33, 15, 18, 22],
    "ad_spend": [10, 15, 20, 8, 12, 10, 5, 7, 9]
})
model = LinearRegression()
model.fit(df[["customers", "ad_spend"]], df["sales"])

x_range = np.linspace(df["customers"].min(), df["customers"].max(), 100)
x_line = pd.DataFrame({
    "customers": x_range,
    "ad_spend": np.full_like(x_range, df["ad_spend"].mean())
})
y_line = model.predict(x_line)

plt.scatter(df["customers"], df["sales"], label="Actual")
plt.plot(x_range, y_line, color="red", label="Regression")
plt.xlabel("Customers")
plt.ylabel("Sales")
plt.legend()
plt.show()

print("決定係数 R^2:", model.score(df[["customers", "ad_spend"]], df["sales"]))