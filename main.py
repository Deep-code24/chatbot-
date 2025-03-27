import random
import time

# Dictionary of responses based on keywords
responses = {
    "hello": ["hii", "hey", "hey what's up","Hi there!", "Hello!", "Hey, good to see you!"],
    "okay":["Yup"],
    "how are you": ["I'm doing great, thanks!", "Good, how about you?", "I'm an AI, so always good!"],
    "what is your name": ["I'm chatbot, nice to meet you!", "Call me Grok!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "what can you do": ["I can chat with you, answer simple questions, or just keep you company!"],
    "default": ["Sorry, I didn’t get that.", "Could you say that again?", "Hmm, not sure what you mean."]
}

# Function to get a response based on user input
def get_response(user_input):
    user_input = user_input.lower().strip()  # Convert to lowercase and remove extra spaces
    
    # Check for exact matches in the responses dictionary
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])  # Randomly pick one response from the list
    
    # If no match is found, return a default response
    return random.choice(responses["default"])

# Main chatbot loop
def chatbot():
    print("Chatbot: Hello! I'm here to chat with you. Type 'hello'to continue or  Type 'bye' to exit .")
    time.sleep(1)  # Small delay for a more natural feel
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Check if user wants to exit
        if "bye" in user_input.lower():
            print("Chatbot:", random.choice(responses["bye"]))
            break
        
        # Get and display the chatbot's response
        response = get_response(user_input)
        print("Chatbot:", response)
        time.sleep(0.5)  # Slight delay to simulate typing

# Start the chatbot
if __name__ == "__main__":
    chatbot()