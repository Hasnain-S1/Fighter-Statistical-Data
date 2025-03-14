import streamlit as st
import random
import pandas as pd

def simulate_fight(fighter1_stats, fighter2_stats):
    """Simulate a fight between two fighters and return the winner, outcome, and reasoning."""
    
    # Weighting factors for different stats to determine fight advantage
    stats_weight = {
        'significant_striking_accuracy': 0.4,  # Striking accuracy plays the biggest role
        'takedown_accuracy': 0.3,  # Takedown accuracy affects ground control
        'significant_strike_defense': 0.2,  # Ability to avoid strikes is important
        'average_takedowns_landed_per_15_minutes': 0.1,  # Takedowns per 15 minutes give slight advantage
    }

    # Function to safely get a stat value, returns 0 if the stat is missing
    def get_stat(stats, stat):
        return stats.get(stat, 0)

    # Calculate a total score for each fighter based on their stats and weights
    fighter1_score = sum(get_stat(fighter1_stats, key) * stats_weight[key] for key in stats_weight)
    fighter2_score = sum(get_stat(fighter2_stats, key) * stats_weight[key] for key in stats_weight)

    # Determine the winner with a probability based on score comparison
    winner = fighter1_stats if random.random() < (fighter1_score / (fighter1_score + fighter2_score)) else fighter2_stats

    # Randomly select a fight outcome type
    fight_outcome = random.choice(["KO/TKO", "Submission", "Decision"])

    # Generate reasoning for the outcome
    reasoning = ""
    if fight_outcome == "KO/TKO":
        reasoning = f"{winner['name']} won with superior striking accuracy and landed powerful shots."
    elif fight_outcome == "Submission":
        reasoning = f"{winner['name']} controlled the fight with superior grappling and secured a submission."
    else:
        reasoning = f"{winner['name']} had better defense and outlasted their opponent to win by decision."

    return winner, fight_outcome, reasoning

def fight_simulation_page(df):
    """Streamlit interface for fight simulation"""
    st.title("🤼 Fight Simulation")
    st.write("Simulate a fight between two UFC fighters and get a predicted outcome.")

    # Step 1: Select a weight class
    weight_classes = sorted([wc for wc in df['weight_class'].unique() if wc is not None])
    weight_class = st.selectbox("Select Weight Class", weight_classes)

    # Step 2: Filter fighters by the selected weight class
    filtered_df = df[df['weight_class'] == weight_class]
    fighters = sorted(filtered_df['name'].unique())

    # Step 3: Select the first fighter
    fighter1_name = st.selectbox("Select First Fighter", fighters)
    fighter1_stats = filtered_df[filtered_df['name'] == fighter1_name].iloc[0].to_dict()

    # Step 4: Select the second fighter (excluding the first fighter from selection)
    fighter2_name = st.selectbox("Select Second Fighter", [f for f in fighters if f != fighter1_name])
    fighter2_stats = filtered_df[filtered_df['name'] == fighter2_name].iloc[0].to_dict()

    # Step 5: Display selected fighters' stats
    st.write(f"### 🥋 {fighter1_name} Stats")
    st.write(f"**Record:** {fighter1_stats['wins']}-{fighter1_stats['losses']}-{fighter1_stats['draws']}")
    st.write(f"**Height:** {round(fighter1_stats['height_cm'])} cm")
    st.write(f"**Weight:** {round(fighter1_stats['weight_in_kg'])} kg")
    st.write(f"**Reach:** {round(fighter1_stats['reach_in_cm'])} cm")
    st.write(f"**Stance:** {fighter1_stats['stance']}")

    st.write(f"### 🥊 {fighter2_name} Stats")
    st.write(f"**Record:** {fighter2_stats['wins']}-{fighter2_stats['losses']}-{fighter2_stats['draws']}")
    st.write(f"**Height:** {round(fighter2_stats['height_cm'])} cm")
    st.write(f"**Weight:** {round(fighter2_stats['weight_in_kg'])} kg")
    st.write(f"**Reach:** {round(fighter2_stats['reach_in_cm'])} cm")
    st.write(f"**Stance:** {fighter2_stats['stance']}")

    # Step 6: Simulate the fight when the button is clicked
    if st.button("Simulate Fight"):
        winner, fight_outcome, reasoning = simulate_fight(fighter1_stats, fighter2_stats)

        # Step 7: Display the fight results
        st.write(f"## 🏆 Fight Outcome: {fight_outcome}")
        st.write(f"🥇 **Winner:** {winner['name']}")
        st.write(f"### 🔍 Reasoning: {reasoning}")

        # Step 8: Display the winner's updated record
        st.write(f"📊 **{winner['name']} Record:** {winner['wins']}-{winner['losses']}-{winner['draws']}")
