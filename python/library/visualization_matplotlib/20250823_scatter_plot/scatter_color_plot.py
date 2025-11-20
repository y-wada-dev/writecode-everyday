import pandas as pd
import matplotlib.pyplot as plt

# sampledata
df = pd.DataFrame({
    "store": ["A","A","A","B","B","B","C","C","C"],
    "sales": [100, 120, 130, 80, 95, 110, 60, 70, 90],
    "customers": [30, 35, 40, 25, 28, 33, 15, 18, 22]
})

# scatter plot
fig, ax = plt.subplots()
for store, group in df.groupby("store"):
    ax.scatter(group["customers"], group["sales"], label=store)

ax.set_title("Sales vs Customers")
ax.set_xlabel("Customers")
ax.set_ylabel("Sales")
ax.legend()
plt.show()