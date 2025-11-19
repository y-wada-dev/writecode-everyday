import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Hiragino Sans'

np.random.seed(42)
df = pd.DataFrame({
    "売上": np.random.normal(100, 20, 50),
    "広告費": np.random.normal(50, 10, 50),
    "来客数": np.random.normal(200, 30, 50),
    "満足度": np.random.normal(3.5, 0.5, 50)
})

print(df.corr())

corr = df.corr()

plt.figure(figsize=(6, 4))
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("各変数間の相関行列ヒートマップ")
plt.show()