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
