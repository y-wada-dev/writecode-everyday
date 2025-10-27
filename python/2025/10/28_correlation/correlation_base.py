import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "sales": [100, 200, 150, 300, 250],
    "ad_spend": [10, 20, 15, 25, 22],
    "customers": [50, 100, 75, 150, 130],
    "discount": [5, 8, 7, 10, 9]
})

corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.show()
high_corr = corr[(corr.abs() > 0.8) & (corr.abs() < 1.0)]
print("高相関ペア：\n", high_corr)