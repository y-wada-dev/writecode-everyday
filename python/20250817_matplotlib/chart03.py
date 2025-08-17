import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# sampleData 
df = pd.DataFrame({
    "date": pd.date_range("2025-07-01", periods=31, freq="D"),
    "sales": [100,120,90,130,150,170,160,140,155,180,
              175,190,210,220,205,195,230,240,235,250,
              245,255,260,270,265,280,275,290,300,310,305]
})

df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")

# 月別集計用の棒グラフ
monthly = df["sales"].resample("ME").sum()

monthly.index = monthly.index.strftime("%Y/%m")

ax = monthly.plot(kind="bar", figsize=(6, 4))

ax.set_title("Monthly Sales")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
plt.tight_layout()
plt.show()
