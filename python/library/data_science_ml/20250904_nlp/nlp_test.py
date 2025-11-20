import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

text = """
Natural Language Processing (NLP) is a field of Artificial Intelligence
that focuses on the interaction between computers and human language.
NLP enables computers to read, understand, and derive meaning from text.
"""

words = [w.strip(".,()").lower() for w in text.split()]

counter = Counter(words)
df = pd.DataFrame(counter.items(), columns=["word", "count"]).sort_values("count", ascending=False)

print(df)

df.set_index("word").plot(kind="bar", figsize=(8, 4), legend=False)
plt.title("Word Frequency")
plt.xlabel("count")
plt.ylabel("word")
plt.show()

