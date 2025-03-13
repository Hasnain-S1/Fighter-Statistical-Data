import streamlit as st
import pandas as pd

# Ensure you import the necessary function from your data_processor module
from utils.data_processor import get_fighter_stats

def historical_comparisons_page(df):
    st.title("📜 Historical Comparisons")
    st.write("Compare modern fighters with historical legends based on statistics.")

    # List of historical fighters (add Khabib, Fedor, Tony Ferguson)
    historical_fighters = [
        "Anderson Silva", "Georges St-Pierre", "Jon Jones", "Khabib Nurmagomedov",
        "Fedor Emelianenko", "Tony Ferguson", "Daniel Cormier", "Stipe Miocic"
    ]
    
    # Select weight class
    weight_classes = sorted([wc for wc in df['weight_class'].unique() if wc is not None])
    weight_class = st.selectbox("Select Weight Class", weight_classes)
    
    # Filter fighters by weight class
    filtered_df = df[df['weight_class'] == weight_class]

    # Select a modern fighter
    modern_fighter = st.selectbox("Select Modern Fighter", sorted(filtered_df['name'].unique()))

    # Select a historical fighter
    historical_fighter = st.selectbox("Select Historical Fighter", historical_fighters)

    # Get stats for modern fighter
    modern_fighter_data = get_fighter_stats(filtered_df, modern_fighter)
    
    # Historical fighter stats placeholder, assuming historical fighter data is available:
    # You may need to manually input historical stats for this to work.
    # (This would ideally be fetched similarly, but if the historical fighters' data is not in the same format, you'd want to have them hardcoded)
    historical_fighter_data = {
        "significant_strikes_landed_per_minute": 4.0,  # Example values
        "significant_striking_accuracy": 0.55,
        "significant_strikes_absorbed_per_minute": 3.5,
        "significant_strike_defence": 0.65,
        "average_takedowns_landed_per_15_minutes": 1.2,
        "takedown_accuracy": 0.6,
        "takedown_defense": 0.85,
        "average_submissions_attempted_per_15_minutes": 0.8,
        "reach_to_height": 0.9
    }

    # Compare significant strikes
    st.markdown("### Striking Comparison")
    st.write(f"**Modern Fighter's Significant Strikes:** {modern_fighter_data.get('significant_strikes_landed_per_minute', 0)} strikes/min")
    st.write(f"**Historical Fighter's Significant Strikes:** {historical_fighter_data['significant_strikes_landed_per_minute']} strikes/min")
    
    # Compare significant striking accuracy
    st.write(f"**Modern Fighter's Striking Accuracy:** {modern_fighter_data.get('significant_striking_accuracy', 0) * 100}%")
    st.write(f"**Historical Fighter's Striking Accuracy:** {historical_fighter_data['significant_striking_accuracy'] * 100}%")
    
    # Insights on striking
    if modern_fighter_data.get('significant_strikes_landed_per_minute', 0) > historical_fighter_data['significant_strikes_landed_per_minute']:
        st.write("Modern fighter lands more significant strikes per minute.")
    else:
        st.write("Historical fighter lands more significant strikes per minute.")
    
    if modern_fighter_data.get('significant_striking_accuracy', 0) > historical_fighter_data['significant_striking_accuracy']:
        st.write("Modern fighter has a higher striking accuracy.")
    else:
        st.write("Historical fighter has a higher striking accuracy.")

    # Compare significant strikes absorbed per minute
    st.markdown("### Striking Defense Comparison")
    st.write(f"**Modern Fighter's Strikes Absorbed Per Minute:** {modern_fighter_data.get('significant_strikes_absorbed_per_minute', 0)}")
    st.write(f"**Historical Fighter's Strikes Absorbed Per Minute:** {historical_fighter_data['significant_strikes_absorbed_per_minute']}")

    if modern_fighter_data.get('significant_strikes_absorbed_per_minute', 0) < historical_fighter_data['significant_strikes_absorbed_per_minute']:
        st.write("Modern fighter absorbs fewer strikes per minute.")
    else:
        st.write("Historical fighter absorbs fewer strikes per minute.")

    # Compare takedown accuracy and defense
    st.markdown("### Grappling Comparison")
    st.write(f"**Modern Fighter's Takedown Accuracy:** {modern_fighter_data.get('takedown_accuracy', 0) * 100}%")
    st.write(f"**Historical Fighter's Takedown Accuracy:** {historical_fighter_data['takedown_accuracy'] * 100}%")

    st.write(f"**Modern Fighter's Takedown Defense:** {modern_fighter_data.get('takedown_defense', 0) * 100}%")
    st.write(f"**Historical Fighter's Takedown Defense:** {historical_fighter_data['takedown_defense'] * 100}%")

    if modern_fighter_data.get('takedown_accuracy', 0) > historical_fighter_data['takedown_accuracy']:
        st.write("Modern fighter has higher takedown accuracy.")
    else:
        st.write("Historical fighter has higher takedown accuracy.")

    if modern_fighter_data.get('takedown_defense', 0) > historical_fighter_data['takedown_defense']:
        st.write("Modern fighter has better takedown defense.")
    else:
        st.write("Historical fighter has better takedown defense.")

    # Compare submission attempts
    st.markdown("### Submission Comparison")
    st.write(f"**Modern Fighter's Submission Attempts:** {modern_fighter_data.get('average_submissions_attempted_per_15_minutes', 0)} submissions/15 min")
    st.write(f"**Historical Fighter's Submission Attempts:** {historical_fighter_data['average_submissions_attempted_per_15_minutes']} submissions/15 min")

    if modern_fighter_data.get('average_submissions_attempted_per_15_minutes', 0) > historical_fighter_data['average_submissions_attempted_per_15_minutes']:
        st.write("Modern fighter attempts more submissions per 15 minutes.")
    else:
        st.write("Historical fighter attempts more submissions per 15 minutes.")

    # Compare reach-to-height ratio
    st.markdown("### Physical Comparison")
    st.write(f"**Modern Fighter's Reach-to-Height Ratio:** {modern_fighter_data.get('reach_to_height', 0)}")
    st.write(f"**Historical Fighter's Reach-to-Height Ratio:** {historical_fighter_data['reach_to_height']}")

    if modern_fighter_data.get('reach_to_height', 0) > historical_fighter_data['reach_to_height']:
        st.write("Modern fighter has a better reach-to-height ratio.")
    else:
        st.write("Historical fighter has a better reach-to-height ratio.")

    # Insights on fighter comparison
    st.markdown("### Insights")
    st.write("Based on the statistical comparison, consider how each fighter's style and strengths contribute to their legacy.")
