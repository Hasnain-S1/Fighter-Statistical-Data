import random
import streamlit as st

def simulate_fight(fighter1_stats, fighter2_stats):
    """
    Simulate a fight between two fighters based on their stats.
    Returns the winner, the outcome of the fight, and reasoning.
    """
    # Weighting factors for different stats (adjust as necessary)
    stats_weight = {
        'striking_accuracy': 0.4,
        'takedown_accuracy': 0.3,
        'significant_strike_defense': 0.2,
        'average_fight_time': 0.1  # Assuming fighters with higher fight time are more durable
    }

    # Function to safely get a stat (defaults to 0 if missing)
    def get_stat(fighter_stats, stat):
        return fighter_stats.get(stat, 0)

    # Calculate score for each fighter based on stats and weights
    fighter1_score = sum(get_stat(fighter1_stats, key) * stats_weight[key] for key in stats_weight)
    fighter2_score = sum(get_stat(fighter2_stats, key) * stats_weight[key] for key in stats_weight)

    # Randomly give a slight advantage to fighter1 or fighter2 based on their score
    winner = fighter1_stats if random.random() < (fighter1_score / (fighter1_score + fighter2_score)) else fighter2_stats

    # Simulate the fight outcome (KO, TKO, Decision)
    fight_outcome = random.choice(["KO/TKO", "Submission", "Decision"])

    # Generate reasoning based on key stats
    reasoning = ""
    if fight_outcome == "KO/TKO":
        if fighter1_score > fighter2_score:
            reasoning = f"{fighter1_stats['name']} had better striking accuracy and landed more significant strikes."
        else:
            reasoning = f"{fighter2_stats['name']} was able to overwhelm {fighter1_stats['name']} with powerful strikes."
    
    elif fight_outcome == "Submission":
        if fighter1_stats['takedown_accuracy'] > fighter2_stats['takedown_accuracy']:
            reasoning = f"{fighter1_stats['name']} took the fight to the ground with superior takedowns and secured a submission."
        else:
            reasoning = f"{fighter2_stats['name']} controlled the fight with superior grappling and secured a submission."
    
    elif fight_outcome == "Decision":
        if fighter1_score > fighter2_score:
            reasoning = f"{fighter1_stats['name']} outstruck {fighter2_stats['name']} and avoided damage, winning the fight by decision."
        else:
            reasoning = f"{fighter2_stats['name']} managed to outlast {fighter1_stats['name']} with better endurance and defense."

    return winner, fight_outcome, reasoning

def fight_simulation_page(df):
    st.title("🤼 Fight Simulation")
    st.write("Simulate a fight between two UFC fighters and get a predicted outcome.")

    # Weight class selection
    weight_classes = sorted([wc for wc in df['weight_class'].unique() if wc is not None])
    weight_class = st.selectbox("Select Weight Class", weight_classes)

    # Filter fighters by weight class
    filtered_df = df[df['weight_class'] == weight_class]
    fighters = sorted(filtered_df['name'].unique())

    # Select first fighter
    fighter1_name = st.selectbox("Select First Fighter", fighters)
    fighter1_stats = filtered_df[filtered_df['name'] == fighter1_name].iloc[0].to_dict()

    # Select second fighter
    fighter2_name = st.selectbox("Select Second Fighter", [f for f in fighters if f != fighter1_name])
    fighter2_stats = filtered_df[filtered_df['name'] == fighter2_name].iloc[0].to_dict()

    # Display fighter stats
    st.write(f"### {fighter1_name} Stats")
    st.write(f"Record: {fighter1_stats['wins']}-{fighter1_stats['losses']}-{fighter1_stats['draws']}")
    st.write(f"Height: {round(fighter1_stats['height_cm'])} cm")
    st.write(f"Weight: {round(fighter1_stats['weight_in_kg'])} kg")
    st.write(f"Reach: {round(fighter1_stats['reach_in_cm'])} cm")
    st.write(f"Stance: {fighter1_stats['stance']}")

    st.write(f"### {fighter2_name} Stats")
    st.write(f"Record: {fighter2_stats['wins']}-{fighter2_stats['losses']}-{fighter2_stats['draws']}")
    st.write(f"Height: {round(fighter2_stats['height_cm'])} cm")
    st.write(f"Weight: {round(fighter2_stats['weight_in_kg'])} kg")
    st.write(f"Reach: {round(fighter2_stats['reach_in_cm'])} cm")
    st.write(f"Stance: {fighter2_stats['stance']}")

    # Simulate the fight when the button is pressed
    if st.button("Simulate Fight"):
        winner, fight_outcome, reasoning = simulate_fight(fighter1_stats, fighter2_stats)

        # Display fight results
        st.write(f"### Fight Outcome: {fight_outcome}")
        st.write(f"The winner is: {winner['name']}")
        st.write(f"### Reasoning: {reasoning}")

        # Display winner's record after the fight
        st.write(f"**{winner['name']} Record:** {winner['wins']}-{winner['losses']}-{winner['draws']}")
