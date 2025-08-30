import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    "売上": np.random.normal(100, 20, 50),
    "広告費": np.random.normal(50, 10, 50),
    "来客数": np.random.normal(200, 30, 50),
    "満足度": np.random.normal(3.5, 0.5, 50)
})

print(df.corr())
