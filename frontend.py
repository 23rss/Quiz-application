import streamlit as st
from backend_logic import generate_quiz

def main():
    st.title("Quiz Generator")

    # User input for quiz topic and no of questions
    topic = st.text_input("Enter your preferred quiz topic:")
    num_questions = st.slider("Select the number of questions:", 1, 10, 5)

    # Generate quiz based on user input
    if st.button("Generate Quiz"):
        questions, answer_options, correct_answers = generate_quiz(topic, num_questions)

        # Display quiz questions and answer options
        for i, question in enumerate(questions):
            st.write(f"\n**Question {i+1}:** {question}")
            selected_options = st.multiselect("Select the correct answer(s):", answer_options[i])
        
        # Submit quiz
        if st.button("Submit Quiz"):
            score = calculate_score(selected_options, correct_answers)
            st.write(f"\nYour Score: {score}/{num_questions}")

            # Display correct answers
            st.write("\nCorrect Answers:")
            for i, answer in enumerate(correct_answers):
                st.write(f"Question {i+1}: {answer}")

def calculate_score(selected_options, correct_answers):
    score = sum(1 for selected_option, correct_answer in zip(selected_options, correct_answers) if selected_option in correct_answer)
    return score

if __name__ == "__main__":
    main()