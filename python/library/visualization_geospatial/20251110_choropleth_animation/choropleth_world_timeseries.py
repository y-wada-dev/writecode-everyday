import pandas as pd
import plotly.express as px

df = pd.read_csv("country_temp_timeseries.csv")

df["year_month"] = pd.PeriodIndex(df["year_month"], freq="M").astype(str)
order = sorted(df["year_month"].unique())
df["year_month"] = pd.Categorical(df["year_month"], categories=order, ordered=True)

fig = px.choropleth(
    df,
    locations="iso3",
    hover_name="country",
    animation_frame="year_month",
    color_continuous_scale="RdYlBu_r",
    projection="natural earth",
    title="Monthly Average Temperature by Country (°C)"
)

fig.update_layout(
    coloraxis_colorbar=dict(title="°C"),
    margin=dict(l=0, r=0, t=50, b=0),
    updatemenus=[{
        "buttons": [
            {"args": [None, {"frame": {"duration": 700, "redraw": True},
                             "fromcurrent": True, "transition": {"duration": 250}}],
             "label": "▶ Play", "method": "animate"},
            {"args": [[None], {"frame": {"duration": 0, "redraw": False},
                               "mode": "immediate",
                               "transition": {"duration": 0}}],
             "label": "⏹ Pause", "method": "animate"}
        ],
        "direction": "left", "pad": {"r": 10, "t": 35},
        "showactive": False, "type": "buttons", "x": 0.1, "y": 0
    }]
)

fig.show()
fig.write_html("choropleth_world_timeseries.html", include_plotlyjs="cdn")
print("HTML file has been saved.")