import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("japan_temp_by_year_scaled.csv")

sns.set_theme(style="whitegrid")

plt.rcParams["font.family"] = 'Hiragino Sans' 


df_year = df.groupby("year")["temp_c"].mean().reset_index()

plt.figure(figsize=(8, 4))
plt.plot(df_year["year"], df_year["temp_c"], marker="o")
plt.title("全国平均気温の推移 (2010-2016)")
plt.xlabel("年")
plt.ylabel("平均気温 (°C)")
plt.xticks(df_year["year"])
plt.tight_layout()
plt.show()