import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Hiragino Sans'

data = np.random.normal(loc=50, scale=10, size=1000)

plt.hist(data, bins=20, alpha=0.6, color="skyblue", edgecolor="black", density=True)
# plt.title("ヒストグラム")
# plt.xlabel("値")
# plt.ylabel("頻度")
# plt.show()

from scipy.stats import norm
x = np.linspace(min(data), max(data), 100)
plt.plot(x, norm.pdf(x, loc=50, scale=10), "r-", linewidth=2, label="正規分布")
plt.title("ヒストグラムと正規分布")
plt.xlabel("値")
plt.ylabel("確率密度")
plt.legend()
plt.show()