import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import SelectKBest, f_regression

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

X = df.drop(columns=["sales"])
y = df["sales"]

model = RandomForestRegressor(random_state=0)
model.fit(X, y)

importances = pd.Series(model.feature_importances_, index=X.columns)
importances.sort_values(ascending=False).plot(kind="bar")

plt.title("Feature Importances")
plt.show()

selector = SelectKBest(score_func=f_regression, k=2)
X_new = selector.fit_transform(X, y)

selected_features = X.columns[selector.get_support()]
print("selected feature:", list(selected_features))