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




