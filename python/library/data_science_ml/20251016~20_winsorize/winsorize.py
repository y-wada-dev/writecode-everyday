import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats.mstats import winsorize

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
sales_winsor = winsorize(df["sales"], limits=[0.05, 0.05])
df["sales_winsor"] = sales_winsor

print(f"\n[INFO] Winsorize適用 (5%):")
print(df[["sales", "sales_winsor"]].head(10))

# === 可視化 ===
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
sns.boxplot(y=df["sales"], ax=axes[0], color="lightgray")
axes[0].set_title("original")

sns.boxplot(y=df_iqr_removed["sales"], ax=axes[1], color="lightblue")
axes[1].set_title("After IQR removal")

sns.boxplot(y=df["sales_winsor"], ax=axes[2], color="lightgreen")
axes[2].set_title("After Winsorize")

plt.tight_layout()
plt.show()

# 平均・標準偏差の比較
stats = pd.DataFrame({
    "平均": [
        df["sales"].mean(),
        df_iqr_removed["sales"].mean(),
        df["sales_winsor"].mean()
    ],
    "標準偏差": [
        df["sales"].std(),
        df_iqr_removed["sales"].std(),
        df["sales_winsor"].std()
    ]
}, index=["Before", "IQR除去後", "winsorize後"])

print("\n[INFO] 平均・標準偏差の比較:")
print(stats.round(2))