import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, RepeatedKFold, cross_val_score, learning_curve
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, classification_report, confusion_matrix

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

import seaborn as sns

RANDOM_SEED = 42

# ========= 回帰: ベースライン/残差/CV/学習曲線 =========
df = pd.DataFrame({
    "ad_spend": [10, 20, 30, 40, 50, 60],
    "customers": [100, 200, 300, 400, 500, 600],
    "sales": [80, 160, 240, 330, 420, 490]
})

X_reg = df[["ad_spend", "customers"]]
y_reg = df["sales"]

X_train, X_test, y_train, y_test, = train_test_split(
    X_reg, y_reg, test_size=0.3, random_state=RANDOM_SEED
)

reg = LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)

# 評価指標
print("回帰モデルの評価指標")
print("R²:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# ベースラインモデル
y_base = np.full_like(y_test, fill_value=y_train.mean(), dtype=float)
print("\nベースラインモデルの評価指標")
print("R²:", r2_score(y_test, y_base))
print("MAE:", mean_absolute_error(y_test, y_base))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_base)))

# 残差プロット
residuals = y_test - y_pred
plt.figure(figsize=(5,3))
plt.scatter(y_pred, residuals)
plt.axhline(0, color="r", linestyle="--")
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.title("Residuals Plot")
plt.grid(True, alpha=0.5)
plt.show()

# iris = load_iris(as_frame=True)
# X, y = iris.data, iris.target

# X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3, random_state=0)

# clf = RandomForestClassifier(random_state=0)
# clf.fit(X_train, y_train)
# y_pred = clf.predict(X_test)

# print("Accuracy:", accuracy_score(y_test, y_pred))
# print("Precision:", precision_score(y_test, y_pred, average="macro"))
# print("Recall:", recall_score(y_test, y_pred, average="macro"))
# print("F1:", f1_score(y_test, y_pred, average="macro"))
# print("混同行列:\n", confusion_matrix(y_test, y_pred))

# import matplotlib.pyplot as plt

# plt.scatter(y_test, y_pred)
# plt.plot([y.min(), y.max()], [y.min(), y.max()], "r--")
# plt.xlabel("Actual")
# plt.ylabel("Predicted")
# plt.title("Prediced VS Actual")
# plt.grid(True, alpha=0.5) 
# plt.show()