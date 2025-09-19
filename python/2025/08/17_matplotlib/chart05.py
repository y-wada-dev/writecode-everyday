import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


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

monthly_this = df.resample("ME", on="date")["sales"].sum().rename("2025")

monthly_prev = (monthly_this * 0.9).rename("2024")
monthly_prev.index = monthly_prev.index - pd.DateOffset(years=1)

comp = pd.concat([monthly_prev, monthly_this], axis=1)

comp.index = comp.index.strftime("%Y/%m")

ax = comp.plot(marker="o", figsize=(7, 4))
ax.set_title("Monthly Sales Comparison")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()