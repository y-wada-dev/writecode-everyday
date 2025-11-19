import pandas as pd

# サンプルデータ
data = {
    "名前": ["tanaka","sato","suzuki"],
    "年齢": [25, 30, 22],
    "職業": ["エンジニア", "デザイナー", "マネージャー"]
}

df = pd.DataFrame(data)

print("サンプルデータ:")
print(df)

# csvファイルに保存
df.to_csv("sample.csv", index=False, encoding="utf-8-sig")
print("csvファイルに保存済み: sample.csv")


