import pandas as pd
import numpy as np

df = pd.DataFrame({
    "id": range(1, 11),
    "date": ["2025-01-01", "2025-01-02", "2025/01/03", None, "2025-01-05",
             "2025-01-06", "2025-01-07", "2025-01-08", "2025-13-01", "2025-01-10"],
    "sales": [100, 200, None, 150, 9999, 180, 170, np.nan, 210, 50],
    "category": ["A", "B", "A", "B", "C", "C", None, "B", "A", "A"]
})

print(df)