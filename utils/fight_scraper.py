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
        print(f"Error: Failed to get response from Sherdog, status code {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    fighter_link = soup.find("a", href=re.compile("/fighter/"))

    if fighter_link:
        fighter_url = "https://www.sherdog.com" + fighter_link["href"]
        print(f"Fighter URL found: {fighter_url}")
        return fighter_url
    else:
        print(f"Fighter URL not found for {fighter_name}")
        return None

def get_recent_fights(fighter_name):
    """Scrapes recent fight history from Sherdog."""
    fighter_url = get_fighter_sherdog_url(fighter_name)
    if not fighter_url:
        return []  # Return an empty list instead of a string

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(fighter_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Look for fight history section
    fight_rows = soup.select("table.fight_history tr")

    if not fight_rows:
        print(f"No fight history found for {fighter_name}")
        return []  # Return an empty list instead of a string
    
    fight_data = []
    for row in fight_rows[1:6]:  # Get the last 5 fights (skip header)
        columns = row.find_all("td")
        if len(columns) < 6:
            continue  # Skip rows that don't have enough data

        fight = {
            "Result": columns[0].text.strip(),
            "Opponent": columns[1].text.strip(),
            "Event": columns[2].text.strip(),
            "Method": columns[3].text.strip(),
            "Round": columns[4].text.strip(),
            "Time": columns[5].text.strip()
        }
        fight_data.append(fight)
    
    return fight_data if fight_data else []  # Always return a list

def get_fighter_stats_with_recent(df, fighter_name):
    """Retrieves fighter stats from the DataFrame and adds recent fight data."""
    fighter = df[df['name'] == fighter_name]
    
    if fighter.empty:
        return None  # Fighter not found
    
    fighter_data = fighter.iloc[0].to_dict()  # Convert row to dictionary
    
    # Fetch recent fights
    recent_fights = get_recent_fights(fighter_name)
    
    # Ensure recent_fights is always a list
    fighter_data["recent_fights"] = recent_fights if isinstance(recent_fights, list) else []
    
    # Career highlights
    fighter_data["achievements"] = fighter_data.get('achievements', 'No achievements recorded')
    
    return fighter_data
