import sys
import os

# Ensure utils module is found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd

from utils.data_processor import (
    load_and_process_data,
    get_fighters_by_weight_class,
    get_fighter_stats,
    get_comparison_metrics
)
from utils.visualization import create_spider_chart, create_stats_bar_chart

# Page config (must be the first Streamlit command)
st.set_page_config(
    page_title="UFC Fighter Statistics Dashboard",
    page_icon="🥊",
    layout="wide"
)

# Load custom CSS
css_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'styles.css')
with open(css_path) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load and process data
@st.cache_data
def load_data():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'attached_assets', 'ufc-fighters-statistics-cleaned.csv')
    return load_and_process_data(file_path)

df = load_data()

# Header
st.title("🥊 UFC Fighter Statistics Dashboard")
st.markdown("Compare fighters and analyze their statistics across different weight classes")

# Sidebar
st.sidebar.title("Fighter Selection")

# Gender selection
gender = st.sidebar.radio("Select Gender", ['Male', 'Female'])
filtered_df = df[df['gender'] == gender]

# Weight class selection
weight_classes_male = [
    'Flyweight', 'Bantamweight', 'Featherweight', 'Lightweight', 
    'Welterweight', 'Middleweight', 'Light Heavyweight', 'Heavyweight'
]
weight_classes_female = [
    'Strawweight', 'Flyweight', 'Bantamweight', 'Featherweight'
]

weight_class_options = weight_classes_male if gender == "Male" else weight_classes_female

weight_class = st.sidebar.selectbox("Select Weight Class", weight_class_options)

# Filter dataset based on weight class
filtered_df = filtered_df[filtered_df['weight_class'] == weight_class]

# Get fighters in selected weight class
fighters = get_fighters_by_weight_class(filtered_df, weight_class)

# Fighter selection
col1, col2 = st.columns(2)

with col1:
    fighter1 = st.selectbox("Select First Fighter", fighters, key='fighter1')
    fighter1_data = get_fighter_stats(filtered_df, fighter1)

with col2:
    remaining_fighters = [f for f in fighters if f != fighter1]
    fighter2 = st.selectbox("Select Second Fighter", remaining_fighters, key='fighter2')
    fighter2_data = get_fighter_stats(filtered_df, fighter2)

# Display fighter comparison
st.markdown("### Fighter Comparison")

# Basic stats comparison
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

# Spider chart comparison
st.markdown("### Performance Comparison")

fighter1_metrics = get_comparison_metrics(fighter1_data)
fighter2_metrics = get_comparison_metrics(fighter2_data)

spider_chart = create_spider_chart(
    fighter1_metrics,
    fighter2_metrics,
    fighter1,
    fighter2
)
st.plotly_chart(spider_chart, use_container_width=True, key="spider")

# Detailed statistics
st.markdown("### Detailed Statistics")

detailed_col1, detailed_col2 = st.columns(2)

with detailed_col1:
    st.markdown(f"#### {fighter1} - Strike Statistics")
    strike_stats = {
        'Strikes Landed/Min': fighter1_data['significant_strikes_landed_per_minute'],
        'Strike Accuracy': fighter1_data['significant_striking_accuracy'],
        'Strikes Absorbed/Min': fighter1_data['significant_strikes_absorbed_per_minute'],
        'Strike Defense': fighter1_data['significant_strike_defence']
    }
    st.plotly_chart(create_stats_bar_chart(strike_stats, "Strike Statistics"), use_container_width=True, key=f"{fighter1}_stats")

with detailed_col2:
    st.markdown(f"#### {fighter2} - Strike Statistics")
    strike_stats = {
        'Strikes Landed/Min': fighter2_data['significant_strikes_landed_per_minute'],
        'Strike Accuracy': fighter2_data['significant_striking_accuracy'],
        'Strikes Absorbed/Min': fighter2_data['significant_strikes_absorbed_per_minute'],
        'Strike Defense': fighter2_data['significant_strike_defence']
    }
    st.plotly_chart(create_stats_bar_chart(strike_stats, "Strike Statistics"), use_container_width=True, key=f"{fighter2}_stats")

# Footer
st.markdown("---")
st.markdown("Data source: UFC Fighter Statistics Dataset")




