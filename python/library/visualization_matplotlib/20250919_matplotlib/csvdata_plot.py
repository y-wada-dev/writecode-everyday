import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample.csv", parse_dates=["date"])
df = df.set_index("date")

monthly_store = df.groupby("store")["sales"].resample("ME").sum().unstack(0)

monthly_store.index = monthly_store.index.strftime("%Y/%m")

ax = monthly_store.plot(kind="bar", figsize=(8,4))
ax.set_title("Monthly Sales by Store")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
plt.tight_layout()
plt.show()