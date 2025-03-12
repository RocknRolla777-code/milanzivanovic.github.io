import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Unos podataka
data = {
    "Godina": [2015, 2016, 2017, 2018],
    "Prijavljeni_Ukupno": [3355, 3643, 3465, 2744],
    "Prijavljeni_Muski": [3040, 3281, 3114, 2448],
    "Prijavljeni_Zenski": [315, 362, 351, 296],
    "Osudjeni_Ukupno": [1926, 2032, 1633, 1548],
    "Osudjeni_Muski": [1784, 1880, 1491, 1422],
    "Osudjeni_Zenski": [142, 152, 142, 126],
}

# Kreiranje DataFrame-a
df = pd.DataFrame(data)

# --- 1. Grafikon trenda ---
fig_trend = go.Figure()

# Prijavljeni
fig_trend.add_trace(go.Scatter(
    x=df["Godina"], y=df["Prijavljeni_Ukupno"], mode="lines+markers",
    name="Prijavljeni (Ukupno)", line=dict(color="royalblue", width=3),
    marker=dict(size=8, symbol="circle")
))
fig_trend.add_trace(go.Scatter(
    x=df["Godina"], y=df["Prijavljeni_Muski"], mode="lines+markers",
    name="Prijavljeni (Muški)", line=dict(color="dodgerblue", dash="dash"),
    marker=dict(size=8, symbol="triangle-up")
))
fig_trend.add_trace(go.Scatter(
    x=df["Godina"], y=df["Prijavljeni_Zenski"], mode="lines+markers",
    name="Prijavljeni (Ženski)", line=dict(color="blueviolet", dash="dot"),
    marker=dict(size=8, symbol="x")
))

# Osuđeni
fig_trend.add_trace(go.Scatter(
    x=df["Godina"], y=df["Osudjeni_Ukupno"], mode="lines+markers",
    name="Osuđeni (Ukupno)", line=dict(color="firebrick", width=3),
    marker=dict(size=8, symbol="circle")
))
fig_trend.add_trace(go.Scatter(
    x=df["Godina"], y=df["Osudjeni_Muski"], mode="lines+markers",
    name="Osuđeni (Muški)", line=dict(color="orangered", dash="dash"),
    marker=dict(size=8, symbol="triangle-down")
))
fig_trend.add_trace(go.Scatter(
    x=df["Godina"], y=df["Osudjeni_Zenski"], mode="lines+markers",
    name="Osuđeni (Ženski)", line=dict(color="darkred", dash="dot"),
    marker=dict(size=8, symbol="x")
))

# Stilizacija
fig_trend.update_layout(
    title=dict(
        text="Trend broja prijavljenih i osuđenih maloletnika u Republici Srbiji (2015-2018)",
        x=0.5, font=dict(size=22)
    ),
    xaxis=dict(title="Godina", tickmode="array", tickvals=df["Godina"], tickfont=dict(size=14)),
    yaxis=dict(title="Broj lica", tickfont=dict(size=14)),
    legend=dict(title="Kategorija", font=dict(size=14), orientation="h", y=-0.2),
    template="plotly_white",
    margin=dict(l=40, r=40, t=80, b=80)
)

fig_trend.show()

# --- 2. Uporedni bar grafikon ---
fig_bar = go.Figure()

fig_bar.add_trace(go.Bar(
    x=df["Godina"], y=df["Prijavljeni_Ukupno"],
    name="Prijavljeni (Ukupno)", marker_color="royalblue"
))

fig_bar.add_trace(go.Bar(
    x=df["Godina"], y=df["Osudjeni_Ukupno"],
    name="Osuđeni (Ukupno)", marker_color="firebrick"
))

# Stil
fig_bar.update_layout(
    title=dict(
        text="Poređenje prijavljenih i osuđenih maloletnika u Republici Srbiji (2015-2018)",
        x=0.5, font=dict(size=22)
    ),
    xaxis=dict(title="Godina", tickmode="array", tickvals=df["Godina"], tickfont=dict(size=14)),
    yaxis=dict(title="Broj lica", tickfont=dict(size=14)),
    legend=dict(title="Kategorija", font=dict(size=14)),
    template="plotly_white",
    margin=dict(l=40, r=40, t=80, b=80),
    barmode="group"
)

fig_bar.show()

# --- 3. Udeo po polu: Pie Chart ---
df_polu = pd.DataFrame({
    "Pol": ["Muški", "Ženski"],
    "Prijavljeni": [df["Prijavljeni_Muski"].sum(), df["Prijavljeni_Zenski"].sum()],
    "Osuđeni": [df["Osudjeni_Muski"].sum(), df["Osudjeni_Zenski"].sum()],
})
df_polu = df_polu.melt(id_vars="Pol", var_name="Kategorija", value_name="Broj")

fig_pie = px.pie(
    df_polu, names="Pol", values="Broj", color="Pol",
    title="Udeo muških i ženskih maloletnika (Prijavljeni i Osuđeni)",
    color_discrete_map={"Muški": "royalblue", "Ženski": "pink"}
)

fig_pie.update_traces(
    hoverinfo="label+percent+value", textinfo="percent+label",
    marker=dict(line=dict(color="white", width=2))
)

fig_pie.update_layout(
    title=dict(text="Raspodela prijavljenih i osuđenih po polu u Republici Srbiji (2015-2018)", x=0.5, font=dict(size=22)),
)

fig_pie.show()
