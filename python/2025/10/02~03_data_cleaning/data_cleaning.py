import pandas as pd
import numpy as np

df = pd.DataFrame({
    "id": range(1, 11),
    "date": ["2025-01-01", "2025-01-02", "2025/01/03", None, "2025-01-05",
             "2025-01-06", "2025-01-07", "2025-01-08", "2025-13-01", "2025-01-10"],
    "sales": [100, 200, None, 150, 9999, 180, 170, np.nan, 210, 50],
    "category": ["A", "B", "A", "B", "C", "C", None, "B", "A", "A"]
})

print(df)

print("="*50)

print(df.isnull().sum())

print("="*50)

# 欠損補完
df["sales"] = df["sales"].fillna(df["sales"].median())
df["category"] = df["category"].fillna("Unknown")

df["date"] = pd.to_datetime(df["date"], errors='coerce')
print(df)

print("="*50)

# 異常値処理
Q1 = df["sales"].quantile(0.25)
Q3 = df["sales"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df["sales_cleaned"] = df["sales"].where(df["sales"].between(lower, upper))

print(df)