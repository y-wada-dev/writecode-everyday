import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ads_sales.csv")

plt.figure(figsize=(6, 4))
plt.scatter(df["ads_spend"], df["sales"], color="blue", alpha=0.7)

plt.title("Monthly Sales vs. Ads Spend", fontsize=14)
plt.xlabel("ads_spend($)", fontsize=12)
plt.ylabel("sales($)", fontsize=12)

plt.grid(True, linestyle="--", alpha=0.5)

plt.show()