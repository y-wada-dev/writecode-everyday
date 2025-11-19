import random
import time

# 出題する単語リスト
words = [
    "python", "function", "variable", "iterator", "generator",
    "lambda", "decorator", "exception", "list", "dictionary",
    "comprehension", "tuple", "set", "module", "package",
    "class", "inheritance", "polymorphism", "encapsulation", "abstraction",
    "algorithm", "recursion", "syntax", "debugging", "runtime",
    "interpreter", "compiler", "expression", "statement", "boolean",
    "parameter", "argument", "keyword", "immutable", "mutable",
    "context", "namespace", "scope", "attribute", "method",
    "instance", "constructor", "destructor", "annotation", "iterator",
    "generator", "yield", "closure", "singleton", "prototype"
]

NUMBER_OF_WORDS = 5

def typing_practice():
    print("タイピング練習を開始します。")
    print(f"次の {NUMBER_OF_WORDS} 個の単語をできるだけ早く入力してください。")
    
    # ランダムに単語を選ぶ
    selected_words = random.sample(words, NUMBER_OF_WORDS)
    print("単語:", " ".join(selected_words))
    
    # タイマー開始
    start_time = time.time()
    
    # ユーザー入力
    user_input = input("入力: ")
    
    # タイマー終了
    end_time = time.time()
    
    # 結果表示
    elapsed_time = end_time - start_time
    print(f"入力時間: {elapsed_time:.2f}秒")
    
    # 正誤判定
    if user_input.strip() == " ".join(selected_words):
        print("正解です！")
    else:
        print("不正解です。")
        print(f"正しい入力: {' '.join(selected_words)}")
    print("練習を終了します。")

if __name__ == "__main__":
    typing_practice()