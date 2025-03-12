import pandas as pd

def load_and_process_data(file_path):
    df = pd.read_csv(file_path)
    
    # Add a 'weight_class' column based on UFC official weight classes
    weight_classes = {
        'Strawweight': (0, 52.2),
        'Flyweight': (52.2, 56.7),
        'Bantamweight': (56.7, 61.2),
        'Featherweight': (61.2, 65.8),
        'Lightweight': (65.8, 70.3),
        'Welterweight': (70.3, 77.1),
        'Middleweight': (77.1, 83.9),
        'Light Heavyweight': (83.9, 93.0),
        'Heavyweight': (93.0, 120.2),
        'Super Heavyweight': (120.2, float('inf'))
    }
    
    df['weight_class'] = None
    for weight_class, (lower, upper) in weight_classes.items():
        mask = (df['weight_in_kg'] > lower) & (df['weight_in_kg'] <= upper)
        df.loc[mask, 'weight_class'] = weight_class
    
    df['win_percentage'] = df['wins'] / (df['wins'] + df['losses'] + df['draws']) * 100
    return df

def get_fighters_by_weight_class(df, weight_class):
    return df[df['weight_class'] == weight_class]['name'].tolist()

def get_fighter_stats(df, fighter_name):
    return df[df['name'] == fighter_name].iloc[0]
def get_comparison_metrics(fighter_data):
    return {
        'Striking Accuracy': fighter_data.get('significant_striking_accuracy', 0),
        'Takedown Accuracy': fighter_data.get('takedown_accuracy', 0),
        'Strike Defense': fighter_data.get('significant_strike_defence', 0),
        'Takedown Defense': fighter_data.get('takedown_defense', 0)
    }

