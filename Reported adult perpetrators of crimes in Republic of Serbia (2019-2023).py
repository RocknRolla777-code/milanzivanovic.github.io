import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Data for 2019–2023
data = {
    "Year": [2019, 2020, 2021, 2022, 2023],
    "Total_Offenders": [92797, 74394, 80632, 82958, 74504],
    "Known_Offenders": [64695, 51863, 54240, 51414, 47760],
    "Males_Count": [55517, 44257, 46232, 43576, 40678],
    "Females_Count": [9178, 7606, 8008, 7838, 7082],
    "Males_Share": [85.8, 85.3, 85.2, 84.8, 85.2],
    "Females_Share": [14.2, 14.7, 14.8, 15.2, 14.8]
}

# Create DataFrame
df = pd.DataFrame(data)

# --- 1. Line Chart: Trends in 2019–2023 ---
fig_trend = go.Figure()

# Add series for total offenders, known offenders, males, and females
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
        text="Trend of Reported Adult Criminal Offenders in Serbia (2019–2023)",
        x=0.5, font=dict(size=22)
    ),
    xaxis=dict(title="Year", tickmode="array", tickvals=df["Year"], tickfont=dict(size=14)),
    yaxis=dict(title="Number of Offenders", tickfont=dict(size=14)),
    legend=dict(title="Category", font=dict(size=14), orientation="h", y=-0.2),
    template="plotly_white",
    margin=dict(l=40, r=40, t=80, b=80)
)

fig_trend.show()

# --- 2. Bar Chart: Gender Participation (2019–2023) ---
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
        text="Gender Participation in Known Adult Offenders in Serbia (2019–2023)",
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

# --- 3. Pie Chart: Overall Gender Distribution (2019–2023) ---
# Aggregate total counts for males and females over the 5 years
total_males = df["Males_Count"].sum()
total_females = df["Females_Count"].sum()

# Create DataFrame for pie chart
pie_data = pd.DataFrame({
    "Gender": ["Males", "Females"],
    "Count": [total_males, total_females]
})

fig_pie = px.pie(
    pie_data, names="Gender", values="Count",
    title="Gender Distribution Among Known Adult Offenders in Serbia (2019–2023)",
    color="Gender",
    color_discrete_map={"Males": "dodgerblue", "Females": "purple"}
)

fig_pie.update_traces(
    hoverinfo="label+percent+value", textinfo="percent+label",
    marker=dict(line=dict(color="white", width=2))
)

fig_pie.update_layout(
    title=dict(text="Overall Gender Share Among Adult Offenders in Serbia (2019–2023)", x=0.5, font=dict(size=22))
)

fig_pie.show()
