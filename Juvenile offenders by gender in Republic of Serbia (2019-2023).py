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

st.title("📊 Juvenile Crime Trends in Serbia (2019–2023)")
st.markdown(
    """
    This web app visualizes trends and insights into juvenile crime statistics 
    in the Republic of Serbia between **2019 and 2023**. Use the menu on the left 
    to explore the visualizations.
    """
)

# --- DATA ---
data = {
    "Year": [2019, 2020, 2021, 2022, 2023],
    "Reported_Total": [2903, 2524, 2513, 2410, 2598],
    "Reported_Males": [2611, 2280, 2267, 2121, 2313],
    "Reported_Females": [292, 244, 246, 289, 285],
    "Convicted_Total": [1676, 1239, 1383, 1213, 1454],
    "Convicted_Males": [1518, 1133, 1262, 1094, 1313],
    "Convicted_Females": [158, 106, 121, 119, 141],
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
    st.subheader("📈 Juvenile Crime Trends (2019–2023)")
    fig_trend = go.Figure()

    # Add Reported traces
    fig_trend.add_trace(go.Scatter(
        x=df["Year"], y=df["Reported_Total"], mode="lines+markers",
        name="Reported (Total)", line=dict(color="royalblue", width=3),
        marker=dict(size=8)
    ))
    fig_trend.add_trace(go.Scatter(
        x=df["Year"], y=df["Reported_Males"], mode="lines+markers",
        name="Reported (Males)", line=dict(color="dodgerblue", dash="dash"),
        marker=dict(size=8)
    ))
    fig_trend.add_trace(go.Scatter(
        x=df["Year"], y=df["Reported_Females"], mode="lines+markers",
        name="Reported (Females)", line=dict(color="blueviolet", dash="dot"),
        marker=dict(size=8)
    ))

    # Add Convicted traces
    fig_trend.add_trace(go.Scatter(
        x=df["Year"], y=df["Convicted_Total"], mode="lines+markers",
        name="Convicted (Total)", line=dict(color="firebrick", width=3),
        marker=dict(size=8)
    ))
    fig_trend.add_trace(go.Scatter(
        x=df["Year"], y=df["Convicted_Males"], mode="lines+markers",
        name="Convicted (Males)", line=dict(color="orangered", dash="dash"),
        marker=dict(size=8)
    ))
    fig_trend.add_trace(go.Scatter(
        x=df["Year"], y=df["Convicted_Females"], mode="lines+markers",
        name="Convicted (Females)", line=dict(color="darkred", dash="dot"),
        marker=dict(size=8)
    ))

    # Chart styling
    fig_trend.update_layout(
        title="Juvenile Crime Trends: Reported vs. Convicted (2019–2023)",
        xaxis_title="Year",
        yaxis_title="Number of Individuals",
        legend_title="Category",
        template="plotly_white",
        margin=dict(l=40, r=40, t=60, b=60),
    )
    st.plotly_chart(fig_trend, use_container_width=True)

elif chart_selection == "Comparative Bar Chart":
    st.subheader("📊 Comparative Analysis of Reported vs. Convicted (2019–2023)")
    fig_bar = go.Figure()
    fig_bar.add_trace(go.Bar(
        x=df["Year"], y=df["Reported_Total"],
        name="Reported (Total)", marker_color="royalblue"
    ))
    fig_bar.add_trace(go.Bar(
        x=df["Year"], y=df["Convicted_Total"],
        name="Convicted (Total)", marker_color="firebrick"
    ))

    # Chart styling
    fig_bar.update_layout(
        title="Reported vs. Convicted Juvenile Crimes (2019–2023)",
        xaxis_title="Year",
        yaxis_title="Number of Individuals",
        legend_title="Category",
        template="plotly_white",
        margin=dict(l=40, r=40, t=60, b=60),
        barmode="group"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

elif chart_selection == "Gender Distribution":
    st.subheader("🧑‍🤝‍🧑 Gender Distribution in Juvenile Crime")
    # Gender data
    df_gender = pd.DataFrame({
        "Gender": ["Male", "Female"],
        "Reported": [df["Reported_Males"].sum(), df["Reported_Females"].sum()],
        "Convicted": [df["Convicted_Males"].sum(), df["Convicted_Females"].sum()],
    })
    df_gender = df_gender.melt(id_vars="Gender", var_name="Category", value_name="Count")

    # Pie chart
    fig_pie = px.pie(
        df_gender, names="Gender", values="Count", color="Gender",
        title="Gender Distribution of Juvenile Crime in Serbia",
        color_discrete_map={"Male": "royalblue", "Female": "pink"}
    )
    fig_pie.update_traces(
        hoverinfo="label+percent+value",
        textinfo="percent+label",
        marker=dict(line=dict(color="white", width=2))
    )
    st.plotly_chart(fig_pie, use_container_width=True)

st.sidebar.info("📆 Data from the Republic of Serbia (2019–2023)")
