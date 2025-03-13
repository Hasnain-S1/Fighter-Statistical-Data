import streamlit as st

def trivia_page():
    st.title("❓ UFC Trivia")
    st.write("Test your knowledge with UFC-related trivia questions!")

    # Questions
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

    # Variable to track user score
    score = 0

    # Loop through each question and get the user's answer
    for idx, q in enumerate(questions, 1):
        st.subheader(f"Q{idx}: {q['question']}")
        user_answer = st.text_input(f"Your Answer for Q{idx}:")
        
        if user_answer:
            if user_answer.strip().lower() == q['answer'].lower():
                score += 1
                st.markdown("✅ Correct!")
            else:
                st.markdown(f"❌ Incorrect! The correct answer is: {q['answer']}")

    # Display final score after all questions are answered
    if score > 0:
        st.markdown(f"### You got {score} out of {len(questions)} correct!")
    else:
        st.markdown(f"### You got {score} out of {len(questions)} correct. Better luck next time!")


