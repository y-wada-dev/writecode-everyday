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
