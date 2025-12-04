import random

# Predefined responses organized by intent/keyword
responses = {
    "greetings": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "how_are_you": ["I'm a bot, but I'm doing well, thanks!", "I'm functioning smoothly!"],
    "bye": ["Goodbye!", "See you later!", "Bye, have a great day!"],
    "fallback": ["Sorry, I don't understand that.", "Can you rephrase that?", "I'm not sure how to respond."]
}

def get_bot_response(user_input):
    """
    Determines the chatbot's response based on user input.
    """
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return random.choice(responses["greetings"])
    elif "how are you" in user_input or "how are u" in user_input:
        return random.choice(responses["how_are_you"])
    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
        return random.choice(responses["bye"])
    else:
        # Default response if no pattern matches
        return random.choice(responses["fallback"])

def start_chat():
    """
    Runs the main chat loop.
    """
    print("Bot: Hi! I'm a simple chatbot. Type 'bye', 'exit' or 'quit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input)
        print(f"Bot: {response}")
        
        # Exit condition for the loop
        if "bye" in user_input.lower() or "exit" in user_input.lower() or "quit" in user_input.lower():
            break

# Run the chatbot
if __name__ == "__main__":
    start_chat()