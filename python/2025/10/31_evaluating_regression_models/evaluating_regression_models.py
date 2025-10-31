import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# サンプルデータ
df = pd.DataFrame({
    "ad_spend": [10, 20, 30, 40, 50, 60],
    "customers": [100, 200, 300, 400, 500, 600],
    "sales": [80, 160, 240, 330, 420, 490]
})

X = df[["ad_spend", "customers"]]
y = df["sales"]

X_tarin, X_test, y_train, y_test, = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_tarin, y_train)
y_pred = model.predict(X_test)

# 評価指標
print("R²:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))