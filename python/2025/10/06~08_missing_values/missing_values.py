import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# フォント設定（日本語対応）
plt.rcParams['font.family'] = 'Hiragino Sans'

# データ読み込み
df = pd.read_csv("sample_missing.csv", parse_dates=["date"])
print("===元データ===")
print(df)

# 欠損値の確認
print("\n===欠損値の確認===")
print(df.isnull().sum())

# 可視化（ヒートマップ）
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap="coolwarm", yticklabels=False)
plt.title("欠損データのヒートマップ")
plt.show()

# 補完処理
df_mean = df.fillna(df.mean(numeric_only=True))

df_ffill = df.fillna(method='ffill')

# 結果表示
print("\n===平均値で補完したデータ===")
print(df_mean)

print("\n===前の値で補完したデータ（ffill）===")
print(df_ffill)
