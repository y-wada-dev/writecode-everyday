import yfinance as yf
import matplotlib.pyplot as plt

ticker = yf.Ticker("7203.T")
df = ticker.history(period="1y")

df["Close"].plot(figsize=(10,4))
plt.title("Toyota Stock Price")
plt.xlabel("Date")
plt.ylabel("Price (JPY)")
plt.grid(True, alpha=0.3)
plt.show()

df["Close"].plot(alpha=0.5, label="Close")
df["Close"].rolling(window=20).mean().plot(label="20-day MA")
plt.legend()
plt.show()

