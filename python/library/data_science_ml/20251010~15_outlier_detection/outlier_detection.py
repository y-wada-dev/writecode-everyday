import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# データの読み込み
df = pd.read_csv("sample_outlier.csv")
print(df)

# 箱ひげ図の描画
plt.figure(figsize=(7, 4))
sns.boxplot(data=df)
plt.show()

# IQR法による外れ値検出
def detect_outliers_iqr(df, col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    mask = (df[col] < lower) | (df[col] > upper)
    return df[mask]

outlier_iqr = detect_outliers_iqr(df, "sales")
print("IQR法による外れ値:\n", outlier_iqr)

# Zスコア法による外れ値検出
def detect_outliers_zscore(df, col, threshold=2.0):
    mean = df[col].mean()
    std = df[col].std()
    z_scores = (df[col] - mean) / std
    return df[np.abs(z_scores) > threshold]

outliers_z = detect_outliers_zscore(df, "sales")
print("Zスコア法による外れ値:\n", outliers_z)

s = pd.to_numeric(df["sales"], errors="coerce").dropna()
mean = s.mean()
std  = s.std(ddof=0)  # or ddof=1
z = (s - mean) / std
print("mean:", mean, "std:", std)
print(pd.DataFrame({"sales": s, "z": z}).sort_values("z"))

# 外れ値を除去したデータ
def remove_outliers(df, col, threshold=2.0):
    mean = df[col].mean()
    std = df[col].std()
    z = np.abs((df[col] - mean) / std)
    return df[z <= threshold]

df_cleaned = remove_outliers(df, "sales")
print("外れ値を除去したデータ:\n", df_cleaned)

# 可視化
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
sns.boxplot(data=df, ax=axes[0])
axes[0].set_title("Before (with outliners)")
sns.boxplot(data=df_cleaned, ax=axes[1])
axes[1].set_title("After (outliners removed)")
plt.tight_layout()
plt.show()