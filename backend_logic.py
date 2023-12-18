import openai

openai.api_key = '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'

def q_and_a(user_interest):
    # Input text for generating a question and answer
    input_text = f"Create a quiz question about {user_interest}:"

    # Use OpenAI to generate question and answer
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_text,
        max_tokens=100  
    )

    generated_text = response['choices'][0]['text']

    # Extracting question and answer from the generated text
    question, *options = generated_text.split('\n')
    correct_answer = options[0].strip()  

    return question, options, correct_answer

if __name__ == "__main__":
    user_interest = input("Enter your topic of interest: ")

    question, answer_options, correct_answer = q_and_a(user_interest)

    # Print  generated question, answer options, and correct answer
    print("Question:", question)
    print("Answer Options:")
    for i, option in enumerate(answer_options, 1):
        print(f"{i}. {option}")
    print("Correct Answer:", correct_answer)
