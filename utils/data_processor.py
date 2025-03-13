import pandas as pd
from utils.fight_scraper import get_recent_fights  # Import the fight scraper function


def load_and_process_data(file_path):
    df = pd.read_csv(file_path)
    
    # Define UFC weight classes 
    weight_classes = {
        'Strawweight': (0, 52.2),
        'Flyweight': (52.2, 56.7),
        'Bantamweight': (56.7, 61.2),
        'Featherweight': (61.2, 65.8),
        'Lightweight': (65.8, 70.3),
        'Welterweight': (70.3, 77.1),
        'Middleweight': (77.1, 83.9),
        'Light Heavyweight': (83.9, 93.0),
        'Heavyweight': (93.0, 120.2)
    }

    # Assign weight classes based on fighter weight
    df['weight_class'] = None
    for weight_class, (lower, upper) in weight_classes.items():
        mask = (df['weight_in_kg'] > lower) & (df['weight_in_kg'] <= upper)
        df.loc[mask, 'weight_class'] = weight_class

    # Calculate win percentage (handling potential division by zero)
    df['win_percentage'] = df['wins'] / (df['wins'] + df['losses'] + df['draws']).replace(0, 1) * 100

    return df  # Ensure the modified DataFrame is returned

# Function to get fighters by weight class
def get_fighters_by_weight_class(df, weight_class):
    return df[df['weight_class'] == weight_class]['name'].tolist()

# Function to get fighter stats
def get_fighter_stats(df, fighter_name):
    fighter = df[df['name'] == fighter_name]
    return fighter.iloc[0] if not fighter.empty else None

# Function to get key comparison metrics
def get_comparison_metrics(fighter_data):
    if fighter_data is None:
        return {}

    return {
        'Striking Accuracy': fighter_data.get('significant_striking_accuracy', 0),
        'Takedown Accuracy': fighter_data.get('takedown_accuracy', 0),
        'Strike Defense': fighter_data.get('significant_strike_defence', 0),
        'Takedown Defense': fighter_data.get('takedown_defense', 0)
    }

def get_fighter_stats_with_recent(df, fighter_name):
    # Get fighter stats from the dataset
    fighter_stats = get_fighter_stats(df, fighter_name)

    # Fetch recent fights and achievements from fight_scraper
    recent_fights, achievements = get_recent_fights(fighter_name)

    # Add new data to the existing stats
    fighter_stats["recent_fights"] = recent_fights
    fighter_stats["achievements"] = achievements

    return fighter_stats
