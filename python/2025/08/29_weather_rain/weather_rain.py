import requests
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Hiragino Sans'

lat, lon = 35.6895, 139.6917

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,precipitation&start=2025-08-01T00:00:00Z&end=2025-08-07T23:00:00Z&timezone=Asia%2FTokyo"

respose = requests.get(url)
respose.raise_for_status()
data = respose.json()

df = pd.DataFrame({
    "時間" : data["hourly"]["time"],
    "気温" : data["hourly"]["temperature_2m"],
    "降水量" : data["hourly"]["precipitation"]
})
df["時間"] = pd.to_datetime(df["時間"])
df = df.set_index("時間")

fig, ax1 = plt.subplots(figsize=(10, 4))


ax1.plot(df.index, df["気温"], color="tab:red", label="気温 (°C)")
ax1.set_xlabel("日付")
ax1.set_ylabel("気温 (°C)", color="tab:red")
ax1.tick_params(axis='y', labelcolor="tab:red")

ax2 = ax1.twinx()
ax2.bar(df.index, df["降水量"], color="tab:blue", alpha=0.3, label="降水量 (mm)")
ax2.set_ylabel("降水量 (mm)", color="tab:blue")
ax2.tick_params(axis='y', labelcolor="tab:blue")

plt.title("1週間の気温と降水量")
plt.show()