import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# --- Streamlit App Setup ---
st.set_page_config(
    page_title="Tourism Statistics",
    page_icon="🌍",
    layout="wide"
)

# App Title
st.title("🌍 Tourism Statistics: Number of Tourist Nights by Country (2023)")
st.markdown(
    """
    Explore interactive visualizations showing the number of tourist nights and package arrangements 
    for various countries in **2023**. Use the sidebar to switch between visualizations.
    """
)

# --- Data Preparation ---
data = {
    "Country": [
        "Austria", "Bosnia and Herzegovina", "Bulgaria", "Canada", 
        "Czech Republic", "Germany", "Egypt", "Spain", "France", 
        "United Kingdom", "Greece", "Hungary", "Italy", "Montenegro", 
        "North Macedonia", "Poland", "Romania", "Serbia", 
        "Russian Federation", "Slovenia", "Slovakia", "Tunisia", 
        "Turkey", "Latin America and Central America", "Asian Countries", 
        "United States", "Other European Countries", 
        "Other African Countries", "Australia and New Zealand", 
        "Other Non-European Countries"
    ],
    "TouristNights": [
        9437, 19611, 11688, 23, 11175, 3113, 41805, 24680, 8090,
        716, 467452, 17980, 49647, 41084, 8724, 2396, 2801, 
        173083, 411, 10067, 242, 29879, 85651, 4017, 11036, 
        621, 27093, 3968, 83, 2672
    ],
    "PackageArrangements": [
        26145, 62876, 79922, 92, 33871, 8858, 374498, 171373, 
        39160, 3494, 4485790, 75604, 198897, 336941, 31528, 
        7119, 5849, 600671, 1280, 31915, 485, 28275, 658323, 
        43975, 103414, 4508, 17608, 41651, 779, 18800
    ]
}
df = pd.DataFrame(data)

# Map country names to ISO Alpha-3 codes (required for geoplot)
country_iso_mapping = {
    "Austria": "AUT", "Bosnia and Herzegovina": "BIH", "Bulgaria": "BGR",
    "Canada": "CAN", "Czech Republic": "CZE", "Germany": "DEU", "Egypt": "EGY",
    "Spain": "ESP", "France": "FRA", "United Kingdom": "GBR", 
    "Greece": "GRC", "Hungary": "HUN", "Italy": "ITA", 
    "Montenegro": "MNE", "North Macedonia": "MKD", "Poland": "POL", 
    "Romania": "ROU", "Serbia": "SRB", "Russian Federation": "RUS",
    "Slovenia": "SVN", "Slovakia": "SVK", "Tunisia": "TUN", "Turkey": "TUR",
    "Latin America and Central America": "LAM", "Asian Countries": "ASM",
    "United States": "USA", "Other European Countries": "EUR",
    "Other African Countries": "AFR", "Australia and New Zealand": "NZL", 
    "Other Non-European Countries": "OTH"
}
df["ISO_Code"] = df["Country"].map(country_iso_mapping)

# --- Sidebar Navigation ---
st.sidebar.title("Visualizations")
chart_selection = st.sidebar.radio(
    "Choose a visualization:",
    ["Interactive Map", "Bar Chart"]
)

# --- Visualization Logic ---
if chart_selection == "Interactive Map":
    st.subheader("🌍 Interactive Map of Tourist Nights (2023)")
    fig_map = px.choropleth(
        df,
        locations="ISO_Code",  # Locations based on ISO codes
        color="TouristNights",  # Color based on Tourist Nights column
        hover_name="Country",  # Country name on hover
        title="Number of Tourist Nights by Country (2023)",
        color_continuous_scale="Viridis"  # Enhanced color visibility
    )

    # Map layout updates
    fig_map.update_geos(showcoastlines=True, showland=True, fitbounds="locations")
    fig_map.update_layout(
        title_font_size=20,
        geo=dict(showframe=False, showcoastlines=True, projection_type="equirectangular")
    )
    st.plotly_chart(fig_map, use_container_width=True)

elif chart_selection == "Bar Chart":
    st.subheader("📊 Bar Chart Comparison of Tourist Nights")
    fig_bar = go.Figure()

    # Add Tourist Nights bar
    fig_bar.add_trace(
        go.Bar(
            x=df["Country"], 
            y=df["TouristNights"], 
            name="Tourist Nights", 
            marker_color="blue"
        )
    )

    # Add Package Arrangements bar
    fig_bar.add_trace(
        go.Bar(
            x=df["Country"], 
            y=df["PackageArrangements"], 
            name="Package Arrangements", 
            marker_color="orange"
        )
    )

    # Customize bar chart layout
    fig_bar.update_layout(
        title="Comparison of Tourist Nights and Package Arrangements (2023)",
        xaxis_title="Countries",
        yaxis_title="Number of Nights",
        barmode="group",  # Grouped bar charts
        legend_title="Type of Arrangement",
        xaxis=dict(tickangle=45),  # Rotate country labels for readability
        title_font_size=20,
        margin=dict(l=40, r=40, t=60, b=60)
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# Footer information in sidebar
st.sidebar.info("📆 Data source: Tourism data for 2023.")
