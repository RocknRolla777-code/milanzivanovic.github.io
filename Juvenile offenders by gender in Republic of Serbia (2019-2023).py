import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

# --- Streamlit App Setup ---
# App title and configuration
st.set_page_config(
    page_title="Juvenile Crime Trends in Serbia",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Trends in Juvenile Crime (2019–2023) in Serbia")
st.markdown(
    """
    This web app provides visual insights into juvenile crime trends in the Republic of Serbia 
    between **2019 and 2023**. Use the menu on the left to choose the type of visualization.
    """
)

# --- DATA ---
data = {
    "Godina": [2019, 2020, 2021, 2022, 2023],
    "Prijavljeni_Ukupno": [2903, 2524, 2513, 2410, 2598],
    "Prijavljeni_Muski": [2611, 2280, 2267, 2121, 2313],
    "Prijavljeni_Zenski": [292, 244, 246, 289, 285],
    "Osudjeni_Ukupno": [1676, 1239, 1383, 1213, 1454],
    "Osudjeni_Muski": [1518, 1133, 1262, 1094, 1313],
    "Osudjeni_Zenski": [158, 106, 121, 119, 141],
}
df = pd.DataFrame(data)

# --- Sidebar Menu ---
st.sidebar.title("Navigation")
chart_selection = st.sidebar.radio(
    "Choose a chart to display:",
    ["Trend Analysis", "Comparative Bar Chart", "Gender Distribution"]
)

# --- Visualization Logic ---
if chart_selection == "Trend Analysis":
    st.subheader("📈 Trend Analysis (2019–2023)")
    fig_trend = go.Figure()

    # Add Prijavljeni traces
    fig_trend.add_trace(go.Scatter(
        x=df["Godina"], y=df["Prijavljeni_Ukupno"], mode="lines+markers",
        name="Prijavljeni (Ukupno)", line=dict(color="royalblue", width=3),
        marker=dict(size=8)
    ))
    fig_trend.add_trace(go.Scatter(
        x=df["Godina"], y=df["Prijavljeni_Muski"], mode="lines+markers",
        name="Prijavljeni (Muški)", line=dict(color="dodgerblue", dash="dash"),
        marker=dict(size=8)
    ))
    fig_trend.add_trace(go.Scatter(
        x=df["Godina"], y=df["Prijavljeni_Zenski"], mode="lines+markers",
        name="Prijavljeni (Ženski)", line=dict(color="blueviolet", dash="dot"),
        marker=dict(size=8)
    ))

    # Add Osudjeni traces
    fig_trend.add_trace(go.Scatter(
        x=df["Godina"], y=df["Osudjeni_Ukupno"], mode="lines+markers",
        name="Osuđeni (Ukupno)", line=dict(color="firebrick", width=3),
        marker=dict(size=8)
    ))
    fig_trend.add_trace(go.Scatter(
        x=df["Godina"], y=df["Osudjeni_Muski"], mode="lines+markers",
        name="Osuđeni (Muški)", line=dict(color="orangered", dash="dash"),
        marker=dict(size=8)
    ))
    fig_trend.add_trace(go.Scatter(
        x=df["Godina"], y=df["Osudjeni_Zenski"], mode="lines+markers",
        name="Osuđeni (Ženski)", line=dict(color="darkred", dash="dot"),
        marker=dict(size=8)
    ))

    # Chart styling
    fig_trend.update_layout(
        title="Trend Analysis: Juvenile Crime (2019–2023)",
        xaxis_title="Year",
        yaxis_title="Number of Individuals",
        legend_title="Category",
        template="plotly_white",
        margin=dict(l=40, r=40, t=60, b=60),
    )
    st.plotly_chart(fig_trend, use_container_width=True)

elif chart_selection == "Comparative Bar Chart":
    st.subheader("📊 Comparative Bar Chart (2019–2023)")
    fig_bar = go.Figure()
    fig_bar.add_trace(go.Bar(
        x=df["Godina"], y=df["Prijavljeni_Ukupno"],
        name="Prijavljeni (Ukupno)", marker_color="royalblue"
    ))
    fig_bar.add_trace(go.Bar(
        x=df["Godina"], y=df["Osudjeni_Ukupno"],
        name="Osuđeni (Ukupno)", marker_color="firebrick"
    ))

    # Chart styling
    fig_bar.update_layout(
        title="Comparative Bar Chart: Reported vs. Convicted (2019–2023)",
        xaxis_title="Year",
        yaxis_title="Number of Individuals",
        legend_title="Category",
        template="plotly_white",
        margin=dict(l=40, r=40, t=60, b=60),
        barmode="group"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

elif chart_selection == "Gender Distribution":
    st.subheader("🧑‍🤝‍🧑 Gender Distribution Analysis")
    # Gender data
    df_polu = pd.DataFrame({
        "Pol": ["Muški", "Ženski"],
        "Prijavljeni": [df["Prijavljeni_Muski"].sum(), df["Prijavljeni_Zenski"].sum()],
        "Osuđeni": [df["Osudjeni_Muski"].sum(), df["Osudjeni_Zenski"].sum()],
    })
    df_polu = df_polu.melt(id_vars="Pol", var_name="Category", value_name="Count")

    # Pie chart
    fig_pie = px.pie(
        df_polu, names="Pol", values="Count", color="Pol",
        title="Gender Distribution of Juvenile Crime in Serbia",
        color_discrete_map={"Muški": "royalblue", "Ženski": "pink"}
    )
    fig_pie.update_traces(
        hoverinfo="label+percent+value",
        textinfo="percent+label",
        marker=dict(line=dict(color="white", width=2))
    )
    st.plotly_chart(fig_pie, use_container_width=True)

st.sidebar.info("📆 Data from the Republic of Serbia (2019–2023)")
