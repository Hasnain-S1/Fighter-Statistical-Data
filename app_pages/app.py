import sys
import os
import streamlit as st
import pandas as pd

# Ensure utils module is found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import functions and page modules
from utils.data_processor import (
    load_and_process_data,
    get_fighters_by_weight_class,
    get_fighter_stats,
    get_comparison_metrics
)
from utils.visualization import create_spider_chart
from app_pages.fighter_profile import fighter_profile_page
from app_pages.fight_simulation import fight_simulation_page
from app_pages.historical_comparisons import historical_comparisons_page
from app_pages.weight_class_breakdown import weight_class_breakdown_page
from app_pages.trivia import trivia_page

# 🌟 Set Global Page Configuration
st.set_page_config(
    page_title="UFC Fighter Statistics Dashboard",
    page_icon="🥊",
    layout="wide"
)

# 🌟 Global Styles for the App
st.markdown("""
    <style>
        /* Background Color */
        body {
            background-color: #1e1e1e;
            color: white;
        }

        /* Title & Headers */
        h1, h2, h3 {
            text-align: center;
            color: #ff4b4b;
        }

        /* Customizing Buttons */
        div.stButton > button {
            background-color: #ff4b4b;
            color: white;
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
            transition: 0.3s;
        }

        div.stButton > button:hover {
            background-color: #cc0000;
        }

        /* Sidebar Customization */
        section[data-testid="stSidebar"] {
            background-color: #333333;
            color: white;
        }

        /* Table Styling */
        table {
            width: 100%;
            text-align: center;
            border-collapse: collapse;
        }

        th {
            background-color: #ff4b4b;
            color: white;
            padding: 10px;
        }

        td {
            padding: 8px;
            border-bottom: 1px solid #555;
        }
    </style>
""", unsafe_allow_html=True)

# 🔹 Load and process data
@st.cache_data
def load_data():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'ufc-fighters-statistics-cleaned.csv')
    return load_and_process_data(file_path)

df = load_data()

# 🔹 Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Go to:", 
    ["🏠 Main Dashboard", "👊 Fighter Profile", "🤼 Fight Simulation", "📊 Historical Comparisons", "⚖️ Weight Class Breakdown", "❓ Trivia"]
)

# 🔹 Page Selection Logic
if page == "🏠 Main Dashboard":
    st.title("🥊 UFC Fighter Statistics Dashboard")
    st.markdown("Compare fighters and analyze their statistics across different weight classes.")

    # ✅ Fighter Selection UI
    weight_classes_male = ['Flyweight', 'Bantamweight', 'Featherweight', 'Lightweight', 'Welterweight', 'Middleweight', 'Light Heavyweight', 'Heavyweight']
    weight_classes_female = ['Strawweight', 'Flyweight', 'Bantamweight', 'Featherweight']
    weight_class_options = weight_classes_male + weight_classes_female  

    weight_class = st.sidebar.selectbox("Select Weight Class", weight_class_options)

    filtered_df = df[df['weight_class'] == weight_class]
    fighters = sorted(get_fighters_by_weight_class(filtered_df, weight_class))

    col1, col2 = st.columns(2)

    with col1:
        fighter1 = st.selectbox("Select First Fighter", fighters, key='fighter1')
        fighter1_data = get_fighter_stats(filtered_df, fighter1)

    with col2:
        remaining_fighters = sorted([f for f in fighters if f != fighter1])
        fighter2 = st.selectbox("Select Second Fighter", remaining_fighters, key='fighter2')
        fighter2_data = get_fighter_stats(filtered_df, fighter2)

    # ✅ Display Fighter Stats
    st.markdown("### Fighter Comparison")

    stats_col1, stats_col2 = st.columns(2)

    with stats_col1:
        st.markdown(f"#### {fighter1}")
        st.markdown(f"**Record:** {fighter1_data['wins']}-{fighter1_data['losses']}-{fighter1_data['draws']}")
        st.markdown(f"**Height:** {round(fighter1_data['height_cm'])} cm")
        st.markdown(f"**Weight:** {round(fighter1_data['weight_in_kg'])} kg")
        st.markdown(f"**Reach:** {round(fighter1_data['reach_in_cm'])} cm")
        st.markdown(f"**Stance:** {fighter1_data['stance']}")

    with stats_col2:
        st.markdown(f"#### {fighter2}")
        st.markdown(f"**Record:** {fighter2_data['wins']}-{fighter2_data['losses']}-{fighter2_data['draws']}")
        st.markdown(f"**Height:** {round(fighter2_data['height_cm'])} cm")
        st.markdown(f"**Weight:** {round(fighter2_data['weight_in_kg'])} kg")
        st.markdown(f"**Reach:** {round(fighter2_data['reach_in_cm'])} cm")
        st.markdown(f"**Stance:** {fighter2_data['stance']}")

    # ✅ Performance Comparison Chart
    st.markdown("### Performance Comparison")
    fighter1_metrics = get_comparison_metrics(fighter1_data)
    fighter2_metrics = get_comparison_metrics(fighter2_data)

    spider_chart = create_spider_chart(
        fighter1_metrics,
        fighter2_metrics,
        fighter1,
        fighter2
    )
    st.plotly_chart(spider_chart, use_container_width=True)

    # ✅ Footer
    st.markdown("---")
    st.markdown("Data source: UFC Fighter Statistics Dataset")

elif page == "👊 Fighter Profile":
    fighter_profile_page(df)
elif page == "🤼 Fight Simulation":
    fight_simulation_page(df)
elif page == "📊 Historical Comparisons":
    historical_comparisons_page(df)
elif page == "⚖️ Weight Class Breakdown":
    weight_class_breakdown_page(df)
elif page == "❓ Trivia":
    trivia_page()
