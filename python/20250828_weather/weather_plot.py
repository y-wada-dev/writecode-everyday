import requests
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Hiragino Sans'

lat, lon = 35.6895, 139.6917

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,precipitation&start=2025-08-01T00:00:00Z&end=2025-08-07T23:00:00Z&timezone=Asia%2FTokyo"

respose = requests.get(url)
data = respose.json()

df = pd.DataFrame({
    "時間" : data["hourly"]["time"],
    "気温" : data["hourly"]["temperature_2m"],
    "降水量" : data["hourly"]["precipitation"]
})
df["時間"] = pd.to_datetime(df["時間"])
df = df.set_index("時間")

df["気温"].plot(figsize=(10, 4))
plt.title("1週間の気温変化")
plt.xlabel("日付")
plt.ylabel("気温 (°C)")
plt.grid(True, alpha=0.3)
plt.show()