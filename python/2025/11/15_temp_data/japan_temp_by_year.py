import pandas as pd

df =pd.read_csv("japan_temp_by_year.csv")
df.head()
print("データの先頭5行:")
print(df.head())

df.describe()
print("データの基本統計量:")
print(df.describe())

df_year = df.groupby("year")["temp_c"].mean()
print("年ごとの平均気温:")
print(df_year)

