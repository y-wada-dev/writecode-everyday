import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "sales": [100, 200, 150, 300],
    "ad_spend": [10, 20, 15, 25],
    "customers": [50, 80, 60, 120]  
})

# 売上効率を計算
df["sales_per_customer"] = df["sales"] / df["customers"]
df["roi"] = df["sales"] / df["ad_spend"]

print(df)

# カテゴリ変数を数値化
df2 = pd.DataFrame({
    "gender": ["male", "female", "male", "female"],
    "purchased": [1, 0, 1, 1]
})

df_encoded = pd.get_dummies(df2, columns=["gender"], drop_first=True)
print(df_encoded)

df3 = pd.DataFrame({
    "date": pd.date_range("2025-01-01", periods=5, freq="D"),
    "sales": [100, 150, 130, 180, 200]
})

df3["month"] = df3["date"].dt.month
df3["dayofweek"] = df3["date"].dt.dayofweek
print(df3)

# 相関行列のヒートマップを表示
corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()