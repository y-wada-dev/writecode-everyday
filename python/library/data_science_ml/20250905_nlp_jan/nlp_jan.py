from janome.tokenizer import Tokenizer

t = Tokenizer()

text = "自然言語処理はコンピュータと人間の言語の相互作用を扱う人工知能の分野です。"

words = [token.surface for token in t.tokenize(text)]
print(words)
print(len(words))