import pandas as pd
import matplotlib.pyplot as plt

# sampleData 
data = {
    "date": pd.date_range("2025-07-01", periods=62, freq="D"),
    "item": (["A"]*31 + ["B"]*31),
    "sales": [100,120,90,130,150,170,160,140,155,180,175,190,210,220,205,195,230,240,235,250,
              245,255,260,270,265,280,275,290,300,310,305] +
             [80,95,85,100,120,130,110,115,118,125,130,135,140,150,145,148,155,160,158,165,
              170,175,178,180,182,185,188,190,195,200,205]
}

# print(data)

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M")

# ピボットする
pv = df.pivot_table(index="month", columns="item", values="sales", aggfunc="sum")
# print(pv)

# グループ別の月別集計用の棒グラフ 
ax = pv.plot(kind="bar", figsize=(7,4))
ax.set_title("Monthly Sales by Item")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()