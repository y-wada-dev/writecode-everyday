import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

plt.rcParams['font.family'] = 'Hiragino Sans' 

np.random.seed(42)

x = np.random.rand(50) * 10
y = 2 * x +5 + np.random.randn(50) * 2

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
line = slope * x + intercept

plt.scatter(x, y, label="Data Points")
plt.plot(x, line, color="red", label=f"回帰直線: y = {slope:.2f}x+{intercept:.2f}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title(f"相関係数 r{r_value:.2f}")
plt.show()