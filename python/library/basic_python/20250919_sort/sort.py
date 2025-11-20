# This is a simple Python script to sort a list of numbers.
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print("ソート後のリスト:", numbers)

# This script sorts a list of numbers in ascending order and prints the sorted list.
sorted_numbers = sorted(numbers)
print("ソートされたリスト:", sorted_numbers)

# The sorted() function returns a new sorted list from the elements of any iterable.
sorted_numbers_desc = sorted(numbers, reverse=True)
print("降順にソートされたリスト:", sorted_numbers_desc)

words = ["banana","apple", "cherry"]
words.sort()
print("ソート後の単語リスト:", words)


sorted_words = sorted(words)
print("ソートされた単語リスト:", sorted_words)

sorted_words_desc = sorted(words, reverse=True)
print("降順にソートされた単語リスト:", sorted_words_desc)

sorted_legth = sorted(words, key=len)
print("長さでソートされた単語リスト:", sorted_legth)

data = [("apple", 3), ("banana", 2), ("cherry", 5)]
data.sort(key=lambda x: x[1])
print("値でソートされたデータ:", data)

data_array ={
    "apple": 3,
    "banana": 2,
    "cherry": 5
}
sorted_data = sorted(data_array.items(), key=lambda x: x[1])
print("値でソートされた辞書データ:", sorted_data)