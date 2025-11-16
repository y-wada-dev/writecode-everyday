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

df_pref = df.groupby("pref_name")["temp_c"].mean().sort_values(ascending=False)
print("都道府県ごとの平均気温:")
print(df_pref)

pivot = df.pivot_table(
    index="pref_name",
    columns="year",
    values="temp_c"
)

print("都道府県ごとの年別気温ピボットテーブル:")
print(pivot)

max_each_year = df.groupby("year").apply(lambda x: x.loc[x["temp_c"].idxmax()])
min_each_year = df.groupby("year").apply(lambda x: x.loc[x["temp_c"].idxmin()])

print("各年の最高気温記録:")
print(max_each_year[["year", "pref_name", "temp_c"]])
print("各年の最低気温記録:")
print(min_each_year[["year", "pref_name", "temp_c"]])

df_change = (
    df[df["year"] == 2016].set_index("pref_code")["temp_c"] -
    df[df["year"] == 2015].set_index("pref_code")["temp_c"]
)

df_change = df_change.sort_values(ascending=False)
print("2015年から2016年の気温変化（都道府県別）:")
print(df_change)