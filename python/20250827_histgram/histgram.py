import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Hiragino Sans'

data = np.random.normal(loc=50, scale=10, size=1000)

plt.hist(data, bins=20, color="skyblue", edgecolor="black")
plt.title("ヒストグラム")
plt.xlabel("値")
plt.ylabel("頻度")
plt.show()