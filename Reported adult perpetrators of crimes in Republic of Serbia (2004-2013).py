import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Data (2004–2013)
data = {
    "Year": [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013],
    "Total_Offenders": [88453, 100536, 105701, 98702, 101723, 100026, 74279, 88207, 92879, 91411],
    "Known_Offenders": [60641, 62370, 63970, 61992, 67407, 64656, 50870, 59674, 61876, 61560],
    "Males_Count": [54322, 55871, 56888, 55561, 60238, 57358, 44945, 52614, 54652, 54182],
    "Females_Count": [6319, 6499, 7082, 6431, 7169, 7298, 5925, 7060, 7224, 7378],
    "Males_Share": [89.6, 89.6, 88.9, 89.6, 93.0, 88.7, 88.4, 88.2, 88.3, 88.0],
    "Females_Share": [10.4, 10.4, 11.1, 10.4, 7.0, 11.3, 11.6, 11.8, 11.7, 12.0]
}

# Create DataFrame
df = pd.DataFrame(data)

# --- 1. Line Chart: Trend from 2004 to 2013 ---
fig_trend = go.Figure()

# Add series for each category
fig_trend.add_trace(go.Scatter(
    x=df["Year"], y=df["Total_Offenders"], mode="lines+markers",
    name="Total Offenders", line=dict(color="royalblue", width=3),
    marker=dict(size=8, symbol="circle")
))
fig_trend.add_trace(go.Scatter(
    x=df["Year"], y=df["Known_Offenders"], mode="lines+markers",
    name="Known Offenders", line=dict(color="darkorange", width=3),
    marker=dict(size=8, symbol="square")
))
fig_trend.add_trace(go.Scatter(
    x=df["Year"], y=df["Males_Count"], mode="lines+markers",
    name="Males", line=dict(color="dodgerblue", dash="dash"),
    marker=dict(size=8, symbol="triangle-up")
))
fig_trend.add_trace(go.Scatter(
    x=df["Year"], y=df["Females_Count"], mode="lines+markers",
    name="Females", line=dict(color="purple", dash="dot"),
    marker=dict(size=8, symbol="x")
))

# Styling
fig_trend.update_layout(
    title=dict(
        text="Trend of Reported Adult Criminal Offenders in Serbia (2004–2013)",
        x=0.5, font=dict(size=22)
    ),
    xaxis=dict(title="Year", tickmode="array", tickvals=df["Year"], tickfont=dict(size=14)),
    yaxis=dict(title="Number of Offenders", tickfont=dict(size=14)),
    legend=dict(title="Category", font=dict(size=14), orientation="h", y=-0.2),
    template="plotly_white",
    margin=dict(l=40, r=40, t=80, b=80)
)

fig_trend.show()

# --- 2. Bar Chart: Gender Participation (2004–2013) ---
fig_bar = go.Figure()

fig_bar.add_trace(go.Bar(
    x=df["Year"], y=df["Males_Share"],
    name="Males (Share %)", marker_color="dodgerblue"
))
fig_bar.add_trace(go.Bar(
    x=df["Year"], y=df["Females_Share"],
    name="Females (Share %)", marker_color="purple"
))

# Styling
fig_bar.update_layout(
    title=dict(
        text="Gender Participation in Known Adult Offenders in Serbia (2004–2013)",
        x=0.5, font=dict(size=22)
    ),
    xaxis=dict(title="Year", tickmode="array", tickvals=df["Year"], tickfont=dict(size=14)),
    yaxis=dict(title="Share (%)", tickfont=dict(size=14)),
    legend=dict(title="Gender", font=dict(size=14)),
    template="plotly_white",
    margin=dict(l=40, r=40, t=80, b=80),
    barmode="group"
)

fig_bar.show()

# --- 3. Pie Chart: Overall Gender Distribution (2004–2013) ---
# Calculate total counts for males and females across the decade
total_males = df["Males_Count"].sum()
total_females = df["Females_Count"].sum()

# Create DataFrame for pie chart
pie_data = pd.DataFrame({
    "Gender": ["Males", "Females"],
    "Count": [total_males, total_females]
})

fig_pie = px.pie(
    pie_data, names="Gender", values="Count",
    title="Gender Distribution Among Known Adult Offenders in Serbia (2004–2013)",
    color="Gender",
    color_discrete_map={"Males": "dodgerblue", "Females": "purple"}
)

fig_pie.update_traces(
    hoverinfo="label+percent+value", textinfo="percent+label",
    marker=dict(line=dict(color="white", width=2))
)

fig_pie.update_layout(
    title=dict(text="Overall Gender Share Among Adult Offenders in Serbia(2004–2013)", x=0.5, font=dict(size=22))
)

fig_pie.show()
