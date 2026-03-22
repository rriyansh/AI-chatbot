import json
import random
import string


def load_intents(file_path):
    """
    Load intents from JSON file
    """
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def clean_text(text):
    """
    Clean user input text
    """
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text


def find_response(user_input, intents):
    """
    Find matching response based on keywords
    """
    user_input = clean_text(user_input)

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            pattern = clean_text(pattern)

            if pattern in user_input:
                return random.choice(intent["responses"])

    return "Sorry, I don't understand that. Please try something else."


def chatbot():
    """
    Main chatbot loop
    """
    print("My Bot is Running...")
    print("Type 'exit' to stop.\n")

    intents = load_intents("intents.json")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Goodbye! Have a nice day 👋")
            break

        response = find_response(user_input, intents)

        print("Bot:", response)


if __name__ == "__main__":
    chatbot()
