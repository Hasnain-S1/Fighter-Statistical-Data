import streamlit as st
import pandas as pd
from utils.data_processor import get_fighters_by_weight_class, get_fighter_stats
from utils.visualization import create_stats_bar_chart, create_spider_chart
from utils.fight_scraper import get_fighter_stats_with_recent, get_recent_fights

def fighter_profile_page(df):
    st.title("🏅 Fighter Profile")
    
    # Select weight class
    weight_classes = sorted([wc for wc in df['weight_class'].unique() if wc is not None])
    weight_class = st.selectbox("Select Weight Class", weight_classes)
    
    # Filter fighters by weight class
    filtered_df = df[df['weight_class'] == weight_class]
    fighters = sorted(get_fighters_by_weight_class(filtered_df, weight_class))

    # Select a fighter
    fighter_name = st.selectbox("Select Fighter", fighters)

    # Get fighter stats
    fighter_data = get_fighter_stats_with_recent(filtered_df, fighter_name)


    # Display fighter details
    st.markdown(f"## {fighter_name}")
    st.markdown(f"**Record:** {fighter_data['wins']}-{fighter_data['losses']}-{fighter_data['draws']}")
    st.markdown(f"**Height:** {round(fighter_data['height_cm'])} cm")
    st.markdown(f"**Weight:** {round(fighter_data['weight_in_kg'])} kg")
    st.markdown(f"**Reach:** {round(fighter_data['reach_in_cm'])} cm")
    st.markdown(f"**Stance:** {fighter_data['stance']}")

    # Spider Chart for Performance
    st.markdown("### Fighter Attributes")
    fighter_metrics = {
        'Striking': fighter_data.get('significant_striking_accuracy', 0),
        'Grappling': fighter_data.get('takedown_accuracy', 0),
        'Defense': fighter_data.get('significant_strike_defence', 0),
        'Cardio': fighter_data.get('average_fight_time', 0)
    }
    st.plotly_chart(create_spider_chart(fighter_metrics, {}, fighter_name, ""), use_container_width=True)

    # Recent Fights Section
    st.markdown("### Recent Fights")
    recent_fights_df = get_recent_fights(fighter_name)  # Fetch recent fights

    if isinstance(recent_fights_df, pd.DataFrame) and not recent_fights_df.empty:
        st.dataframe(recent_fights_df)  # Display fights as a table
    else:
        st.write("No recent fight data available.")

    # Career Highlights / Achievements
    st.markdown("### Career Highlights")
    st.markdown(f"- Achievements: {fighter_data.get('achievements', 'No achievements recorded')}")

