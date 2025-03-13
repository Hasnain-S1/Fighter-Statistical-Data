import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def get_fighter_sherdog_url(fighter_name):
    """Finds the Sherdog URL for a given fighter by searching Sherdog's website."""
    search_url = f"https://www.sherdog.com/stats/fightfinder?SearchTxt={fighter_name.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        return None
    
    soup = BeautifulSoup(response.text, "html.parser")
    fighter_link = soup.find("a", href=re.compile("/fighter/"))
    
    if fighter_link:
        return "https://www.sherdog.com" + fighter_link["href"]
    
    return None

def get_recent_fights(fighter_name):
    """Scrapes recent fight history from Sherdog."""
    fighter_url = get_fighter_sherdog_url(fighter_name)
    if not fighter_url:
        return f"No fighter found for {fighter_name}"
    
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(fighter_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the correct fight history table
    fight_rows = soup.select(".module_fight_history table.new_table.fighter tbody tr")
    
    fight_data = []
    for row in fight_rows[1:6]:  # Get the last 5 fights
        columns = row.find_all("td")
        if len(columns) < 6:
            continue

        fight = {
            "Result": columns[0].text.strip(),
            "Opponent": columns[1].text.strip(),
            "Event": columns[2].text.strip(),
            "Method": columns[3].text.strip(),
            "Round": columns[4].text.strip(),
            "Time": columns[5].text.strip()
        }
        fight_data.append(fight)
    
    return pd.DataFrame(fight_data) if fight_data else "No recent fight data available."

def get_fighter_stats_with_recent(df, fighter_name):
    """Retrieves fighter stats from the DataFrame and adds recent fight data."""
    fighter = df[df['name'] == fighter_name]
    
    if fighter.empty:
        return None  # Fighter not found
    
    fighter_data = fighter.iloc[0].to_dict()  # Convert row to dictionary
    
    # Fetch recent fights
    recent_fights_df = get_recent_fights(fighter_name)
    
    # Store recent fights as a list of dictionaries
    if isinstance(recent_fights_df, pd.DataFrame) and not recent_fights_df.empty:
        fighter_data["recent_fights"] = recent_fights_df.to_dict(orient="records")
    else:
        fighter_data["recent_fights"] = "No recent fight data available."
    
    return fighter_data

# Example Usage (Testing)
if __name__ == "__main__":
    fighter_name = "Jon Jones"  # You can change this to any fighter's name
    fighter_url = get_fighter_sherdog_url(fighter_name)
    print("Sherdog URL:", fighter_url)
