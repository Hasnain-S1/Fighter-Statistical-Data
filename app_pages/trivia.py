import streamlit as st
import pandas as pd
import os

# Path for the leaderboard CSV file
LEADERBOARD_FILE = "trivia_leaderboard.csv"

# Ensure leaderboard file exists
if not os.path.exists(LEADERBOARD_FILE):
    df = pd.DataFrame(columns=["Username", "Score"])
    df.to_csv(LEADERBOARD_FILE, index=False)

def get_valid_answers():
    """Returns a dictionary of valid answers including full names, nicknames, and case variations."""
    return {
        "Georges St-Pierre": ["georges st-pierre", "Georges St-Pierre", "gsp", "GSP"],
        "Conor McGregor": ["conor mcgregor", "Conor McGregor", "the notorious", "The Notorious"],
        "Khabib Nurmagomedov": ["khabib nurmagomedov", "Khabib Nurmagomedov", "the eagle", "The Eagle"],
        "Anderson Silva": ["anderson silva", "Anderson Silva", "the spider", "The Spider"],
        "Tony Ferguson": ["tony ferguson", "Tony Ferguson", "el cucuy", "El Cucuy"],
        "Jorge Masvidal": ["jorge masvidal", "Jorge Masvidal", "gamebred", "Gamebred"],
        "Charles Oliveira": ["charles oliveira", "Charles Oliveira", "do bronx", "Do Bronx"],
        "Ronda Rousey": ["ronda rousey", "Ronda Rousey", "rowdy", "Rowdy"]
    }

def trivia_page():
    """UFC Trivia Page"""
    st.title("❓ UFC Trivia")
    st.write("Test your knowledge with UFC-related trivia questions!")

    # User input for the leaderboard
    username = st.text_input("Enter your name for the leaderboard:")

    # List of trivia questions
    questions = [
        {"question": "Who holds the most UFC title defenses in history?", "answer": "Georges St-Pierre"},
        {"question": "Which UFC fighter is known as 'The Notorious'?", "answer": "Conor McGregor"},
        {"question": "Who is the longest reigning UFC Lightweight Champion?", "answer": "Khabib Nurmagomedov"},
        {"question": "Which fighter holds the record for the most consecutive UFC title defenses?", "answer": "Anderson Silva"},
        {"question": "Which fighter is known for his 'Darce Choke' submission?", "answer": "Tony Ferguson"},
        {"question": "Who was the first fighter to win a UFC championship in two different weight classes?", "answer": "Conor McGregor"},
        {"question": "Who has the fastest knockout in UFC history?", "answer": "Jorge Masvidal"},
        {"question": "Who is the UFC fighter known for being undefeated and retiring with a perfect record?", "answer": "Khabib Nurmagomedov"},
        {"question": "Which UFC fighter was nicknamed 'The Spider'?", "answer": "Anderson Silva"},
        {"question": "Which UFC fighter has the most submissions in UFC history?", "answer": "Charles Oliveira"},
        {"question": "Who was the first UFC fighter to hold two belts simultaneously?", "answer": "Conor McGregor"},
        {"question": "Which UFC fighter has the most finishes in UFC history?", "answer": "Charles Oliveira"},
        {"question": "Who was the first woman to sign with the UFC?", "answer": "Ronda Rousey"},
        {"question": "Which UFC fighter is known for his iconic 'Flying Knee' knockout of Ben Askren?", "answer": "Jorge Masvidal"},
        {"question": "Who has the most performance of the night bonuses in UFC history?", "answer": "Charles Oliveira"}
    ]

    valid_answers = get_valid_answers()  # Get all accepted answers
    score = 0  # Initialize score

    for idx, q in enumerate(questions, 1):
        st.subheader(f"Q{idx}: {q['question']}")
        user_answer = st.text_input(f"Your Answer for Q{idx}:")

        if user_answer:
            correct_answers = valid_answers.get(q["answer"], [q["answer"].lower()])
            if user_answer.strip().lower() in [ans.lower() for ans in correct_answers]:
                score += 1
                st.markdown("✅ Correct!")
            else:
                st.markdown(f"❌ Incorrect! The correct answer is: {q['answer']}")

    # Show final score
    if score > 0:
        st.markdown(f"### You got {score} out of {len(questions)} correct!")
    else:
        st.markdown(f"### You got {score} out of {len(questions)} correct. Better luck next time!")

    # Leaderboard
    if username:
        update_leaderboard(username, score)

    # Display leaderboard
    show_leaderboard()

def update_leaderboard(username, score):
    """Updates the leaderboard with the player's score."""
    df = pd.read_csv(LEADERBOARD_FILE)

    if username in df["Username"].values:
        df.loc[df["Username"] == username, "Score"] = score
    else:
        new_entry = pd.DataFrame({"Username": [username], "Score": [score]})
        df = pd.concat([df, new_entry], ignore_index=True)

    df.to_csv(LEADERBOARD_FILE, index=False)

def show_leaderboard():
    """Displays the leaderboard."""
    df = pd.read_csv(LEADERBOARD_FILE)
    st.write("### 🏆 Leaderboard")
    st.table(df.sort_values(by="Score", ascending=False).head(10))
