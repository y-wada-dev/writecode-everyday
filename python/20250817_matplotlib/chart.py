import pandas as pd
import matplotlib.pyplot as plt

# sampleData 
df = pd.DataFrame({
    "date": pd.date_range("2025-07-01", periods=31, freq="D"),
    "sales": [100,120,90,130,150,170,160,140,155,180,
              175,190,210,220,205,195,230,240,235,250,
              245,255,260,270,265,280,275,290,300,310,305]
})

df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")

# 折れ線
plt.figure(figsize=(7, 5))
df["sales"].plot(marker="o")
plt.title("Daily Sales")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 4))
df["sales"].plot(label="Daily", alpha=0.6)
df["sales"].rolling(7).mean().plot(label="7-day MA", linewidth=2)
plt.title("Daily Sales with 70day Moving Average")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()