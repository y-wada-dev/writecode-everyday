import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Hiragino Sans'

np.random.seed(0)
data = np.random.normal(loc=50, scale=10, size=100)

plt.boxplot(data)
plt.title("箱ひげ図の例")
plt.ylabel("値")
plt.show()