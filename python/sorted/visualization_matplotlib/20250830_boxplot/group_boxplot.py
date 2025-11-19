import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Hiragino Sans'

group1 = np.random.normal(50, 10, 100)
group2 = np.random.normal(60, 15, 100)
group3 = np.random.normal(55, 5, 100)

plt.boxplot([group1, group2, group3], labels=["グループ1", "グループ2", "グループ3"])
plt.title("グループ別の箱ひげ図")
plt.ylabel("値")
plt.show()