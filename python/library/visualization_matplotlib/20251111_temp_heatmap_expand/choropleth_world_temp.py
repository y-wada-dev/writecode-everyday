import pandas as pd
import plotly.express as px

df = pd.read_csv("country_temp_sample.csv")

fig = px.choropleth(
    df,
    locations="iso3",                 # ISO3コード
    color="temp_c",                   # 塗り分け値
    hover_name="country",             # ホバー表示名
    color_continuous_scale="RdYlBu_r",# 寒暖色（青=低/赤=高）
    projection="natural earth",
    title="Average Temperature (°C)"
)

fig.update_layout(coloraxis_colorbar=dict(title="Temp (C)"))
fig.show()