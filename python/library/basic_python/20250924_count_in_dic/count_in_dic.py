words = ["apple", "banana", "apple", "orange", "banana", "apple"]
count_dict = {}
for w in words:
    count_dict[w] = count_dict.get(w, 0) + 1
print("カウント結果:", count_dict)
