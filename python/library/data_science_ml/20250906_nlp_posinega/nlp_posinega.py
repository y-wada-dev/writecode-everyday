from collections import Counter

texts = [
    "I love this movie, it was fantastic and wonderful!",
    "This is the worst film I have ever seen, terrible and boring.",
    "The food was okay, not great but not bad either."
]

positive_words = {"love", "fantastic", "wonderful", "great", "good", "amazing"}
negative_words = {"worst", "terrible", "boring", "bad", "awful"}

def analyze_setiment(text):
    words = [w.strip(".,!?").lower() for w in text.split()]
    pos = sum(1 for w in words if w in positive_words)
    neg = sum(1 for w in words if w in negative_words)
    score = pos - neg

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

for text in texts:
    print(f"{text} -> {analyze_setiment(text)}")