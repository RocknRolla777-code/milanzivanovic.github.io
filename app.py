import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

# --- Streamlit App Setup ---

# App title and description
st.set_page_config(
    page_title="Serbia Criminal Offenders Analysis",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Serbia Criminal Offenders Analysis (2004–2023)")
st.markdown(
    """
    Explore data visualizations of reported adult offenders in the Republic of Serbia 
    from **2004 to 2023**. Use the navigation options to view trends, gender participation, 
    and overall distribution.
    """
)

# --- Data Preparation ---
data = {
    "Year": list(range(2004, 2024)),
    "Total_Offenders": [
        88453, 100536, 105701, 98702, 101723, 100026, 74279, 88207,
        92879, 91411, 92600, 108759, 96237, 90348, 92874, 92797,
        74394, 80632, 82958, 74504,
    ],
    "Known_Offenders": [
        60641, 62370, 63970, 61992, 67407, 64656, 50870, 59674,
        61876, 61560, 54568, 64226, 67089, 61767, 63903, 64695,
        51863, 54240, 51414, 47760,
    ],
    "Males_Count": [
        54322, 55871, 56888, 55561, 60238, 57358, 44945, 52614,
        54652, 54182, 47458, 55722, 57488, 52827, 54471, 55517,
        44257, 46232, 43576, 40678,
    ],
    "Females_Count": [
        6319, 6499, 7082, 6431, 7169, 7298, 5925, 7060,
        7224, 7378, 7110, 8504, 9601, 8940, 9432, 9178,
        7606, 8008, 7838, 7082,
    ],
    "Males_Share": [
        89.6, 89.6, 88.9, 89.6, 93.0, 88.7, 88.4, 88.2,
        88.3, 88.0, 87.0, 86.8, 85.7, 85.5, 85.2, 85.8,
        85.3, 85.2, 84.8, 85.2,
    ],
    "Females_Share": [
        10.4, 10.4, 11.1, 10.4, 7.0, 11.3, 11.6, 11.8,
        11.7, 12.0, 13.0, 13.2, 14.3, 14.5, 14.8, 14.2,
        14.7, 14.8, 15.2, 14.8,
    ]
}

df = pd.DataFrame(data)

# --- Sidebar Menu ---
st.sidebar.title("Navigation")
chart_selection = st.sidebar.radio(
    "Choose a Chart to Display:",
    ["Trend Analysis", "Gender Participation", "Gender Distribution"]
)

# --- Visualization Logic ---

if chart_selection == "Trend Analysis":
    st.subheader("📈 Trend Analysis (2004–2023)")
    fig_trend = go.Figure()

    # Add offenders and gender breakdown trends
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

    # Style the chart
    fig_trend.update_layout(
        title=dict(
            text="Trend of Reported Adult Criminal Offenders in Serbia (2004–2023)",
            x=0.5, font=dict(size=22)
        ),
        xaxis=dict(title="Year", tickmode="array", tickvals=df["Year"], tickfont=dict(size=14)),
        yaxis=dict(title="Number of Offenders", tickfont=dict(size=14)),
        legend=dict(title="Category", font=dict(size=14), orientation="h", y=-0.2),
        template="plotly_white",
        margin=dict(l=40, r=40, t=80, b=80)
    )

    st.plotly_chart(fig_trend, use_container_width=True)

elif chart_selection == "Gender Participation":
    st.subheader("📊 Gender Participation Analysis (2004–2023)")
    fig_bar = go.Figure()

    fig_bar.add_trace(go.Bar(
        x=df["Year"], y=df["Males_Share"], name="Males (Share %)",
        marker_color="dodgerblue"
    ))
    fig_bar.add_trace(go.Bar(
        x=df["Year"], y=df["Females_Share"], name="Females (Share %)",
        marker_color="purple"
    ))

    # Style the chart
    fig_bar.update_layout(
        title=dict(
            text="Gender Participation in Known Adult Offenders in Serbia (2004–2023)",
            x=0.5, font=dict(size=22)
        ),
        xaxis=dict(title="Year", tickfont=dict(size=14)),
        yaxis=dict(title="Share (%)", tickfont=dict(size=14)),
        legend=dict(title="Gender", font=dict(size=14)),
        template="plotly_white",
        margin=dict(l=40, r=40, t=80, b=80),
        barmode="group"
    )

    st.plotly_chart(fig_bar, use_container_width=True)

elif chart_selection == "Gender Distribution":
    st.subheader("🧑‍🤝‍🧑 Overall Gender Distribution (2004–2023)")
    # Aggregate the totals
    total_males = df["Males_Count"].sum()
    total_females = df["Females_Count"].sum()

    # Prepare pie chart data and create chart
    pie_data = pd.DataFrame({
        "Gender": ["Males", "Females"],
        "Count": [total_males, total_females]
    })

    fig_pie = px.pie(
        pie_data, names="Gender", values="Count",
        color="Gender",
        color_discrete_map={"Males": "dodgerblue", "Females": "purple"}
    )

    fig_pie.update_traces(
        hoverinfo="label+percent+value", textinfo="percent+label",
        marker=dict(line=dict(color="white", width=2))
    )

    fig_pie.update_layout(
        title=dict(text="Overall Gender Share Among Adult Offenders in Serbia (2004–2023)", x=0.5, font=dict(size=22))
    )

    st.plotly_chart(fig_pie, use_container_width=True)

st.sidebar.info("📆 Data from the Republic of Serbia (2004–2023).")
