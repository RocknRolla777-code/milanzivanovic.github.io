import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="Crime Analysis in Serbia(2004–2017)",
    page_icon="📊",
    layout="wide"
)

# --- Full Data Setup (2004–2017) ---
data = {
    "Year": [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017],
    "Total": [
        88453, 100536, 105701, 98702, 101723, 100026, 74279, 88207, 92879,
        91411, 92600, 108759, 96237, 90348
    ],
    "Murder": [
        330, 291, 303, 390, 337, 348, 335, 281, 302,
        220, 198, 252, 196, 192
    ],
    "Serious_Injury": [
        1713, 1635, 1651, 1520, 1517, 1423, 925, 1197, 1201,
        1179, 1041, 1344, 1155, 1053
    ],
    "Minor_Injury": [
        2534, 2547, 2407, 2426, 2468, 2255, 1576, 1823, 1802,
        1770, 1605, 1729, 1658, 1621
    ],
    "Rape": [
        154, 114, 127, 164, 142, 177, 138, 131, 121,
        92, 60, 88, 91, 77
    ],
    "Neglect_Minors": [
        64, 148, 102, 86, 93, 118, 62, 84, 102,
        90, 105, 88, 114, 126
    ],
    "Family_Violence": [
        1009, 1397, 2191, 2550, 3276, 3384, 2837, 3550, 3624,
        3782, 3642, 5040, 7244, 7795
    ],
    "No_Support": [
        1073, 1009, 1074, 1234, 1524, 1742, 1442, 1882, 2141,
        2041, 1822, 2341, 2395, 2195
    ],
    "Theft": [
        29296, 35655, 38209, 32027, 31357, 31552, 19948, 27175, 32293,
        34162, 39081, 44938, 33200, 30312
    ],
    "Robbery": [
        1924, 2208, 2467, 3461, 3343, 3313, 2718, 3190, 3211,
        2818, 3110, 3494, 2149, 1655
    ],
    "Human_Trafficking": [
        69, 68, 50, 51, 51, 50, 71, 53, 55,
        25, 21, 20, 17, 2
    ],
}

df = pd.DataFrame(data)

# Calculate percentage share for stacked bar chart
category_columns = df.columns[2:]
for category in category_columns:
    df[f"{category}_Share"] = (df[category] / df["Total"]) * 100

# Calculate year-to-year percentage changes for heatmap
df_percentage_change = df[category_columns].pct_change().fillna(0) * 100
df_percentage_change["Year"] = df["Year"]

# Melt data for heatmap
df_heatmap = df_percentage_change.melt(id_vars="Year", var_name="Crime_Type", value_name="Percent_Change")

# --- Sidebar Components ---
st.sidebar.title("Crime Analysis Visualizations")
chart_selection = st.sidebar.radio(
    "Choose a visualization:",
    ["Yearly Crime Trends", "Crime Shares (Stacked Bar Chart)", "Year-to-Year Change (Heatmap)"]
)

# --- Visualization Selection ---
if chart_selection == "Yearly Crime Trends in Serbia (2004-2017)":
    st.subheader("📈 Yearly Crime Trends in Serbia (2004–2017)")
    
    # Line chart: Yearly Trends
    fig_line = go.Figure()

    # Add Total trend
    fig_line.add_trace(go.Scatter(
        x=df["Year"], y=df["Total"],
        mode="lines+markers", name="Total Crimes",
        line=dict(color="black", width=3),
        marker=dict(size=8, symbol="circle")
    ))

    # High-contrast `Dark24` palette for other categories
    color_palette = px.colors.qualitative.Dark24

    for i, category in enumerate(category_columns):
        fig_line.add_trace(go.Scatter(
            x=df["Year"], y=df[category],
            mode="lines+markers",
            name=category,
            line=dict(width=2, color=color_palette[i % len(color_palette)], dash="dashdot"),
            marker=dict(size=6)
        ))

    # Customize layout
    fig_line.update_layout(
        title="Yearly Crime Trends (2004–2017)",
        xaxis_title="Year",
        yaxis_title="Number of Crimes",
        legend_title="Crime Type",
        template="plotly_white",
        margin=dict(l=40, r=40, t=80, b=60),
    )
    st.plotly_chart(fig_line, use_container_width=True)


elif chart_selection == "Crime Shares (Stacked Bar Chart)":
    st.subheader("📊 Contribution of Crime Categories (2004–2017)")

    # Stacked bar chart
    fig_bar = go.Figure()

    color_palette_bar = px.colors.qualitative.Plotly
    for i, category in enumerate(category_columns):
        fig_bar.add_trace(go.Bar(
            x=df["Year"], y=df[f"{category}_Share"],
            name=category, marker_color=color_palette_bar[i % len(color_palette_bar)]
        ))

    # Customize layout
    fig_bar.update_layout(
        title="Contribution of Crime Categories (2004–2017)",
        xaxis_title="Year",
        yaxis_title="Percentage Contribution (%)",
        barmode="stack",  # Stacked bar chart
        legend_title="Crime Type",
        template="plotly_white",
        margin=dict(l=40, r=40, t=80, b=60),
    )
    st.plotly_chart(fig_bar, use_container_width=True)


elif chart_selection == "Year-to-Year Change (Heatmap)":
    st.subheader("🌡️ Year-to-Year Percentage Change in Crimes (2004–2017)")
    
    # Heatmap
    fig_heatmap = px.imshow(
        df_percentage_change[category_columns].T,
        labels=dict(x="Year", y="Crime Type", color="Year-to-Year Change (%)"),
        x=df_percentage_change["Year"],
        y=category_columns,
        color_continuous_scale="RdBu",  # Red-Blue for clear positive/negative changes
        title="Year-to-Year Percentage Change in Crimes (2004–2017)"
    )
    
    # Customize heatmap layout
    fig_heatmap.update_layout(
        title_font_size=20,
        margin=dict(l=60, r=60, t=80, b=60),
        xaxis=dict(title="Year", tickvals=df["Year"]),
        yaxis=dict(title="Crime Type")
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)


# Footer
st.sidebar.info("Source: Republic Institute of Statistics in Serbia")
