import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="Juvenile Crime Trends in Serbia (2015–2018)",
    page_icon="📊",
    layout="wide"
)

# --- Data Input ---
data = {
    "Year": [2015, 2016, 2017, 2018],
    "Reported_Total": [3355, 3643, 3465, 2744],
    "Reported_Male": [3040, 3281, 3114, 2448],
    "Reported_Female": [315, 362, 351, 296],
    "Convicted_Total": [1926, 2032, 1633, 1548],
    "Convicted_Male": [1784, 1880, 1491, 1422],
    "Convicted_Female": [142, 152, 142, 126],
}

df = pd.DataFrame(data)

# --- Sidebar Navigation ---
st.sidebar.title("Visualizations")
chart_selection = st.sidebar.radio(
    "Choose a chart to display:",
    ["Trend of Reported and Convicted", "Comparison of Reported and Convicted", "Gender Distribution"]
)

# --- Chart: Trend of Reported and Convicted ---
if chart_selection == "Trend of Reported and Convicted":
    st.subheader("📈 Trend of Reported and Convicted Juveniles in Serbia (2015–2018)")
    fig_trend = go.Figure()

    # Reported
    fig_trend.add_trace(go.Scatter(
        x=df["Year"], y=df["Reported_Total"], mode="lines+markers",
        name="Reported (Total)", line=dict(color="royalblue", width=3),
        marker=dict(size=8, symbol="circle")
    ))
    fig_trend.add_trace(go.Scatter(
        x=df["Year"], y=df["Reported_Male"], mode="lines+markers",
        name="Reported (Male)", line=dict(color="dodgerblue", dash="dash"),
        marker=dict(size=8, symbol="triangle-up")
    ))
    fig_trend.add_trace(go.Scatter(
        x=df["Year"], y=df["Reported_Female"], mode="lines+markers",
        name="Reported (Female)", line=dict(color="blueviolet", dash="dot"),
        marker=dict(size=8, symbol="x")
    ))

    # Convicted
    fig_trend.add_trace(go.Scatter(
        x=df["Year"], y=df["Convicted_Total"], mode="lines+markers",
        name="Convicted (Total)", line=dict(color="firebrick", width=3),
        marker=dict(size=8, symbol="circle")
    ))
    fig_trend.add_trace(go.Scatter(
        x=df["Year"], y=df["Convicted_Male"], mode="lines+markers",
        name="Convicted (Male)", line=dict(color="orangered", dash="dash"),
        marker=dict(size=8, symbol="triangle-down")
    ))
    fig_trend.add_trace(go.Scatter(
        x=df["Year"], y=df["Convicted_Female"], mode="lines+markers",
        name="Convicted (Female)", line=dict(color="darkred", dash="dot"),
        marker=dict(size=8, symbol="x")
    ))

    fig_trend.update_layout(
        title=dict(
            text="Trend of Reported and Convicted Juveniles in Serbia (2015–2018)",
            x=0.5, font=dict(size=22)
        ),
        xaxis=dict(title="Year", tickmode="array", tickvals=df["Year"], tickfont=dict(size=14)),
        yaxis=dict(title="Number of Individuals", tickfont=dict(size=14)),
        legend=dict(title="Category", font=dict(size=14), orientation="h", y=-0.2),
        template="plotly_white",
        margin=dict(l=40, r=40, t=80, b=80),
    )
    st.plotly_chart(fig_trend, use_container_width=True)

# --- Chart: Comparison Bar Chart ---
elif chart_selection == "Comparison of Reported and Convicted":
    st.subheader("📊 Comparison of Reported and Convicted Juveniles (2015–2018)")
    fig_bar = go.Figure()

    fig_bar.add_trace(go.Bar(
        x=df["Year"], y=df["Reported_Total"],
        name="Reported (Total)", marker_color="royalblue"
    ))
    fig_bar.add_trace(go.Bar(
        x=df["Year"], y=df["Convicted_Total"],
        name="Convicted (Total)", marker_color="firebrick"
    ))

    fig_bar.update_layout(
        title=dict(
            text="Comparison of Reported and Convicted Juveniles in Serbia (2015–2018)",
            x=0.5, font=dict(size=22)
        ),
        xaxis=dict(title="Year", tickmode="array", tickvals=df["Year"], tickfont=dict(size=14)),
        yaxis=dict(title="Number of Individuals", tickfont=dict(size=14)),
        legend=dict(title="Category", font=dict(size=14)),
        template="plotly_white",
        margin=dict(l=40, r=40, t=80, b=80),
        barmode="group"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# --- Chart: Gender Distribution Pie Chart ---
elif chart_selection == "Gender Distribution":
    st.subheader("🟣 Gender Distribution of Reported and Convicted Juveniles (2015–2018)")
    df_gender = pd.DataFrame({
        "Gender": ["Male", "Female"],
        "Reported": [df["Reported_Male"].sum(), df["Reported_Female"].sum()],
        "Convicted": [df["Convicted_Male"].sum(), df["Convicted_Female"].sum()],
    })

    df_gender = df_gender.melt(id_vars="Gender", var_name="Category", value_name="Count")

    fig_pie = px.pie(
        df_gender, names="Gender", values="Count", color="Gender",
        title="Gender Distribution of Reported and Convicted Juveniles",
        color_discrete_map={"Male": "royalblue", "Female": "pink"}
    )

    fig_pie.update_traces(
        hoverinfo="label+percent+value", textinfo="percent+label",
        marker=dict(line=dict(color="white", width=2))
    )

    fig_pie.update_layout(
        title=dict(text="Gender Distribution of Reported and Convicted Juveniles in Serbia (2015–2018)", x=0.5, font=dict(size=22)),
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# --- Footer ---
st.sidebar.info("Source: Republic Institute of Statistics in Serbia")
