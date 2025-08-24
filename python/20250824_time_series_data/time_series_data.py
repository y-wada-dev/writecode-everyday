import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

date_range = pd.date_range("2025-01-01", "2025-03-31")
sales = np.random.randint(80, 200, len(date_range))

df = pd.DataFrame({"Date": date_range, "Sales": sales})
df = df.set_index("Date")

print(df.head())

# df["Sales"].plot(figsize=(10,4))
# plt.title("Daily Sales")
# plt.xlabel("Date")
# plt.ylabel("Sales")
# plt.grid(True, alpha=0.3)
# plt.show()

monthly = df["Sales"].resample("M").sum()
monthly.plot(kind="bar", figsize=(8,4))
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()