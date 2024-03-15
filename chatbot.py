import re

def respond_to_greeting(user_input):
    greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]

    # Using regular expressions to match user input against greetings
    pattern = re.compile("|".join(greetings), re.IGNORECASE)
    if re.match(pattern, user_input):
        return "Hello! How can I assist you today?"
    else:
        return "I'm sorry, I didn't catch that. Could you please try saying hello?"

def main():
    print("Hi there! I'm the Greeting Bot. What can I do for you?")
    print("Feel free to say hello to start the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        else:
            response = respond_to_greeting(user_input)
            print("Greeting Bot:", response)

if __name__ == "__main__":
    main()
