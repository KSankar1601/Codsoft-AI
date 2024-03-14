def respond_to_weather_query(user_input):
    weather_keywords = ["weather", "forecast", "temperature", "rain", "sunny"]

    if any(word in user_input.lower() for word in weather_keywords):
        return "The weather today is sunny with a high of 75°F."
    else:
        return "I'm sorry, I don't understand. Can you please ask about the weather?"

def main():
    print("Hello! I'm the Weather Bot. How can I assist you today?")
    print("You can ask me about the weather forecast.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        else:
            response = respond_to_weather_query(user_input)
            print("Weather Bot:", response)

if __name__ == "__main__":
    main()
