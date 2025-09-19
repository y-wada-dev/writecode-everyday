import pandas as pd

index = list(range(1, 999))
columns = list(range(1, 999))

multiplication_table = pd.DataFrame(
    [[i * j for j in columns] for i in index],
    index=index, 
    columns=columns)

print("九九の表:")
print(multiplication_table)

# 保存するファイル名
file_name = "multiplication_table.csv"

# CSVファイルに保存
multiplication_table.to_csv(file_name, index=True)
print(f"九九の表を {file_name} に保存しました")