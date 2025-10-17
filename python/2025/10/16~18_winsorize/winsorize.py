import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats.mstats as winsorize

# データ読み込み
df = pd.read_csv("sample_outlier.csv")
print("[OK] Loaded data:", len(df), "rows")
print(df.head())

# === 外れ値検出・除去 ===
Q1 = df["sales"].quantile(0.25)
Q3 = df["sales"].quantile(0.75)
IQR = Q3 - Q1
lower = Q3 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# mask
mask = (df["sales"] >= lower) & (df["sales"] <= upper)
df_iqr_removed = df[mask]

print(f"\n[INFO] 外れ値除去 (IQR法): {len(df) - len(df_iqr_removed)} 件削除")
print(f"  lower={lower:.2f}, upper={upper:.2f}")

# ===Winsorize===
sales_winsor = winsorize(df["sales"], limits=(0.05, 0.05))
df["sales_winsor"] = sales_winsor

print(f"\n[INFO] Winsorize適用 (5%):")
print(df[["sales", "sales_winsor"]].head(10))
