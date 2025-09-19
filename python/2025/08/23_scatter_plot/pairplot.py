import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# サンプルデータを拡張
df = pd.DataFrame({
    "store": ["A","A","A","B","B","B","C","C","C"],
    "sales": [100, 120, 130, 80, 95, 110, 60, 70, 90],
    "customers": [30, 35, 40, 25, 28, 33, 15, 18, 22],
    "ad_spend": [10, 15, 20, 8, 12, 10, 5, 7, 9]
})

# ペアプロット
sns.pairplot(df, hue="store")
plt.show()