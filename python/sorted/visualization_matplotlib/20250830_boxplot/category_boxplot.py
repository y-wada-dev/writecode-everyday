import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Hiragino Sans'

df = pd.DataFrame({
    "store": np.random.choice(["Store A", "Store B", "Store C"], size=300),
    "sales": np.random.normal(loc=100, scale=20, size=300)
})

sns.boxplot(x="store", y ="sales", data=df)
plt.title("店舗別の売上箱ひげ図")
plt.show()