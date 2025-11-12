import pandas as pd
import plotly.express as px
import json

# === GeoJSON 読み込み ===
with open("japan_prefectures.geojson", "r") as f:
    geojson = json.load(f)

# === サンプルデータ ===
df = pd.DataFrame({
    "pref": ["東京都", "大阪府", "北海道", "愛知県", "福岡県"],
    "value": [72, 65, 40, 58, 52],
})

# === Choropleth ===
fig = px.choropleth(
    df,
    geojson=geojson,
    featureidkey="properties.nam_ja",  # GeoJSON内の都道府県名
    locations="pref",                  # データ側の列
    color="value",                     # 色づけする値
    color_continuous_scale="YlOrRd",
    range_color=[40, 75],
    title="日本の都道府県ヒートマップ",
)

# === 地図の調整 ===
fig.update_geos(
    visible=False,
    fitbounds="locations",
    center={"lat": 36, "lon": 138},
    projection_scale=20,
)

# === 欠損地域（データなし）を薄いグレーに ===
fig.update_traces(
    marker_line_width=0.5,
    marker_line_color="white",
    marker=dict(line=dict(color="white", width=0.3)),
    # ここ ↓ が重要
    marker_opacity=1,
    # データなし領域の色指定
    zmin=40,
    zmax=75,
    hovertemplate="%{location}<br>値=%{z}<extra></extra>",
)

# Plotlyの仕様では「missing color」を直接設定できないので、
# GeoJSON 全域の DataFrame を作って補完するのが正攻法です。
# 以下のように全都道府県を埋めるとグレー表示が可能です。

# --- 補完用：全都道府県を用意してmerge ---
all_prefs = pd.DataFrame({"pref": [f["properties"]["nam_ja"] for f in geojson["features"]]})
merged = all_prefs.merge(df, on="pref", how="left")  # 欠損はNaN

fig = px.choropleth(
    merged,
    geojson=geojson,
    featureidkey="properties.nam_ja",
    locations="pref",
    color="value",
    color_continuous_scale="YlOrRd",
    range_color=[40, 75],
    title="日本の都道府県ヒートマップ（欠損＝グレー）",
)

fig.update_geos(
    visible=False,
    fitbounds="locations",
    center={"lat": 36, "lon": 138},
    projection_scale=20,
)

# 欠損値の塗りを薄グレーに
fig.update_traces(
    marker_line_width=0.3,
    marker_line_color="white",
    marker=dict(line=dict(color="white", width=0.3)),
    hovertemplate="%{location}<br>値=%{z}<extra></extra>",
    # これが効く！
    zmin=40, zmax=75,
    showscale=True,
)

# 欠損部分の色（NaN）は `coloraxis_colorbar` で設定
fig.update_layout(
    coloraxis_colorbar=dict(title="value"),
    coloraxis=dict(
        colorbar_title="value",
        cmin=40, cmax=75,
        colorbar_tickvals=[40, 50, 60, 70],
        colorbar_ticktext=["40", "50", "60", "70"],
        # 欠損データ色
        colorbar_outlinecolor="gray",
        colorbar_outlinewidth=0.5,
        colorbar_bgcolor="#ddd"
    )
)

fig.show()
