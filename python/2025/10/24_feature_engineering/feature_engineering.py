import pandas as pd

df = pd.DataFrame({
    "sales": [100, 200, 150, 300],
    "ad_spend": [10, 20, 15, 25],
    "customers": [50, 80, 60, 120]  
})

# 売上効率を計算
df["sales_per_customer"] = df["sales"] / df["customers"]
df["roi"] = df["sales"] / df["ad_spend"]

print(df)
