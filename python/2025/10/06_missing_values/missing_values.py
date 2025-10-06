import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# データ読み込み
df = pd.read_csv("sample_missing.csv", parse_dates=["date"])
print("===元データ===")
print(df)

