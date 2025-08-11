import pandas as pd

# csvファイルを読み込む
df = pd.read_csv("sample.csv", encoding="utf-8-sig")
print("読み込んだデータ:sample.csv")

# データ編集

df["年齢"] = df["年齢"] + 1  # 年齢を1歳増やす
print("編集後のデータ:")
print(df)

df["名前"] = df ["名前"].str.upper()

df["勤続年数"] = [2, 3, 1]

print("修正後データ")
print(df)

df.to_csv("sample.csv", index=False, encoding="utf-8-sig")
print("修正後のデータを保存済み")