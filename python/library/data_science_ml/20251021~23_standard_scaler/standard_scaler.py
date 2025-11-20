from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import matplotlib.pyplot as plt

# フォント
plt.rcParams['font.family'] = 'Hiragino Sans' 

df = pd.DataFrame({
    "sales": [100, 200, 300, 400],
    "ad_spend": [5, 10, 15, 20]
})

scaler = StandardScaler()
scaled = scaler.fit_transform(df)
df_scaled = pd.DataFrame(scaled, columns=df.columns)
print(df_scaled)

scaler = MinMaxScaler()
normalized = scaler.fit_transform(df)
df_norm = pd.DataFrame(normalized, columns=df.columns)
print(df_norm)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].set_title("Standardized (平均0, 分散1)")
axes[0].boxplot(df_scaled.values, labels=df_scaled.columns)

axes[1].set_title("Normalized (0から1の範囲)")
axes[1].boxplot(df_norm.values, labels=df_norm.columns)

plt.tight_layout()
plt.show()