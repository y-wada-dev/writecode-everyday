from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

df = pd.DataFrame({
    "sales": [100, 200, 300, 400],
    "ad_spend": [5, 10, 15, 20]
})

scaler = StandardScaler()
scaled = scaler.fit_transform(df)
df_scaled = pd.DataFrame(scaled, columns=df.columns)
print(df_scaled)

scaler = MinMaxScaler()
normalized = scaler.fit_transform(df)
df_norm = pd.DataFrame(normalized, columns=df.columns)
print(df_norm)